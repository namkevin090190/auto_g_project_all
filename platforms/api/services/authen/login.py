from cores.utils import RequestUtil, PrepareObj, GetUtil
from cores.model import ResponseObj, RequestObj
from cores.const.common import EnvironmentConst

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models import LoginModel


class LoginService:

    def __init__(self, token: str = None):
        if not token:
            token = GetUtil.spec_get(
                EnvironmentConst.Environment.TOKEN)
        self.m_Login = LoginModel(token=token)

    def login(self, device_id: str, username: str, password: str):
        self.m_Login.request_data = self.m_Login.RequestData(deviceId=device_id,
                                                             username=username,
                                                             password=password).to_dict()
        data: RequestObj = PrepareObj.preparation(self.m_Login)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.INGRESS_SERVER + ServicesConst.Authen.LOGIN_ENDPOINT,
                                             data=data)
        return r
