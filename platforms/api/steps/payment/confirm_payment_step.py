from platforms.api.services.payment import ConfirmPayment
from platforms.api.const import ServiceOutput
from platforms import step

from cores.utils import GetUtil, StoreUtil, VerifyResultUtil
from cores.model import ResponseObj


@step('[API][Payment] Confirm payment\
    device_id: <device_id>\
    btc_code: <btc_code>\
    remitter_account_number: <remitter_account_number>\
    <beneficiary_bank_id>\
    beneficiary_account_number: <beneficiary_account_number>\
    beneficiary_account_name: <beneficiary_account_name>\
    otp_code: <otp_code>\
    payment_type: <payment_type>\
    amount: <amount>\
    for payment_id: <payment_id>'
      )
def confirm_pyament(device_id,
                    btc_code,
                    remitter_account_number,
                    beneficiary_bank_id,
                    beneficiary_account_number,
                    beneficiary_account_name,
                    otp_code,
                    payment_type,
                    amount,
                    payment_id=None):
    if not payment_id:
        payment_id = GetUtil.spec_get(
            ServiceOutput.Payment.INIT_PAYMENT_RESPONSE).response_data['payment_id']
    params = dict(payment_id=payment_id,
                  device_id=device_id,
                  btc_code=btc_code,
                  remitter_account_number=remitter_account_number,
                  beneficiary_bank_id=beneficiary_bank_id,
                  beneficiary_account_number=beneficiary_account_number,
                  beneficiary_account_name=beneficiary_account_name,
                  otp_code=otp_code,
                  payment_type=payment_type,
                  amount=amount)
    r = ConfirmPayment().confirm_payment(**params)
    StoreUtil.spec_store(ServiceOutput.Payment.INIT_PAYMENT_RESPONSE, r)
    return r


@step('[API][Payment] Verify init new payment successfully')
def verify_init_new_payment():
    result: ResponseObj = GetUtil.spec_get(
        ServiceOutput.Payment.INIT_PAYMENT_RESPONSE)
    VerifyResultUtil.verify_request_succesfully(result)
