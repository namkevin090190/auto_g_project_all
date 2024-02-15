from pydantic import BaseModel
from dataclasses_json import dataclass_json
from dataclasses import dataclass, field

from platforms.api.const.common_const import ServerConst
from ..Common import Response, Data
from cores.const.api import RequestConst


class CustomerModel(BaseModel):
    @dataclass_json
    @dataclass
    class identifiers:
        identifier_type: str = 'IDENTIFIER_TYPE_EMAIL'
        identifier: str = str()

    @dataclass_json
    @dataclass
    class customer_details:
        title: str = 'CUSTOMER_TITLE_UNKNOWN'
        first_name: str = str()
        last_name: str = str()
        dob: str = '1980-12-25'
        gender: str = 'CUSTOMER_GENDER_UNKNOWN'
        nationality: str = 'VN'
        email_address: str = str()
        mobile_phone_number: str = str()
        contact_method: str = 'CUSTOMER_CONTACT_METHOD_EMAIL'
        country_of_residence: str = 'VN'
        country_of_taxation: str = 'VN'
        accessibility: str = 'CUSTOMER_ACCESSIBILITY_AUDIO'
        external_customer_id: str = str()

    @dataclass_json
    @dataclass
    class customer:
        status: str = 'CUSTOMER_STATUS_ACTIVE'
        password: str = str()
        additional_details: dict = field(default_factory=dict)
        id: str = str()
        customer_details: dict = field(default_factory=dict)
        identifiers: list = field(default_factory=list)
        

    @dataclass_json
    @dataclass
    class RequestData:
        request_id: str = int()
        customer: dict = field(default_factory=dict)

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    header['x-auth-token'] = ServerConst.X_AUTH_TOKEN
    request_data: dict = dict()
