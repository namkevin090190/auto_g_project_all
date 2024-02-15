import json
import os
from typing import Dict

import curl
from jsonschema import validate
import requests
from requests import Response, RequestException
from requests.exceptions import Timeout, ConnectTimeout

from cores.const.common import EnvironmentConst
from cores.const.api import RequestConst
from cores.model import ResponseObj, RequestObj
from cores.decorators import handle_exception
from cores.utils.logger_util import logger


class RequestUtil:

    __log = '''
        - Method: %(method)s
        ====================
        - Url: %(url)s
        ====================
        - Curl: %(r_curl)s
        ====================
        - Header: %(header)s
        ====================
        - Data:   %(data)s
        ====================
        - StatusCode: %(code)s
        ====================
        Response: %(rsp)s
        '''

    def _log(url: str = None, headers: Dict = None, data: Dict = None, response: Response = None,
             log_level=os.getenv('LOG_LEVEL') if os.getenv(
                 'LOG_LEVEL') else EnvironmentConst.Logger.INFO,
             method: str = str()):
        _data = RequestUtil.__log % {'method': method.upper(),
                                     'url': url if url else None,
                                     'r_curl': curl.parse(response, return_it=True) if response else None,
                                     'header': headers if headers else None,
                                     'data': data if data else None,
                                     'code': response.status_code if response else None,
                                     'rsp': response.text}
        if log_level == EnvironmentConst.Logger.INFO:
            # logger.info(_data)
            pass

        elif log_level == EnvironmentConst.Logger.DEBUG:
            logger.debug(
                f'Pretty Payload:\n{_data}\nFull Response:\n{response.json()}')
        elif log_level == EnvironmentConst.Logger.ERROR:
            logger.error(_data)
        else:
            logger.warning('Not support this log value')

    def _parse_data(response: Response):
        return ResponseObj(**dict(status_code=response.status_code,
                                  status_msg='' if not response.json().get('status') else
                                  response.json().get('status').get('code'),
                                  message='' if not (response.json().get('status').get(
                                      'message')) else response.json().get('status').get('message'),
                                  response_data=response.json().get('payload') if response.json().get(
                                      'payload') else response.json(),
                                  meta_data=response.json().get('meta')
                                  )
                           )

    @handle_exception
    def _post(url: str, data: RequestObj) -> Response:
        body = None
        if data.header:
            body = json.dumps(data.request_data)
        else:
            body = data.request_data
        return requests.post(url=url, headers=data.header, data=body)

    @handle_exception
    def _get(url: str) -> Response:
        return requests.get(url)

    @handle_exception
    def _query(url: str, data: RequestObj = None, query: str = None) -> Response:
        return requests.get(url, headers=data.header, params={'q': query})

    @handle_exception
    def _put(url: str, data: RequestObj) -> Response:
        return requests.put(url, headers=data.header, data=json.dumps(data.request_data))

    @handle_exception
    def _patch(url: str, data: RequestObj) -> Response:
        return requests.patch(url=url, headers=data.header,
                              data=json.dumps(data.request_data))

    @handle_exception
    def _delete(url: str, data: RequestObj) -> Response:
        return requests.delete(url, headers=data.header, data=data.request_data)

    # @staticmethod
    # def post_with_oauth(url: str, header: str, data: str, json_flag=False):
    #     logger.debug('/POST url: %s \n header: %s \n data: %s' %
    #                  (url, header, data))
    #     r = requests.post(url, headers=header, data=data)
    #     logger.debug(r.json())
    #     return r.json() if json_flag else Json2Obj.convert_json_to_object(r.json())

    @handle_exception
    def _attach(url: str, data: RequestObj) -> Response:
        return requests.post(url, headers=data.header, files=data.files)

    @staticmethod
    def __retry_until_die(max_retries: int = 2, resp: Response = Response(), request_url: str = str(), data: ResponseObj = ResponseObj(),
                          is_convert: bool = False, method: str = str(), schema: object = None) -> ResponseObj or None:
        """Retry while timeout, do not apply for failed request

        Args:
            max_retries (int, optional): _description_. Defaults to 2.
            resp (Response, optional): _description_. Defaults to Response().
            request_url (str, optional): _description_. Defaults to str().
            data (ResponseObj, optional): _description_. Defaults to ResponseObj().
            is_convert (bool, optional): _description_. Defaults to False.
            method (str, optional): _description_. Defaults to str().
            schema  (object,option): response schema. Defaults to None.

        Raises:
            Exception: Not really rasie exception, but warn the timeout occurs then do the retry

        Returns:
            ResponseObj or None: _description_
        """
        for retry in range(max_retries):
            try:
                if resp.status_code in (RequestConst.StatusCode.OK, RequestConst.StatusCode.CREATED):
                    RequestUtil._log(url=request_url, headers=data.header,
                                     data=data.request_data, response=resp, method=method)
                    if schema != None:
                        validate(instance=resp.json(), schema=schema)
                    return RequestUtil._parse_data(resp) if is_convert else resp.json()
                else:
                    logger.error(RequestException(
                        f'Error with code: {resp.status_code} \nmessage {resp.json()}'))
                    RequestUtil._log(url=request_url, headers=data.header,
                                     data=data.request_data, log_level=EnvironmentConst.Logger.ERROR, method=method)
            except (Timeout, ConnectTimeout):
                logger.warning('Timeout occurred! Retrying!')
                pass
            if retry == max_retries:
                raise Exception(f'Failed to making request!')

    @staticmethod
    def request(method: str, url: str, data: RequestObj, is_convert: bool = False, schema: object = None) -> ResponseObj:
        response: ResponseObj
        match method:
            case RequestConst.Method.GET:
                response = RequestUtil.__retry_until_die(resp=RequestUtil._get(url=url),
                                                         request_url=url, data=data, is_convert=is_convert, method=method, schema=schema)
            case RequestConst.Method.QUERY:
                response = RequestUtil.__retry_until_die(resp=RequestUtil._query(url=url, data=data),
                                                         request_url=url, data=data, is_convert=is_convert, method=method, schema=schema)
            case RequestConst.Method.POST:
                response = RequestUtil.__retry_until_die(resp=RequestUtil._post(url=url, data=data),
                                                         request_url=url, data=data, is_convert=is_convert, method=method, schema=schema)
            case RequestConst.Method.PUT:
                response = RequestUtil.__retry_until_die(resp=RequestUtil._put(url=url, data=data),
                                                         request_url=url, data=data, is_convert=is_convert, method=method, schema=schema)
            case RequestConst.Method.ATTACH:
                response = RequestUtil.__retry_until_die(resp=RequestUtil._attach(url=url, data=data),
                                                         request_url=url, data=data, is_convert=is_convert, method=method, schema=schema)
            case RequestConst.Method.DELETE:
                response = RequestUtil.__retry_until_die(resp=RequestUtil._delete(url=url),
                                                         request_url=url, is_convert=is_convert, method=method, schema=schema)
            case _:
                raise Exception(f'Not support {method}')
        return response
