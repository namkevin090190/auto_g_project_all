from cores.utils import RequestUtil, PrepareObj
from cores.model import ResponseObj, RequestObj

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models import AccountInfoModel


class AccountInfoService:

    def __init__(self):
        # if not token:
        #     token = GetUtil.spec_get(
        #         EnvironmentConst.Environment.TOKEN)
        self.obj = AccountInfoModel()

    def get_account_info(self, cbs_account_no: int):
        self.obj.request_data = self.obj.RequestData(
            cbsAccountNumber=cbs_account_no)
        data: RequestObj = PrepareObj.preparation(self.obj)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.INTERNAL_SERVER + ServicesConst.Account.ACCOUNT_DETAIL_ENDPOINT,
                                             data=data)
        return r
