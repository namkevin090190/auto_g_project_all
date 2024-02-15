import os
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from pydantic import BaseModel
from datetime import timedelta
from typing import Optional
from cores.const.common.environment_const import EnvironmentConst

from cores.utils import DataGeneratorUtil


class Response(BaseModel):
    class __ResponseStatus:
        code: str = str()
        message: str | bool = str()
        errors: str | bool = str()

    class __ResponseMeta:
        request_id: str
        next_cursor: bool

    status: object = __ResponseStatus()
    meta: object = __ResponseMeta()


class Data:
    token: Optional[str] = str()
    header: dict = {'accept': 'application/json, text/plain, */*',
                    'content-type': 'application/json'}


class AccountCommon(BaseModel):
    class Info:
        firstName: str = str()
        middleName: str = str()
        lastName: str = str()
        nationalIdNumber: int = int()
        dob: str = str()
        gender: str = str()
        nationality: str = 'VN'
        mobilePhoneNumber: str = str()
        city: str = str()
        language: str = str()
        fullName: str = f'{firstName} {middleName} {lastName}'

    class Address:
        addressFull: str = str()
        country: str = str()
        province: str = str()
        district: str = str()
        street: str = str()
        houseNumber: str = str()
        postCode: int = int()

    class NationalID:
        type: str = 'CITIZEN_ID_WITH_CHIP'
        number: int = DataGeneratorUtil().random_number_generator(length=12)
        issueDate: str = DataGeneratorUtil().birth_date_generator(
            min_age=19, max_age=60)
        expireDate: str = DataGeneratorUtil().date_generator(
            start_date=issueDate, end_date=issueDate + timedelta(days=8*365))
        issuePlace: str = "CỤC TRƯỞNG CỤC CẢNH SÁT QUẢN LÝ HÀNH CHÍNH VỀ TRẬT TỰ XÃ HỘI"
        


