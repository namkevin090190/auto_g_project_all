from platforms.api.const.services_const import ServiceOutput
from platforms import step

from cores.utils import StoreUtil, GetUtil
from cores.model import ResponseObj

import uuid

from platforms.api.services.ws1_core_tm.flag import FlagServices


@step('[API][Flag] Grant VKYC for customer id <customer_id|current_customer_id>')
def grant_vkyc(customer_id: str):
    customer_id = GetUtil.spec_get(ServiceOutput.Customer.CREATE_CUSTOMER_RESPONSE).get(
        'id') if customer_id == 'current_customer_id' else customer_id
    result: ResponseObj = FlagServices().update_vkyc_flag(
        request_id=f'e2e_{str(uuid.uuid4())}', customer_id=customer_id)
    StoreUtil.spec_store(
        ServiceOutput.Flag.UPDATE_VKYC_FLAG_RESPONSE, result)
