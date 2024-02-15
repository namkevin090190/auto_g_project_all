from platforms.api.services.authen import LoginService, PreLoginService
from platforms.api.const import ServiceOutput
from platforms import step

from cores.utils import GetUtil, StoreUtil, VerifyResultUtil
from cores.const.common import EnvironmentConst as const
from cores.model import ResponseObj


@step('[API][Authen] Login with <username> and <password> in device <device_id>')
def login(username: str, password: str, device_id: str):
    result: ResponseObj = PreLoginService().pre_login(device_id=device_id,
                                                      client_id='1f1sqesvlhqnigjgrfjmdotjfp')
    StoreUtil.spec_store(const.Environment.TOKEN,
                             result.response_data['accessToken'])
    r = LoginService().login(username=username, password=password, device_id=device_id)
    StoreUtil.spec_store(ServiceOutput.Authen.LOGIN_RESPONSE, r)


@step('[API][Authen] Verify login successfully')
def verify_login():
    result: ResponseObj = GetUtil.spec_get(
        ServiceOutput.Authen.LOGIN_RESPONSE)
    VerifyResultUtil.verify_request_succesfully(result)
