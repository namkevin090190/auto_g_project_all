from platforms.api.const.services_const import ServiceOutput
from platforms import step
from platforms.api.const.ws1.ws1_const import WOneConst
from platforms.api.services.ws1_core_tm.product import ProductServices

from cores.utils import StoreUtil, GetUtil
from cores.model import ResponseObj

import uuid


@step('[API][Product] Create product')
def create_product():
    schedule_tag_id = '' if not GetUtil.spec_get(
        ServiceOutput.SchedulerTag.CREATE_SCHEDULER_TAG_RESPONSE).get('id') else GetUtil.spec_get(ServiceOutput.SchedulerTag.CREATE_SCHEDULER_TAG_RESPONSE).get('id')
    result: ResponseObj = ProductServices().create_product(
        request_id=f'e2e_{str(uuid.uuid4())}', product_id=f'e2e_{str(uuid.uuid4())}', schedule_tag_id=schedule_tag_id)
    StoreUtil.spec_store(
        ServiceOutput.Product.CREATE_PRODUCT_RESPONSE, result)


@step('[API][Product] Get product info of Product version id <product_version_id|current_product_version_id|official_product_version_id>')
def get_product_info(product_version_id: str):
    product_version_id = WOneConst.PRODUCT_VERSION_ID if product_version_id == 'official_product_version_id' else GetUtil.spec_get(
        ServiceOutput.Product.CREATE_PRODUCT_RESPONSE).get('id') if product_version_id == 'current_product_version_id' else product_version_id
    result: ResponseObj = ProductServices().get_product_info(product_version_id)
    StoreUtil.spec_store(
        ServiceOutput.Product.GET_PRODUCT_INFO_RESPONSE, result)
