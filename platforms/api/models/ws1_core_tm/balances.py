from pydantic import BaseModel
from dataclasses_json import dataclass_json
from dataclasses import dataclass, field

from platforms.api.const.common_const import ServerConst
from ..Common import Response, Data
from cores.const.api import RequestConst


class BalancesModel(BaseModel):

    @dataclass_json
    @dataclass
    class RequestData:
        pass

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.QUERY
    header: dict = Data.header
    header['x-auth-token'] = ServerConst.X_AUTH_TOKEN
    request_data: dict = dict()
