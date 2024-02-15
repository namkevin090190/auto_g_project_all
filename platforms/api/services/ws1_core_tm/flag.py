from cores.utils import RequestUtil, PrepareObj
from cores.model import ResponseObj, RequestObj

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models.ws1_core_tm.flag import FlagModel


class FlagServices:

    def __init__(self):
        self.m_flag = FlagModel()

    def update_vkyc_flag(self, request_id: str, customer_id: str):
        flag: dict = self.m_flag.flag(customer_id=customer_id).to_dict()
        self.m_flag.request_data = self.m_flag.RequestData(
            request_id=request_id, flag=flag).to_dict()
        data: RequestObj = PrepareObj.preparation(self.m_flag)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.CORE_SERVER + ServicesConst.Flag.UPDATE_FLAG,
                                             data=data, is_convert=False)
        return r
