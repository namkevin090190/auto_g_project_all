from pydantic import BaseModel
from typing import Optional
from dataclasses_json import dataclass_json
from dataclasses import dataclass


from .Common import Response, Data
from cores.const.api import RequestConst


class InitPaymentModel():

    @dataclass_json
    @dataclass
    class RequestData:
        btcCode: Optional[str] = str()
        deviceId: Optional[str] = str()
        otpMessageFooter: Optional[str] = str()

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    token: str = Data.token
    request_data: dict = dict()


class ConfirmPaymentModel():

    @dataclass_json
    @dataclass
    class RequestData:
        otpValue: Optional[int] = int()
        btcCode: Optional[str] = str()
        amount: Optional[int] = int()
        deviceId: Optional[str] = str()
        paymentType: Optional[str] = str()
        description:  Optional[str] = str()
        otpMessageFooter: Optional[str] = str()
        remitterAccountNumber: Optional[int] = int()
        beneficiaryBankBenId: Optional[int] = int()
        beneficiaryAccountNumber: Optional[int] = int()
        beneficiaryAccountName: Optional[str] = str()

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        payload: dict = dict(access_token=str(), expiresIn=int())

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    token: str = Data.token
    request_data: dict = dict()
