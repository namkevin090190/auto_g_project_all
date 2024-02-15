from dataclasses_json import dataclass_json
from dataclasses import dataclass
from pydantic import BaseModel

from .Common import Response, AccountCommon, Data
from cores.const.api import RequestConst
from cores.utils import DataGeneratorUtil


class CBSCustomerModel():
    """CBSCustomer : Core Banking System Customer

    Args:
        BaseModel (_type_): _description_
    """

    @dataclass_json
    @dataclass
    class RequestData(AccountCommon.Info):
        cifNumber: int = int()

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    token: str = Data.token
    request_data: dict = dict()


class CIFModel():

    @dataclass_json
    @dataclass
    class RequestData:
        onboardingId: int = DataGeneratorUtil.random_number_generator(
            length=18)

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    token: str = Data.token
    request_data: dict = dict()


class VikkiModel(BaseModel):

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


class ThirdPartiesModel(BaseModel):
    @dataclass_json
    @dataclass
    class RequestData:
        pass

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    token: str = Data.token
    request_data: dict = dict()
