from pydantic import BaseModel
from dataclasses_json import dataclass_json
from dataclasses import dataclass


from .Common import Response, Data
from cores.const.api import RequestConst


class AccountInfoModel(BaseModel):

    @dataclass_json
    @dataclass
    class RequestData:
        cbsAccountNumber: int = int()
        requireRestriction: bool = True
        requireRemainingTransactionLimit: bool = True
        requireBalance: bool = True

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    token: str = Data.token
    request_data: dict = dict()


class AccountBalanceModel(BaseModel):

    @dataclass_json
    @dataclass
    class RequestData:
        pass

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.GET
    header: dict = Data.header
    token: str = Data.token
    request_data: dict = dict()


class AccountModel(BaseModel):

    @dataclass_json
    @dataclass
    class RequestData:
        cif_number: int = int()
        product_type: str = 'CASA'
        viki_account_number: int = int()

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    token: str = Data.token
    request_data: dict = dict()
