from requests.models import Response

from cores.utils import DataGeneratorUtil, AssertUtil, logger
from cores.const.api import RequestConst

from platforms.api.const import ServerConst, ServicesConst

from platforms.api.services.authen import PreLoginService, LoginService
from platforms.api.services.account import AccountInfoService


class BenchLogin:

    def __init__(self, client, token=None):
        self.client = client
        self.header = {"Authorization": f"Bearer {token}"}

    def pre_login(self, device_id: str, client_id: str):
        m_pre = PreLoginService().m_PreLogin
        m_pre.request_data = m_pre.RequestData(deviceId=device_id,
                                               clientId=client_id).to_json()
        r: Response = self.client.post(url=ServerConst.INGRESS_SERVER + ServicesConst.Authen.PRE_LOGIN_ENDPOINT,
                                       headers=m_pre.header, data=m_pre.request_data)

        AssertUtil.equal(r.status_code, RequestConst.StatusCode.OK)
        AssertUtil.equal(r.json()['status']['code'].lower(),
                         RequestConst.Message.OK)
        return r.json()['payload']['accessToken']

    def login(self, token, username: str, password: str, device_id: str):
        m_login = LoginService(token=token).m_Login
        m_login.request_data = m_login.RequestData(username=username,
                                                   password=password,
                                                   deviceId=device_id).to_json()
        r: Response = self.client.post(ServerConst.INGRESS_SERVER + ServicesConst.Authen.LOGIN_ENDPOINT,
                                       headers=m_login.header, data=m_login.request_data)
        AssertUtil.equal(r.status_code, RequestConst.StatusCode.OK)
        AssertUtil.equal(r.json()['status']['code'].lower(),
                         RequestConst.Message.OK)

    def get_account_info(self, cbs_account_no):
        m_acc = AccountInfoService().obj
        m_acc.request_data = m_acc.RequestData(
            cbsAccountNumber=cbs_account_no).to_json()
        r: Response = self.client.post(ServerConst.INTERNAL_SERVER + ServicesConst.Account.ACCOUNT_DETAIL_ENDPOINT,
                                       headers=m_acc.header,
                                       data=m_acc.request_data)
        AssertUtil.equal(r.status_code, RequestConst.StatusCode.OK)
        AssertUtil.equal(r.json()['status']['code'].lower(),
                         RequestConst.Message.OK)

    def get_account_balance(self):
        pass

    def logout(self):
        pass
