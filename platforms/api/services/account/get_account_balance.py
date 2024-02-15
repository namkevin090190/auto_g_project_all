from cores.utils import RequestUtil, PrepareObj, GetUtil
from cores.model import ResponseObj, RequestObj
from cores.const.common import EnvironmentConst

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models import AccountBalanceModel


class AccountBalanceService:

    def __init__(self, token: str = None):
        if not token:
            token = GetUtil.spec_get(
                EnvironmentConst.Environment.TOKEN)
        self.obj = AccountBalanceModel(token=token)

    def get_account_info(self):
        data: RequestObj = PrepareObj.preparation(self.obj)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.INTERNAL_SERVER + ServicesConst.Account.ACCOUNT_BALANCE_ENDPOINT,
                                             data=data)
        return r