from pydantic import BaseModel
from dataclasses_json import dataclass_json
from dataclasses import dataclass, field

from platforms.api.const.common_const import ServerConst
from ..Common import Response, Data
from cores.const.api import RequestConst


class SchedulerTagModel(BaseModel):
    @dataclass_json
    @dataclass
    class update_mask:
        paths: list = field(default_factory=list)

    @dataclass_json
    @dataclass
    class account_schedule_tag:
        id: str = str()
        description: str = 'e2e'
        sends_scheduled_operation_reports: bool = True
        schedule_status_override: str = 'ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_TO_ENABLED'
        schedule_status_override_start_timestamp: str = '2018-04-10T20:14:37.808587Z'
        schedule_status_override_end_timestamp: str = '9999-12-31T23:59:59Z'
        test_pause_at_timestamp: str = str()

    @dataclass_json
    @dataclass
    class RequestData:
        request_id: str = int()
        account_schedule_tag: dict = field(default_factory=dict)
        update_mask: dict = field(default_factory=dict)

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    header['x-auth-token'] = ServerConst.X_AUTH_TOKEN
    request_data: dict = dict()
