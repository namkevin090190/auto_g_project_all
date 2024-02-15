from typing import Optional

from cores.utils import RequestUtil, PrepareObj, GetUtil
from cores.model import ResponseObj, RequestObj
from cores.const.common import EnvironmentConst

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models import InitPaymentModel


class InitPaymentService:

    def __init__(self, token: str = None):
        if not token:
            token = GetUtil.spec_get(
                EnvironmentConst.Environment.TOKEN)
        self.m_payment = InitPaymentModel(token=token)

    def init_payment(self, device_id: str, btc_code: str, otp_message: Optional[str]):
        self.m_payment.request_data = self.m_payment.RequestData(btcCode=btc_code,
                                                                 deviceId=device_id,
                                                                 otpMessageFooter=otp_message).to_dict()
        data: RequestObj = PrepareObj.preparation(self.m_payment)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.INGRESS_SERVER + ServicesConst.Payment.INIT_PAYMENT_ENDPOINT,
                                             data=data)
        return r
