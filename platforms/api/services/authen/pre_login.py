from cores.utils import RequestUtil, PrepareObj
from cores.model import ResponseObj, RequestObj
from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models import PreLoginModel


class PreLoginService:

    def __init__(self):
        self.m_PreLogin = PreLoginModel()

    def pre_login(self, device_id: str, client_id: str) -> ResponseObj:

        self.m_PreLogin.request_data = self.m_PreLogin.RequestData(deviceId=device_id,
                                                                   clientId=client_id).to_dict()
        data: RequestObj = PrepareObj.preparation(self.m_PreLogin)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.INGRESS_SERVER + ServicesConst.Authen.PRE_LOGIN_ENDPOINT,
                                             data=data)
        return r
