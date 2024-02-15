from typing import Optional
from pydantic import BaseModel
from dataclasses_json import dataclass_json
from dataclasses import dataclass


from .Common import Response, AccountCommon, Data
from cores.const.api import RequestConst


class CardInfoModel(BaseModel):

    @dataclass_json
    @dataclass
    class RequestData(AccountCommon):
        cifNumber: Optional[int] = int()
        accountNumber: Optional[int] = int()
        onboardingId: Optional[int] = int()

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    token: str = Data.token
    request_data: dict = dict()
