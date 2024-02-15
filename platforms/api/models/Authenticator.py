from typing import Optional
from pydantic import BaseModel
from dataclasses_json import dataclass_json
from dataclasses import dataclass


from .Common import Response, Data
from cores.const.api import RequestConst


class LoginModel(BaseModel):

    @dataclass_json
    @dataclass
    class RequestData:
        deviceId: Optional[str] = str()
        username: Optional[str] = str()
        password: Optional[str] = str()

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    request_data: dict = dict()
    header: dict = Data.header
    token: str = Data.token


class PreLoginModel(BaseModel):

    @dataclass_json
    @dataclass
    class RequestData:
        deviceId: Optional[str] = str()
        clientId: Optional[str] = str()

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        payload: dict = dict(access_token=str(), expiresIn=int())

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    token: str = Data.token
    request_data: dict = dict()
