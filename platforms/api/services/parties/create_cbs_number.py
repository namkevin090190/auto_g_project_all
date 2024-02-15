from cores.utils import RequestUtil, PrepareObj, GetUtil
from cores.model import ResponseObj, RequestObj
from cores.const.common import EnvironmentConst

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models import CBSCustomerModel


class CreateCBSAccount:
    def __init__(self, token: str = None):
        if not token:
            token = GetUtil.spec_get(
                EnvironmentConst.Environment.TOKEN)
        self.object = CBSCustomerModel(token=token)

    def create_cbs_account(self, **kwargs):
        p = kwargs
        self.object.request_data = self.object.RequestData(
            **p).to_dict()
        data: RequestObj = PrepareObj.preparation(self.object)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.INGRESS_SERVER +
                                             ServicesConst.Parties.CBS_ACCOUNCT_CREATE_ENDPOINT,
                                             data=data)
        return r
