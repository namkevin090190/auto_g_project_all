from cores.utils import RequestUtil, PrepareObj
from cores.model import ResponseObj, RequestObj

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models.ws1_core_tm.customer import CustomerModel


class CustomerServices:

    def __init__(self):
        self.m_customer = CustomerModel()

    def __parse_customer(self, identifier_data: str, first_name: str, last_name: str, email_address: str, mobile_phone_num: str, external_cus_id: str, password: str, id: str):
        identifier: dict = self.m_customer.identifiers(
            identifier=identifier_data).to_dict()
        customer_details: dict = self.m_customer.customer_details(
            first_name=first_name, last_name=last_name, email_address=email_address, mobile_phone_number=mobile_phone_num, external_customer_id=external_cus_id).to_dict()
        customer: dict = self.m_customer.customer(
            password=password, id=id, customer_details=customer_details, identifiers=[identifier]).to_dict()
        return customer

    def create_customer(self, request_id: str, identifier_data: str, first_name: str, last_name: str, email_address: str, mobile_phone_num: str, external_cus_id: str, password: str, id: str, schema: object = None):
        self.m_customer.request_data = self.m_customer.RequestData(
            request_id=request_id, customer=self.__parse_customer(identifier_data=identifier_data, first_name=first_name, last_name=last_name, email_address=email_address, mobile_phone_num=mobile_phone_num, external_cus_id=external_cus_id, password=password, id=id)).to_dict()
        data: RequestObj = PrepareObj.preparation(self.m_customer)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.CORE_SERVER + ServicesConst.Customer.CREATE_CUSTOMER,
                                             data=data, schema=schema)
        return r
