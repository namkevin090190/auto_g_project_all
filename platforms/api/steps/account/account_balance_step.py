from platforms.api.services.account import AccountBalanceService
from platforms.api.const import ServiceOutput
from platforms import step

from cores.utils import StoreUtil, GetUtil, VerifyResultUtil


@step(['[API][Account] Get Account info',
       '[API][Account] Get Account info <user_id>'])
def step_impl(user_id: str = None, token=None):
    if not user_id:
        pass
    r = AccountBalanceService(token).get_account_info()
    StoreUtil.spec_store(ServiceOutput.Account.ACCOUNT_INFO_RESPONSE, r)
    return r


#########
# Verify
########

@step('[API][Account] Verify Get Account Balance response')
def step_impl():
    result = GetUtil.spec_get(ServiceOutput.Account.ACCOUNT_INFO_RESPONSE)
    VerifyResultUtil.verify_request_succesfully(result)
