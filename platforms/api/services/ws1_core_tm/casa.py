from cores.const.api.request import RequestConst
from cores.utils import RequestUtil, PrepareObj
from cores.model import ResponseObj, RequestObj

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models.ws1_core_tm.casa import CasaModel


class CasaServices:

    def __init__(self):
        self.m_casa = CasaModel()

    def __parse_account(self, product_version_id: str, opening_timestamp: str, stakeholder_ids: list, id: str):
        return self.m_casa.account(
            product_version_id=product_version_id, opening_timestamp=opening_timestamp, stakeholder_ids=stakeholder_ids, id=id, instance_param_vals=self.m_casa.instal_param_vals().to_dict()).to_dict()

    def create_casa(self, request_id: str, product_version_id: str, opening_timestamp: str, stakeholder_ids: list, id: str):
        self.m_casa.request_data = self.m_casa.RequestData(
            request_id=request_id, account=self.__parse_account(product_version_id=product_version_id, opening_timestamp=opening_timestamp, stakeholder_ids=stakeholder_ids, id=id)).to_dict()
        data: RequestObj = PrepareObj.preparation(self.m_casa)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.CORE_SERVER + ServicesConst.Casa.CREATE_CASA,
                                             data=data, is_convert=False)
        return r

    def get_casa(self, account_id: str, pause_time: str):
        self.m_casa.request_data = None
        self.m_casa.method = RequestConst.Method.QUERY
        url: str = ServerConst.CORE_SERVER + ServicesConst.Casa.GET_CASA + \
            f'{account_id}?fields_to_include=INCLUDE_FIELD_DERIVED_INSTANCE_PARAM_VALS' if pause_time == None else ServerConst.CORE_SERVER + ServicesConst.Casa.GET_CASA + \
            f'{account_id}?fields_to_include=INCLUDE_FIELD_DERIVED_INSTANCE_PARAM_VALS&instance_param_vals_effective_timestamp={pause_time}'
        data: RequestObj = PrepareObj.preparation(self.m_casa)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=url,
                                             data=data, is_convert=False)
        return r
