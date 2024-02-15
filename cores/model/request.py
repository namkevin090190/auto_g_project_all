from pydantic import BaseModel
from typing import AnyStr, Optional


class RequestObj(BaseModel):
    token: Optional[str] = str()
    header: dict = dict()
    method: str = str()
    files: Optional[list] = list()
    request_data: Optional[dict] = dict()


class ResponseObj(RequestObj):
    status_code: int = int()
    status_msg: str = ''
    errors: AnyStr = str()
    # grpc_code: int = int() # not applicable
    # api_version: float = float() # not applicable
    message: AnyStr = str()
    response_data: dict = dict()
    meta_data: dict = dict()
