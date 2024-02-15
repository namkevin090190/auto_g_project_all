from cores.const.api.request import RequestConst
from cores.utils import RequestUtil, PrepareObj
from cores.model import ResponseObj, RequestObj

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models.ws1_core_tm.scheduler_tag import SchedulerTagModel


class SchedulerTagServices:

    def __init__(self):
        self.m_scheduler_tag = SchedulerTagModel()

    def create_scheduler_tag(self, request_id: str, id: str, pause_time: str):
        account_schedule_tag: dict = self.m_scheduler_tag.account_schedule_tag(
            id=id, test_pause_at_timestamp=pause_time).to_dict()
        self.m_scheduler_tag.request_data = self.m_scheduler_tag.RequestData(
            request_id=request_id, account_schedule_tag=account_schedule_tag).to_dict()
        data: RequestObj = PrepareObj.preparation(self.m_scheduler_tag)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.CORE_SERVER + ServicesConst.SchedulerTag.CREATE_SCHEDULER_TAG,
                                             data=data, is_convert=False)
        return r

    def update_scheduler_tag(self, request_id: str, id: str, pause_time: str, scheduler_tag_id: str):
        account_schedule_tag: dict = self.m_scheduler_tag.account_schedule_tag(
            id=id, test_pause_at_timestamp=pause_time).to_dict()
        update_mask: dict = self.m_scheduler_tag.update_mask(
            paths=['test_pause_at_timestamp']).to_dict()
        self.m_scheduler_tag.request_data = self.m_scheduler_tag.RequestData(
            request_id=request_id, account_schedule_tag=account_schedule_tag, update_mask=update_mask).to_dict()
        self.m_scheduler_tag.method = RequestConst.Method.PUT
        data: RequestObj = PrepareObj.preparation(self.m_scheduler_tag)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.CORE_SERVER +
                                             ServicesConst.SchedulerTag.UPDATE_SCHEDULER_TAG + scheduler_tag_id,
                                             data=data, is_convert=False)
        return r
