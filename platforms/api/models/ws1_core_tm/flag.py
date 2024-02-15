from pydantic import BaseModel
from dataclasses_json import dataclass_json
from dataclasses import dataclass, field

from platforms.api.const.common_const import ServerConst
from ..Common import Response, Data
from cores.const.api import RequestConst


class FlagModel(BaseModel):

    @dataclass_json
    @dataclass
    class flag:
        flag_definition_id: str = 'VKYC'
        description: str = 'VKYC'
        customer_id: str = str()

    @dataclass_json
    @dataclass
    class RequestData:
        request_id: str = int()
        flag: dict = field(default_factory=dict)

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    header['x-auth-token'] = ServerConst.X_AUTH_TOKEN
    request_data: dict = dict()
