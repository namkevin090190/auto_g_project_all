from pydantic import BaseModel
from dataclasses_json import dataclass_json
from dataclasses import dataclass, field

from platforms.api.const.common_const import ServerConst
from ..Common import Response, Data
from cores.const.api import RequestConst


class ProductModel(BaseModel):
    @dataclass_json
    @dataclass
    class params:
        name: str
        display_name: str
        description: str
        level: str
        is_optional: bool
        value: str

    @dataclass_json
    @dataclass
    class product_version:
        product_id: str = str()
        display_name: str = 'e2e_product'
        description: str = 'new version'
        summary: str = 'new version'
        code: str = str()
        params: list = field(default_factory=list)

    @dataclass_json
    @dataclass
    class RequestData:
        request_id: str = int()
        migration_strategy: str = 'PRODUCT_VERSION_MIGRATION_STRATEGY_NEW_PRODUCT'
        is_internal: bool = False
        product_version: dict = field(default_factory=dict)

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    header['x-auth-token'] = ServerConst.X_AUTH_TOKEN
    request_data: dict = dict()
