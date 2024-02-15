from platforms.api.services.account import AccountInfoService
from platforms.api.const import ServiceOutput
from platforms import step

from cores.utils import StoreUtil


@step(['[API][Account] Get Account info',
       '[API][Account] Get Account info <user_id>'])
def step_impl(user_id: str = None, token: str = None):
    if not user_id:
        pass
    r = AccountInfoService(token).get_account_info()
    StoreUtil.spec_store(ServiceOutput.Account.ACCOUNT_INFO_RESPONSE, r)
    return r


@step('[API][Account] Verify Get Account info response')
def step_impl():
    pass
