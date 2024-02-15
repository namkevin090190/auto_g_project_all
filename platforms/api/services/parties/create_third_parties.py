from cores.utils import RequestUtil, PrepareObj, GetUtil
from cores.model import ResponseObj, RequestObj
from cores.const.common import EnvironmentConst

from platforms.api.const import ServicesConst, ServerConst, ServiceOutput
from platforms.api.models import AccountCommon, ThirdPartiesModel


class CBSCustomer():
    cbsProductType: str = 'current_account'
    cbsAccountNumber: int = GetUtil.spec_get(
        ServiceOutput.Account.ACCOUNT_CREATE_RESPONSE).response_data.account_number
    cmsCustomerNumber: int = GetUtil.spec_get(
        ServiceOutput.Parties.CREATE_CBS_ACC_RESPONSE).response_data.cbs_customer_id
    cmsCardNumber: int = 2799080
    cifNumber: int = GetUtil.spec_get(
        ServiceOutput.Parties.CREATE_CIF_NO_RESPONSE).response_data.cif_number
    cbsCustomerId: int = int()


class ThirdPartyRequestData:
    address: list = [setattr(AccountCommon.Address, 'type', i)
                     for i in ['resident', 'origin', 'current']]
    national_id = AccountCommon.NationalID.to_json()
    device: {
        'device_id': ''
    }
    accounts: list = [
        CBSCustomer()
    ]


class Create3rdPaties:
    def __init__(self):
        self.object = ThirdPartiesModel()

    def __prepare_3rd_parties_payload() -> dict:
        pass

    def create_cbs_account(self, **kwargs):
        p = kwargs
        self.object.request_data = self.__prepare_3rd_parties_payload()
        data: RequestObj = PrepareObj.preparation(self.object)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.INGRESS_SERVER +
                                             ServicesConst.Parties.PARTY_CREATE_ENDPOINT,
                                             data=data)
        return r
