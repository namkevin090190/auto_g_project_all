from cores.utils import RequestUtil, PrepareObj, GetUtil
from cores.model import ResponseObj, RequestObj
from cores.const.common import EnvironmentConst

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models import ConfirmPaymentModel


class ConfirmPayment:

    def __init__(self, token: str = None):
        if not token:
            token = GetUtil.spec_get(
                EnvironmentConst.Environment.TOKEN)
        self.m_confirm_payment = ConfirmPaymentModel(token=token)

    def confirm_payment(self, **kwargs):
        p = kwargs
        self.m_confirm_payment.request_data = self.m_confirm_payment.RequestData(
            **p).to_dict()
        data: RequestObj = PrepareObj.preparation(self.m_confirm_payment)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.INGRESS_SERVER +
                                             ServicesConst.Payment.COFNIRM_PAYMENT_ENDPOINT.format(
                                                 payment_id=p['payment_id']),
                                             data=data)
        return r
