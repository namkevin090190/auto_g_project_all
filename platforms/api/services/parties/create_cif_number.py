from cores.utils import RequestUtil, PrepareObj, GetUtil
from cores.model import ResponseObj, RequestObj
from cores.const.common import EnvironmentConst

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models import CIFModel


class CreateCifNumber:
    def __init__(self, token: str = None):
        if not token:
            token = GetUtil.spec_get(
                EnvironmentConst.Environment.TOKEN)
        self.object = CIFModel(token=token)

    def create_cif_no(self):
        data: RequestObj = PrepareObj.preparation(self.object)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.INGRESS_SERVER +
                                             ServicesConst.Parties.VIKKI_ACCOUNT_VIEW_ENDPOINT,
                                             data=data)
        return r
