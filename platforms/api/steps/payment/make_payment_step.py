from platforms.api.services.payment import InitPaymentService
from platforms.api.const import ServiceOutput
from platforms import step

from cores.utils import GetUtil, StoreUtil, VerifyResultUtil
from cores.model import ResponseObj


@step('[API][Payment] Init new payment <device_id> and code <btc_code>')
def init_new_payment(device_id, btc_code):
    r = InitPaymentService().init_payment(device_id=device_id,
                                          btc_code=btc_code)
    StoreUtil.spec_store(ServiceOutput.Payment.INIT_PAYMENT_RESPONSE, r)
    return r


@step('[API][Payment] Verify init new payment successfully')
def verify_init_new_payment():
    result: ResponseObj = GetUtil.spec_get(
        ServiceOutput.Payment.INIT_PAYMENT_RESPONSE)
    VerifyResultUtil.verify_request_succesfully(result)
