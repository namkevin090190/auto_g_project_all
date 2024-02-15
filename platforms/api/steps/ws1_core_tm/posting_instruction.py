from platforms.api.const.services_const import ServiceOutput
from platforms.api.const.ws1.ws1_const import WOneConst
from platforms import step
from platforms.api.services.ws1_core_tm.posting_instruction import PostingInstructionServices

from cores.utils import StoreUtil, GetUtil, AssertUtil, logger
from cores.model import ResponseObj

import uuid
from datetime import datetime


def __get_client_trx_id_from_auth(client_trx_id_order) -> str:
    client_trx_id_list: list = GetUtil.spec_get(
        WOneConst.SpecStoreKeys.PostingInstruction.AUTH_CLIENT_TRX_ID_LIST)
    client_trx_id: str = ''
    try:
        client_trx_id = '' if client_trx_id_list == [] else client_trx_id_list[
            int(client_trx_id_order)-1] if client_trx_id_order != 'latest_num' else client_trx_id_list[-1]
    except IndexError as error:
        logger.error('client_trx_id error')
        logger.error(error)
    return client_trx_id


@step('[API][PostingInstruction] Inbound Hard Settlement at time stamp <current_time_stamp|value_timestamp> with data - amount <amount> - account id <account_id|current_account_id> - transaction code <transaction_code>')
def inbound_hard_settlement(value_timestamp: str, amount: str, account_id: str, instruction_details_trx_code: str):
    account_id = GetUtil.spec_get(ServiceOutput.Casa.CREATE_CASA_RESPONSE).get(
        'id') if account_id == 'current_account_id' else account_id
    value_timestamp = f'{datetime.utcnow().replace(microsecond=0).isoformat()}Z' if value_timestamp == 'current_time_stamp' else value_timestamp

    result: ResponseObj = PostingInstructionServices().inbound_hard_settlement(
        request_id=f'e2e_{str(uuid.uuid4())}', client_batch_id=f'e2e_{str(uuid.uuid4())}', value_timestamp=value_timestamp, client_transaction_id=f'e2e_{str(uuid.uuid4())}', amount=amount, account_id=account_id, instruction_details_trx_code=instruction_details_trx_code)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.INBOUND_HARD_SETTLEMENT_RESPONSE, result)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.LATEST_TRANSFER_RESPONSE, result)
    StoreUtil.spec_store(
        WOneConst.SpecStoreKeys.PostingInstruction.TRANSACTION_AMOUNT, amount)


@step('[API][PostingInstruction] Outbound Hard Settlement at time stamp <current_time_stamp|value_timestamp> with data - amount <amount> - account id <account_id|current_account_id> - transaction code <transaction_code>')
def outbound_hard_settlement(value_timestamp: str, amount: str, account_id: str, instruction_details_trx_code: str):
    account_id = GetUtil.spec_get(ServiceOutput.Casa.CREATE_CASA_RESPONSE).get(
        'id') if account_id == 'current_account_id' else account_id
    value_timestamp = f'{datetime.utcnow().replace(microsecond=0).isoformat()}Z' if value_timestamp == 'current_time_stamp' else value_timestamp

    result: ResponseObj = PostingInstructionServices().outbound_hard_settlement(
        request_id=f'e2e_{str(uuid.uuid4())}', client_batch_id=f'e2e_{str(uuid.uuid4())}', value_timestamp=value_timestamp, client_transaction_id=f'e2e_{str(uuid.uuid4())}', amount=amount, account_id=account_id, instruction_details_trx_code=instruction_details_trx_code)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.OUTBOUND_HARD_SETTLEMENT_RESPONSE, result)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.LATEST_TRANSFER_RESPONSE, result)
    StoreUtil.spec_store(
        WOneConst.SpecStoreKeys.PostingInstruction.TRANSACTION_AMOUNT, amount)


@step('[API][PostingInstruction] Transfer at time stamp <current_time_stamp|value_timestamp> with data - amount <amount> - from account id <account_id|current_account_id|default_account_id> - to account id <account_id|default_account_id|current_account_id> - transaction code <transaction_code>')
def e_banking(value_timestamp: str, amount: str, debtor_target_account: str, creator_account_id: str, instruction_details_trx_code: str):
    debtor_account_id = GetUtil.spec_get(ServiceOutput.Casa.CREATE_CASA_RESPONSE).get(
        'id') if debtor_target_account == 'current_account_id' else WOneConst.TARGET_ACCOUNT_ID if debtor_target_account == 'default_account_id' else debtor_target_account
    creator_account_id = GetUtil.spec_get(ServiceOutput.Casa.CREATE_CASA_RESPONSE).get(
        'id') if creator_account_id == 'current_account_id' else WOneConst.TARGET_ACCOUNT_ID if creator_account_id == 'default_account_id' else creator_account_id

    value_timestamp = f'{datetime.utcnow().replace(microsecond=0).isoformat()}Z' if value_timestamp == 'current_time_stamp' else value_timestamp

    result: ResponseObj = PostingInstructionServices().transfer(
        request_id=f'e2e_{str(uuid.uuid4())}', client_batch_id=f'e2e_{str(uuid.uuid4())}', value_timestamp=value_timestamp, client_transaction_id=f'e2e_{str(uuid.uuid4())}', amount=amount, creator_account_id=creator_account_id, debtor_account_id=debtor_account_id, instruction_details_trx_code=instruction_details_trx_code)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.TRANSFER_RESPONSE, result)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.LATEST_TRANSFER_RESPONSE, result)
    StoreUtil.spec_store(
        WOneConst.SpecStoreKeys.PostingInstruction.TRANSACTION_AMOUNT, amount)


@step('[API][PostingInstruction] Authorisation at time stamp <current_time_stamp|value_timestamp> with data - amount <amount> - account id <account_id|current_account_id> - transaction code <transaction_code>')
def authorisation(value_timestamp: str, amount: str, account_id: str, instruction_details_trx_code: str):
    account_id = GetUtil.spec_get(ServiceOutput.Casa.CREATE_CASA_RESPONSE).get(
        'id') if account_id == 'current_account_id' else account_id
    value_timestamp = f'{datetime.utcnow().replace(microsecond=0).isoformat()}Z' if value_timestamp == 'current_time_stamp' else value_timestamp

    client_trx_id: str = f'e2e_{str(uuid.uuid4())}'
    client_trx_id_list: list = GetUtil.spec_get(
        WOneConst.SpecStoreKeys.PostingInstruction.AUTH_CLIENT_TRX_ID_LIST)
    client_trx_id_list = [
        client_trx_id] if client_trx_id_list in ([], None) else client_trx_id_list.append(client_trx_id)

    auth_amount_list: list = GetUtil.spec_get(
        WOneConst.SpecStoreKeys.PostingInstruction.AUTH_AMOUNT_LIST)
    auth_amount_list = [
        amount] if auth_amount_list in ([], None) else auth_amount_list.append(amount)

    result: ResponseObj = PostingInstructionServices().authorisation(
        request_id=f'e2e_{str(uuid.uuid4())}', client_batch_id=f'e2e_{str(uuid.uuid4())}', value_timestamp=value_timestamp, client_transaction_id=client_trx_id, amount=amount, account_id=account_id, instruction_details_trx_code=instruction_details_trx_code)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.AUTH_RESPONSE, result)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.LATEST_TRANSFER_RESPONSE, result)
    StoreUtil.spec_store(
        WOneConst.SpecStoreKeys.PostingInstruction.TRANSACTION_AMOUNT, amount)
    StoreUtil.spec_store(
        WOneConst.SpecStoreKeys.PostingInstruction.AUTH_CLIENT_TRX_ID_LIST, client_trx_id_list)
    StoreUtil.spec_store(
        WOneConst.SpecStoreKeys.PostingInstruction.AUTH_AMOUNT_LIST, auth_amount_list)


@step('[API][PostingInstruction] Settlement at time stamp <current_time_stamp|value_timestamp> with data - amount <amount> - account id <account_id|current_account_id> - transaction code <transaction_code> - client transaction id order <order_num|latest_num>')
def settlement(value_timestamp: str, amount: str, account_id: str, instruction_details_trx_code: str, client_trx_id_order: str = '1'):
    account_id = GetUtil.spec_get(ServiceOutput.Casa.CREATE_CASA_RESPONSE).get(
        'id') if account_id == 'current_account_id' else account_id
    value_timestamp = f'{datetime.utcnow().replace(microsecond=0).isoformat()}Z' if value_timestamp == 'current_time_stamp' else value_timestamp
    # get client_trx_id
    client_trx_id: str = __get_client_trx_id_from_auth(
        client_trx_id_order=client_trx_id_order)

    # get auth_amount to check with settle_amount
    auth_amount_list: list = GetUtil.spec_get(
        WOneConst.SpecStoreKeys.PostingInstruction.AUTH_AMOUNT_LIST)
    auth_amount: str = ''
    try:
        auth_amount: str = '' if auth_amount_list == [] else auth_amount_list[
            int(client_trx_id_order)-1] if client_trx_id_order != 'latest_num' else auth_amount_list[-1]
    except IndexError as error:
        logger.error('auth_amount error')
        logger.error(error)

    trx_amount: object = float(
        amount)-float(auth_amount) if float(amount)-float(auth_amount) != 0 else '0'

    result: ResponseObj = PostingInstructionServices().settlement(
        request_id=f'e2e_{str(uuid.uuid4())}', client_batch_id=client_trx_id, value_timestamp=value_timestamp, client_transaction_id=client_trx_id, amount=amount, account_id=account_id, instruction_details_trx_code=instruction_details_trx_code)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.SETTLE_RESPONSE, result)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.LATEST_TRANSFER_RESPONSE, result)
    StoreUtil.spec_store(
        WOneConst.SpecStoreKeys.PostingInstruction.TRANSACTION_AMOUNT, trx_amount)


@step('[API][PostingInstruction] Release at time stamp <current_time_stamp|value_timestamp> with data - transaction code <transaction_code> - client transaction id order <order_num|latest_num>')
def release(value_timestamp: str, instruction_details_trx_code: str, client_trx_id_order: str = '1'):
    value_timestamp = f'{datetime.utcnow().replace(microsecond=0).isoformat()}Z' if value_timestamp == 'current_time_stamp' else value_timestamp
    # get client_trx_id
    client_trx_id: str = __get_client_trx_id_from_auth(
        client_trx_id_order=client_trx_id_order)

    result: ResponseObj = PostingInstructionServices().release(
        request_id=f'e2e_{str(uuid.uuid4())}', client_batch_id=client_trx_id, value_timestamp=value_timestamp, client_transaction_id=client_trx_id, instruction_details_trx_code=instruction_details_trx_code)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.RELEASE_RESPONSE, result)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.LATEST_TRANSFER_RESPONSE, result)


@step('[API][PostingInstruction] Get list posting of  account id <account_id|current_account_id> in time range <start_time> - <end_time>')
def get_list_posting(account_id: str, start_time: str, end_time: str):
    account_id = GetUtil.spec_get(ServiceOutput.Casa.CREATE_CASA_RESPONSE).get(
        'id') if account_id == 'current_account_id' else account_id
    result: ResponseObj = PostingInstructionServices().get_list_posting(
        account_id=account_id, start_time=start_time, end_time=end_time)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.GET_LIST_POSTING_RESPONSE, result)


@step('[API][PostingInstruction] Get posting from id <posting_id|current_posting_id>')
def get_posting(posting_id: str):
    posting_id = GetUtil.spec_get(ServiceOutput.PostingInstruction.LATEST_TRANSFER_RESPONSE).get(
        'id') if posting_id == 'current_posting_id' else posting_id
    result: ResponseObj = PostingInstructionServices().get_posting(
        posting_id=posting_id)
    StoreUtil.spec_store(
        ServiceOutput.PostingInstruction.GET_POSTING_RESPONSE, result)


@step('[API][PostingInstruction] Verify status of <trans_type_name> posting of account id <account_id|current_account_id> in time range <start_time> - <end_time> should be <expected_status>')
def verify_list_posting_posting_status_correct(trans_type_name: str, account_id: str, start_time: str, end_time: str, expected_status: str):
    get_list_posting(account_id=account_id,
                     start_time=start_time, end_time=end_time)
    result: ResponseObj = GetUtil.spec_get(
        ServiceOutput.PostingInstruction.GET_LIST_POSTING_RESPONSE)

    posting_instruction_batches_list: list = result.get(
        'posting_instruction_batches')
    # trans_type_name should be in CALCULATE DAILY INTEREST, REVERT CALCULATED INTEREST LUMP SUM, PAY INTEREST TO CUSTOMER
    status: list = [posting_instruction_batches.get('status') for posting_instruction_batches in posting_instruction_batches_list if posting_instruction_batches.get(
        'batch_details').get('trans_type_name') == trans_type_name]

    AssertUtil.equal(expected_status, status[0],
                     f'Status of {trans_type_name} posting incorrect\n\tExpectation: {expected_status}\n\tActual: {status}')


@step('[API][PostingInstruction] Verify <trans_type_name> posting of account id <account_id|current_account_id> in time range <start_time> - <end_time> is not displayed')
def verify_list_posting_posting_not_displayed(trans_type_name: str, account_id: str, start_time: str, end_time: str):
    get_list_posting(account_id=account_id,
                     start_time=start_time, end_time=end_time)
    result: ResponseObj = GetUtil.spec_get(
        ServiceOutput.PostingInstruction.GET_LIST_POSTING_RESPONSE)

    posting_instruction_batches_list: list = result.get(
        'posting_instruction_batches')
    # trans_type_name should be in CALCULATE DAILY INTEREST, REVERT CALCULATED INTEREST LUMP SUM, PAY INTEREST TO CUSTOMER
    status: list = [posting_instruction_batches.get('status') for posting_instruction_batches in posting_instruction_batches_list if posting_instruction_batches.get(
        'batch_details').get('trans_type_name') == trans_type_name]

    AssertUtil.true(
        status == [], f'{trans_type_name} posting is displayed unexpectedly')


@step('[API][PostingInstruction] Verify status of posting id <posting_id|current_posting_id> should be <expected_status>')
def verify_posting_id_status_displayed(posting_id: str, expected_status: str):
    get_posting(posting_id=posting_id)
    result: ResponseObj = GetUtil.spec_get(
        ServiceOutput.PostingInstruction.GET_POSTING_RESPONSE)
    status: str = 'None'
    try:
        async_operations_dict: str = result.get('async_operations')
        async_operations_dict_key_posting_id: str = list(
            async_operations_dict.keys())[0]
        status = async_operations_dict.get(
            async_operations_dict_key_posting_id).get('response').get('status')
    except AttributeError as error:
        logger.error(error)

    AssertUtil.equal(expected_status, status,
                     f'Status of posting id incorrect\n\tExpectation: {expected_status}\n\tActual: {status}')


@step('[API][PostingInstruction] Verify Contract Violations - Reason of posting id <posting_id|current_posting_id> should be <expected_reason>')
def verify_posting_id_contract_violations_reason_displayed(posting_id: str, expected_reason: str):
    get_posting(posting_id=posting_id)
    result: ResponseObj = GetUtil.spec_get(
        ServiceOutput.PostingInstruction.GET_POSTING_RESPONSE)
    reason: str = ''
    try:
        async_operations_dict: str = result.get('async_operations')
        async_operations_dict_key_posting_id: str = list(
            async_operations_dict.keys())[0]
        reason = async_operations_dict.get(
            async_operations_dict_key_posting_id).get('response').get('posting_instructions')[0].get('contract_violations')[0].get('reason')
    except AttributeError as error:
        logger.error(error)

    AssertUtil.contain(expected_reason, reason,
                       f'Status of posting id incorrect\n\tExpectation: {expected_reason}\n\tActual: {reason}')


@step('[API][PostingInstruction] Verify Instruction Detail posting id <posting_id|current_posting_id> should match with <transaction_code>')
def verify_posting_id_instruction_details_displayed(posting_id: str, transaction_code: str):
    get_posting(posting_id=posting_id)
    result: ResponseObj = GetUtil.spec_get(
        ServiceOutput.PostingInstruction.GET_POSTING_RESPONSE)
    instruction_details_transaction_code: str = ''
    try:
        async_operations_dict: str = result.get('async_operations')
        async_operations_dict_key_posting_id: str = list(
            async_operations_dict.keys())[0]
        posting_structions: dict = async_operations_dict.get(
            async_operations_dict_key_posting_id).get('response').get('posting_instructions')[0]

        instruction_details_transaction_code = posting_structions.get(
            'instruction_details').get('transaction_code')
    except AttributeError as error:
        logger.error(error)

    AssertUtil.equal(instruction_details_transaction_code, transaction_code,
                     f'Transaction code incorrect\n\tExpectation: {instruction_details_transaction_code}\n\tActual: {transaction_code}')


@step('[API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id <posting_id|current_posting_id> should match with <transaction_code>')
def verify_posting_id_instruction_details_and_transaction_code_displayed(posting_id: str, transaction_code: str):
    expected_domain, expected_family, expected_subfamily = PostingInstructionServices(
    ).parse_trx_code(transaction_code)

    verify_posting_id_instruction_details_displayed(
        posting_id=posting_id, transaction_code=transaction_code)

    result: ResponseObj = GetUtil.spec_get(
        ServiceOutput.PostingInstruction.GET_POSTING_RESPONSE)
    transaction_code_domain: str = ''
    transaction_code_family: str = ''
    transaction_code_subfamily: str = ''
    try:
        async_operations_dict: str = result.get('async_operations')
        async_operations_dict_key_posting_id: str = list(
            async_operations_dict.keys())[0]
        posting_structions: dict = async_operations_dict.get(
            async_operations_dict_key_posting_id).get('response').get('posting_instructions')[0]

        transaction_code_domain = posting_structions.get(
            'transaction_code').get('domain')
        transaction_code_family = posting_structions.get(
            'transaction_code').get('family')
        transaction_code_subfamily = posting_structions.get(
            'transaction_code').get('subfamily')
    except AttributeError as error:
        logger.error(error)

    AssertUtil.equal(expected_domain, transaction_code_domain,
                     f'Domain incorrect\n\tExpectation: {expected_domain}\n\tActual: {transaction_code_domain}')
    AssertUtil.equal(expected_family, transaction_code_family,
                     f'Domain incorrect\n\tExpectation: {expected_family}\n\tActual: {transaction_code_family}')
    AssertUtil.equal(expected_subfamily, transaction_code_subfamily,
                     f'Domain incorrect\n\tExpectation: {expected_subfamily}\n\tActual: {transaction_code_subfamily}')
