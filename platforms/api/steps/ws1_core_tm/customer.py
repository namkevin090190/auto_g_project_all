from cores.utils.common.assertion_util import AssertUtil
from platforms.api.const.services_const import ServiceOutput
from platforms.api.const.ws1.ws1_scheme import CustomerScheme
from platforms.api.services.ws1_core_tm.customer import CustomerServices
from platforms import step

from cores.utils import StoreUtil, DataGeneratorUtil
from cores.model import ResponseObj

import uuid


@step('[API][Customer] Create customer')
def create_customer():
    detail_name = DataGeneratorUtil().detail_name_generator()
    result: ResponseObj = CustomerServices().create_customer(request_id=f'e2e_{str(uuid.uuid4())}', identifier_data=DataGeneratorUtil().phone_generator(), first_name=detail_name["first_name"], last_name=detail_name["last_name"], email_address=f'{detail_name["first_name"]}_{detail_name["last_name"]}@gmail.com', mobile_phone_num=DataGeneratorUtil(
    ).phone_generator(), external_cus_id=DataGeneratorUtil().phone_generator(), password=DataGeneratorUtil().random_number_generator(length=8), id=f'e2e_{DataGeneratorUtil().random_number_generator(length=7)}', schema=CustomerScheme.CreateCustomerSuccessScheme)
    StoreUtil.spec_store(
        ServiceOutput.Customer.CREATE_CUSTOMER_RESPONSE, result)
