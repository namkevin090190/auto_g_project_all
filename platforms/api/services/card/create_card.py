from cores.utils import RequestUtil, PrepareObj, GetUtil
from cores.model import ResponseObj, RequestObj
from cores.const.common import EnvironmentConst

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models import CardInfoModel


class CreateCard:
    def __init__(self):
        self.object = CardInfoModel()

    def create_card(self, **kwargs):
        p = kwargs
        self.object.request_data = self.object.RequestData(
            **p).to_dict()
        data: RequestObj = PrepareObj.preparation(self.object)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.INGRESS_SERVER +
                                             ServicesConst.Card.CARD_CREATE_ENDPOINT,
                                             data=data)
        return r
