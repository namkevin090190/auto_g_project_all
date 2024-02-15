from cores.utils import RequestUtil, PrepareObj, GetUtil
from cores.model import ResponseObj, RequestObj
from cores.const.common import EnvironmentConst

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models import AccountModel


class CreateAccount:

    def __init__(self):
        self.obj = AccountModel()

    def get_account_info(self):
        data: RequestObj = PrepareObj.preparation(self.obj)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.INTERNAL_SERVER + ServicesConst.Account.ACCOUNT_CREATE_ENDPOINT,
                                             data=data)
        return r
