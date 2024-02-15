from pydantic import BaseModel
from dataclasses_json import dataclass_json
from dataclasses import dataclass, field

from platforms.api.const.common_const import ServerConst
from ..Common import Response, Data
from cores.const.api import RequestConst


class CasaModel(BaseModel):
    @dataclass_json
    @dataclass
    class instal_param_vals:
        status: str = 'active'

    @dataclass_json
    @dataclass
    class account:
        product_version_id: str = str()
        opening_timestamp: str = str()
        stakeholder_ids: list = field(default_factory=list)
        id: str = str()
        status: str = 'ACCOUNT_STATUS_OPEN'
        instance_param_vals: dict = field(default_factory=dict)

    @dataclass_json
    @dataclass
    class RequestData:
        request_id: str = int()
        account: dict = field(default_factory=dict)

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    header['x-auth-token'] = ServerConst.X_AUTH_TOKEN
    request_data: dict = dict()
