from cores.const.api.request import RequestConst
from cores.utils import RequestUtil, PrepareObj, logger
from cores.model import ResponseObj, RequestObj

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.const.ws1.ws1_const import WOneConst
from platforms.api.models.ws1_core_tm.posting_instruction import OutboundAuthorisationModel, PostingInstructionModel, InboundHardSettlementModel, OutboundHardSettlementModel, ReleaseModel, SettlementModel, TransferModel


class PostingInstructionServices:

    def __init__(self):
        self.m_posting_instruction = PostingInstructionModel()
        self.m_inbound_hard_settlement = InboundHardSettlementModel()
        self.m_outbound_hard_settlement = OutboundHardSettlementModel()
        self.m_transfer = TransferModel()
        self.m_authorisation = OutboundAuthorisationModel()
        self.m_settlement = SettlementModel()
        self.m_release = ReleaseModel()

    def __parse_hard_settlement_posting_instruction_batch(self, client_batch_id: str, value_timestamp: str, client_transaction_id: str, inbound: bool, amount: str, account_id: str, instruction_details_trx_code: str, domain: str, family: str, subfamily: str) -> dict:
        transaction_code: dict = self.m_posting_instruction.transaction_code(
            domain=domain, family=family, subfamily=subfamily)
        instruction_details: dict = self.m_posting_instruction.instruction_details(
            transaction_code=instruction_details_trx_code)
        target_account: dict = self.m_posting_instruction.target_account(
            account_id=account_id)
        hard_settlement: dict = self.m_posting_instruction.hard_settlement(
            amount=amount, denomination='VND', target_account=target_account)
        # if inbound == true, set posting_instruction to inbound_hard_settlement else outbound_hard_settlement
        posting_instructions: list = [self.m_inbound_hard_settlement.posting_instructions(
            client_transaction_id=client_transaction_id, inbound_hard_settlement=hard_settlement, instruction_details=instruction_details, transaction_code=transaction_code)] if inbound == True else [self.m_outbound_hard_settlement.posting_instructions(
                client_transaction_id=client_transaction_id, outbound_hard_settlement=hard_settlement, instruction_details=instruction_details, transaction_code=transaction_code)]
        # ------
        return self.m_posting_instruction.posting_instruction_batch(
            client_batch_id=client_batch_id, value_timestamp=value_timestamp, posting_instructions=posting_instructions)

    def __parse_transfer_posting_instruction_batch(self, client_batch_id: str, value_timestamp: str, client_transaction_id: str, amount: str, creator_account_id: str, debtor_account_id: str, instruction_details_trx_code: str, domain: str, family: str, subfamily: str) -> dict:
        transaction_code: dict = self.m_posting_instruction.transaction_code(
            domain=domain, family=family, subfamily=subfamily)
        instruction_details: dict = self.m_posting_instruction.instruction_details(
            transaction_code=instruction_details_trx_code)
        creditor_target_account: dict = self.m_posting_instruction.target_account(
            account_id=creator_account_id)
        debtor_target_account: dict = self.m_posting_instruction.target_account(
            account_id=debtor_account_id)

        transfer: dict = self.m_transfer.transfer(
            amount=amount, denomination='VND', creditor_target_account=creditor_target_account, debtor_target_account=debtor_target_account)

        posting_instructions: list = [self.m_transfer.posting_instructions(
            client_transaction_id=client_transaction_id, transfer=transfer, instruction_details=instruction_details, transaction_code=transaction_code)]
        return self.m_posting_instruction.posting_instruction_batch(
            client_batch_id=client_batch_id, value_timestamp=value_timestamp, posting_instructions=posting_instructions)

    def __parse_authorisation_posting_instruction_batch(self, client_batch_id: str, value_timestamp: str, client_transaction_id: str, amount: str, account_id: str, instruction_details_trx_code: str, domain: str, family: str, subfamily: str) -> dict:
        transaction_code: dict = self.m_posting_instruction.transaction_code(
            domain=domain, family=family, subfamily=subfamily)
        instruction_details: dict = self.m_posting_instruction.instruction_details(
            transaction_code=instruction_details_trx_code)
        target_account: dict = self.m_posting_instruction.target_account(
            account_id=account_id)
        hard_settlement: dict = self.m_posting_instruction.hard_settlement(
            amount=amount, denomination='VND', target_account=target_account)
        posting_instructions: list = [self.m_authorisation.posting_instructions(
            client_transaction_id=client_transaction_id, outbound_authorisation=hard_settlement, instruction_details=instruction_details, transaction_code=transaction_code)]
        return self.m_posting_instruction.posting_instruction_batch(
            client_batch_id=client_batch_id, value_timestamp=value_timestamp, posting_instructions=posting_instructions)

    def __parse_settlement_posting_instruction_batch(self, client_batch_id: str, value_timestamp: str, client_transaction_id: str, amount: str, account_id: str, instruction_details_trx_code: str, domain: str, family: str, subfamily: str) -> dict:
        transaction_code: dict = self.m_posting_instruction.transaction_code(
            domain=domain, family=family, subfamily=subfamily)
        instruction_details: dict = self.m_posting_instruction.instruction_details(
            transaction_code=instruction_details_trx_code)
        target_account: dict = self.m_posting_instruction.target_account(
            account_id=account_id)
        settlement: dict = self.m_settlement.settlement(
            amount=amount, target_account=target_account)
        posting_instructions: list = [self.m_settlement.posting_instructions(
            client_transaction_id=client_transaction_id, settlement=settlement, instruction_details=instruction_details, transaction_code=transaction_code)]
        return self.m_settlement.posting_instruction_batch(
            client_batch_id=client_batch_id, value_timestamp=value_timestamp, posting_instructions=posting_instructions, batch_details={})

    def __parse_release_posting_instruction_batch(self, client_batch_id: str, value_timestamp: str, client_transaction_id: str, instruction_details_trx_code: str) -> dict:
        instruction_details: dict = self.m_posting_instruction.instruction_details(
            transaction_code=instruction_details_trx_code)
        release: dict = {}
        posting_instructions: list = [self.m_release.posting_instructions(
            client_transaction_id=client_transaction_id, release=release, instruction_details=instruction_details)]
        return self.m_release.posting_instruction_batch(
            client_batch_id=client_batch_id, value_timestamp=value_timestamp, posting_instructions=posting_instructions, batch_details={})

    def parse_trx_code(self, instruction_details_trx_code: str) -> tuple:
        domain: str
        family: str
        subfamily: str
        domain = family = subfamily = ''
        match instruction_details_trx_code.replace(' ', '').upper():
            case 'VIKKI_TO_VIKKI,INTERNAL_TRANSFER,E_BANKING,CASA':
                trx_code_list: list = WOneConst.VIKKI_TO_VIKKI.split('_')
                domain, family, subfamily = trx_code_list[0], trx_code_list[1], trx_code_list[2]
            case 'VIKKI_TO_HDBANK,INTERNAL_TRANSFER,E_BANKING,CASA':
                trx_code_list: list = WOneConst.VIKKI_TO_HDB.split('_')
                domain, family, subfamily = trx_code_list[0], trx_code_list[1], trx_code_list[2]
            case 'VIKKI_TO_NAPAS,E_BANKING,CASA':
                trx_code_list: list = WOneConst.VIKKI_TO_NAPAS.split('_')
                domain, family, subfamily = trx_code_list[0], trx_code_list[1], trx_code_list[2]
            case 'VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA':
                trx_code_list: list = WOneConst.DOMESTIC_CARD.split('_')
                domain, family, subfamily = trx_code_list[0], trx_code_list[1], trx_code_list[2]
            case 'VIRTUAL_CARD_FX_CARD_NOT_PRESENT,CARD,CASA':
                trx_code_list: list = WOneConst.FOREIGN_CARD.split('_')
                domain, family, subfamily = trx_code_list[0], trx_code_list[1], trx_code_list[2]
            case _:
                logger.error('Wrong instruction_details_trx_code')
        return domain, family, subfamily

    def inbound_hard_settlement(self, request_id: str, client_batch_id: str, value_timestamp: str, client_transaction_id: str, amount: str, account_id: str, instruction_details_trx_code: str):
        domain: str
        family: str
        subfamily: str
        domain, family, subfamily = self.parse_trx_code(
            instruction_details_trx_code)
        posting_instruction_batch: dict = self.__parse_hard_settlement_posting_instruction_batch(client_batch_id=client_batch_id, value_timestamp=value_timestamp, client_transaction_id=client_transaction_id,
                                                                                                 inbound=True, amount=amount, account_id=account_id, instruction_details_trx_code=instruction_details_trx_code, domain=domain, family=family, subfamily=subfamily)
        self.m_posting_instruction.request_data = self.m_posting_instruction.RequestData(
            request_id=request_id, posting_instruction_batch=posting_instruction_batch).to_dict()
        data: RequestObj = PrepareObj.preparation(
            self.m_posting_instruction)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.CORE_SERVER +
                                             ServicesConst.PostingInstruction.POSTING_INSTRUCTION_ASYNC_CREATE,
                                             data=data, is_convert=False)
        return r

    def outbound_hard_settlement(self, request_id: str, client_batch_id: str, value_timestamp: str, client_transaction_id: str, amount: str, account_id: str, instruction_details_trx_code: str):
        domain: str
        family: str
        subfamily: str
        domain, family, subfamily = self.parse_trx_code(
            instruction_details_trx_code)
        posting_instruction_batch: dict = self.__parse_hard_settlement_posting_instruction_batch(client_batch_id=client_batch_id, value_timestamp=value_timestamp, client_transaction_id=client_transaction_id,
                                                                                                 inbound=False, amount=amount, account_id=account_id, instruction_details_trx_code=instruction_details_trx_code, domain=domain, family=family, subfamily=subfamily)
        self.m_posting_instruction.request_data = self.m_posting_instruction.RequestData(
            request_id=request_id, posting_instruction_batch=posting_instruction_batch).to_dict()
        data: RequestObj = PrepareObj.preparation(
            self.m_posting_instruction)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.CORE_SERVER +
                                             ServicesConst.PostingInstruction.POSTING_INSTRUCTION_ASYNC_CREATE,
                                             data=data, is_convert=False)
        return r

    def transfer(self, request_id: str, client_batch_id: str, value_timestamp: str, client_transaction_id: str, amount: str, creator_account_id: str, debtor_account_id: str, instruction_details_trx_code: str):
        domain: str
        family: str
        subfamily: str
        domain, family, subfamily = self.parse_trx_code(
            instruction_details_trx_code)
        posting_instruction_batch: dict = self.__parse_transfer_posting_instruction_batch(client_batch_id=client_batch_id, value_timestamp=value_timestamp, client_transaction_id=client_transaction_id,
                                                                                          amount=amount, creator_account_id=creator_account_id, debtor_account_id=debtor_account_id, instruction_details_trx_code=instruction_details_trx_code, domain=domain, family=family, subfamily=subfamily)
        self.m_posting_instruction.request_data = self.m_posting_instruction.RequestData(
            request_id=request_id, posting_instruction_batch=posting_instruction_batch).to_dict()
        data: RequestObj = PrepareObj.preparation(self.m_posting_instruction)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.CORE_SERVER +
                                             ServicesConst.PostingInstruction.POSTING_INSTRUCTION_ASYNC_CREATE,
                                             data=data, is_convert=False)
        return r

    def authorisation(self, request_id: str, client_batch_id: str, value_timestamp: str, client_transaction_id: str, amount: str, account_id: str, instruction_details_trx_code: str):
        domain: str
        family: str
        subfamily: str
        domain, family, subfamily = self.parse_trx_code(
            instruction_details_trx_code)
        posting_instruction_batch: dict = self.__parse_authorisation_posting_instruction_batch(client_batch_id=client_batch_id, value_timestamp=value_timestamp, client_transaction_id=client_transaction_id,
                                                                                               amount=amount, account_id=account_id, instruction_details_trx_code=instruction_details_trx_code, domain=domain, family=family, subfamily=subfamily)
        self.m_posting_instruction.request_data = self.m_posting_instruction.RequestData(
            request_id=request_id, posting_instruction_batch=posting_instruction_batch).to_dict()
        data: RequestObj = PrepareObj.preparation(self.m_posting_instruction)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.CORE_SERVER +
                                             ServicesConst.PostingInstruction.POSTING_INSTRUCTION_ASYNC_CREATE,
                                             data=data, is_convert=False)
        return r

    def settlement(self, request_id: str, client_batch_id: str, value_timestamp: str, client_transaction_id: str, amount: str, account_id: str, instruction_details_trx_code: str):
        domain: str
        family: str
        subfamily: str
        domain, family, subfamily = self.parse_trx_code(
            instruction_details_trx_code)
        posting_instruction_batch: dict = self.__parse_settlement_posting_instruction_batch(client_batch_id=client_batch_id, value_timestamp=value_timestamp, client_transaction_id=client_transaction_id,
                                                                                            amount=amount, account_id=account_id, instruction_details_trx_code=instruction_details_trx_code, domain=domain, family=family, subfamily=subfamily)
        self.m_posting_instruction.request_data = self.m_posting_instruction.RequestData(
            request_id=request_id, posting_instruction_batch=posting_instruction_batch).to_dict()
        data: RequestObj = PrepareObj.preparation(self.m_posting_instruction)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.CORE_SERVER +
                                             ServicesConst.PostingInstruction.POSTING_INSTRUCTION_ASYNC_CREATE,
                                             data=data, is_convert=False)
        return r

    def release(self, request_id: str, client_batch_id: str, value_timestamp: str, client_transaction_id: str, instruction_details_trx_code: str):
        posting_instruction_batch: dict = self.__parse_release_posting_instruction_batch(client_batch_id=client_batch_id, value_timestamp=value_timestamp, client_transaction_id=client_transaction_id,
                                                                                         instruction_details_trx_code=instruction_details_trx_code)
        self.m_posting_instruction.request_data = self.m_posting_instruction.RequestData(
            request_id=request_id, posting_instruction_batch=posting_instruction_batch).to_dict()
        data: RequestObj = PrepareObj.preparation(self.m_posting_instruction)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.CORE_SERVER +
                                             ServicesConst.PostingInstruction.POSTING_INSTRUCTION_ASYNC_CREATE,
                                             data=data, is_convert=False)
        return r

    def get_list_posting(self, account_id: str, start_time: str, end_time: str):
        self.m_posting_instruction.request_data = None
        self.m_posting_instruction.method = RequestConst.Method.QUERY
        url = ServerConst.CORE_SERVER + \
            ServicesConst.PostingInstruction.POSTING_INSTRUCTION + \
            f'?page_size=10&order_by_direction=ORDER_BY_DESC&start_time={start_time}&end_time={end_time}&account_ids={account_id}'
        data: RequestObj = PrepareObj.preparation(self.m_posting_instruction)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=url,
                                             data=data, is_convert=False)
        return r

    def get_posting(self, posting_id: str):
        self.m_posting_instruction.request_data = None
        self.m_posting_instruction.method = RequestConst.Method.QUERY
        url = ServerConst.CORE_SERVER + \
            ServicesConst.PostingInstruction.POSTING_INSTRUCTION_ASYNC_OPERATION_BATCH_GET + \
            f'?ids={posting_id}'
        data: RequestObj = PrepareObj.preparation(self.m_posting_instruction)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=url,
                                             data=data, is_convert=False)
        return r
