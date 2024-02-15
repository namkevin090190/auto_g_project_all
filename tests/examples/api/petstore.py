from platforms.api.models import Data

from cores.utils import PrepareObj, RequestUtil
from cores.model.request import RequestObj
from cores.const.api import RequestConst


class PetStore:

    @staticmethod
    def create_pet():
        __body = {
            "id": 0,
            "category": {
                "id": 0,
                "name": "test"
            },
            "name": "doggie",
                    "photoUrls": [
                        "string"
            ],
            "tags": [
                        {
                            "id": 0,
                            "name": "test"
                        }
            ],
            "status": "available"
        }
        __url = 'https://petstore.swagger.io/v2/pet'
        __header = Data.header
        __obj = {
            'header': __header,
            'method':  RequestConst.Method.POST,
            'body': __body
        }
        body = RequestObj(**__obj)
        r = RequestUtil.request(method=body.method,
                                data=body,
                                url=__url,
                                is_convert=False)
        return r

    @staticmethod
    def retrieve_pet_info(pet_id: int):
        __url = f'https://petstore.swagger.io/v2/pet/{pet_id}'
        __header = Data.header
        __obj = {
            'header': __header,
            'method':  RequestConst.Method.GET,
            'body': None
        }
        body = RequestObj(**__obj)
        r = RequestUtil.request(method=body.method,
                                url=__url,
                                data=body,
                                is_convert=False)
        return r
