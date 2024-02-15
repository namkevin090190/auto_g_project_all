from platforms.api.const.services_const import ServiceOutput
from platforms import step
from platforms.api.services.ws1_core_tm.scheduler_tag import SchedulerTagServices


from cores.utils import StoreUtil, GetUtil
from cores.model import ResponseObj

import uuid


@step('[API][SchedulerTag] Create Scheduler Tag with pause_time <pause_time>')
def create_scheduler_tag(pause_time: str):
    result: ResponseObj = SchedulerTagServices().create_scheduler_tag(
        request_id=f'e2e_{str(uuid.uuid4())}', id=f'e2e_{str(uuid.uuid4())}', pause_time=pause_time)
    StoreUtil.spec_store(
        ServiceOutput.SchedulerTag.CREATE_SCHEDULER_TAG_RESPONSE, result)


@step('[API][SchedulerTag] Update Scheduler Tag <scheduler_tag_id|current_scheduler_tag_id> with pause_time <new_pause_time>')
def update_scheduler_tag(scheduler_tag_id: str, new_pause_time: str):
    scheduler_tag_id = GetUtil.spec_get(
        ServiceOutput.SchedulerTag.CREATE_SCHEDULER_TAG_RESPONSE).get('id') if scheduler_tag_id == 'current_scheduler_tag_id' else scheduler_tag_id
    result: ResponseObj = SchedulerTagServices().update_scheduler_tag(
        request_id=f'e2e_{str(uuid.uuid4())}', id=f'e2e_{str(uuid.uuid4())}', pause_time=new_pause_time, scheduler_tag_id=scheduler_tag_id)
    StoreUtil.spec_store(
        ServiceOutput.SchedulerTag.CREATE_SCHEDULER_TAG_RESPONSE, result)
