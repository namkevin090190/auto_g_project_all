from pydantic import BaseModel
from dataclasses_json import dataclass_json
from dataclasses import dataclass, field

from platforms.api.const.common_const import ServerConst
from ..Common import Response, Data
from cores.const.api import RequestConst


class PostingInstructionModel(BaseModel):
    @dataclass_json
    @dataclass
    class transaction_code:
        domain: str = str()
        family: str = str()
        subfamily: str = str()

    @dataclass_json
    @dataclass
    class instruction_details:
        transaction_code: str = str()

    @dataclass_json
    @dataclass
    class target_account:
        account_id: str = str()

    @dataclass_json
    @dataclass
    class hard_settlement:
        amount: str = str()
        denomination: str = str()
        target_account: dict = field(default_factory=dict)
        internal_account_id: str = "1"
        advice: bool = False

    @dataclass_json
    @dataclass
    class posting_instruction_batch:
        client_id: str = 'AsyncCreatePostingInstructionBatch'
        client_batch_id: str = str()
        value_timestamp: str = str()
        posting_instructions: list = field(default_factory=list)

    @dataclass_json
    @dataclass
    class RequestData:
        request_id: str = int()
        posting_instruction_batch: dict = field(default_factory=dict)

    @dataclass_json
    @dataclass
    class ResponseData(Response):
        pass

    method: str = RequestConst.Method.POST
    header: dict = Data.header
    header['x-auth-token'] = ServerConst.X_AUTH_TOKEN
    request_data: dict = dict()


class InboundHardSettlementModel(BaseModel):
    @dataclass_json
    @dataclass
    class posting_instructions:
        client_transaction_id: str = str()
        inbound_hard_settlement: dict = field(default_factory=dict)
        instruction_details: dict = field(default_factory=dict)
        transaction_code: dict = field(default_factory=dict)


class OutboundHardSettlementModel(BaseModel):
    @dataclass_json
    @dataclass
    class posting_instructions:
        client_transaction_id: str = str()
        outbound_hard_settlement: dict = field(default_factory=dict)
        instruction_details: dict = field(default_factory=dict)
        transaction_code: dict = field(default_factory=dict)


class OutboundAuthorisationModel(BaseModel):
    @dataclass_json
    @dataclass
    class posting_instructions:
        client_transaction_id: str = str()
        outbound_authorisation: dict = field(default_factory=dict)
        instruction_details: dict = field(default_factory=dict)
        transaction_code: dict = field(default_factory=dict)


class SettlementModel(BaseModel):
    @dataclass_json
    @dataclass
    class posting_instructions:
        id: str = ''
        client_transaction_id: str = str()
        settlement: dict = field(default_factory=dict)
        instruction_details: dict = field(default_factory=dict)
        transaction_code: dict = field(default_factory=dict)

    @dataclass_json
    @dataclass
    class settlement:
        amount: str = str()
        final: bool = True
        denomination: str = ''
        target_account: dict = field(default_factory=dict)
        internal_account_id: str = ""
        advice: bool = False
        require_pre_posting_hook_execution: bool = True

    @dataclass_json
    @dataclass
    class posting_instruction_batch:
        id: str = ''
        create_request_id: str = ''
        client_id: str = 'AsyncCreatePostingInstructionBatch'
        client_batch_id: str = str()
        value_timestamp: str = str()
        posting_instructions: list = field(default_factory=list)
        batch_details: dict = field(default_factory=dict)
        dry_run: bool = False


class ReleaseModel(BaseModel):
    @dataclass_json
    @dataclass
    class posting_instructions:
        id: str = ''
        client_transaction_id: str = str()
        release: dict = field(default_factory=dict)
        instruction_details: dict = field(default_factory=dict)

    @dataclass_json
    @dataclass
    class posting_instruction_batch:
        id: str = ''
        create_request_id: str = ''
        client_id: str = 'AsyncCreatePostingInstructionBatch'
        client_batch_id: str = str()
        value_timestamp: str = str()
        posting_instructions: list = field(default_factory=list)
        batch_details: dict = field(default_factory=dict)
        dry_run: bool = False


class TransferModel(BaseModel):
    @dataclass_json
    @dataclass
    class posting_instructions:
        client_transaction_id: str = str()
        transfer: dict = field(default_factory=dict)
        instruction_details: dict = field(default_factory=dict)
        transaction_code: dict = field(default_factory=dict)

    @dataclass_json
    @dataclass
    class transfer:
        amount: str = str()
        denomination: str = str()
        creditor_target_account: dict = field(default_factory=dict)
        debtor_target_account: dict = field(default_factory=dict)
