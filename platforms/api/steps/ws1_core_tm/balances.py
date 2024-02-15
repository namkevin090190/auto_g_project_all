from platforms.api.const.services_const import ServiceOutput
from platforms import step
from platforms.api.const.ws1.ws1_const import WOneConst
from platforms.api.services.ws1_core_tm.balances import BalancesServices

from cores.utils import GetUtil, AssertUtil, StoreUtil, logger
from cores.model import ResponseObj


def __get_balances_rsp(account_id: str, account_address: str = None):
    account_id = GetUtil.spec_get(ServiceOutput.Casa.CREATE_CASA_RESPONSE).get(
        'id') if account_id == 'current_account_id' else WOneConst.TARGET_ACCOUNT_ID if account_id == 'default_account_id' else account_id
    result: ResponseObj = BalancesServices().query_balances(
        account_id=account_id, account_address=account_address)
    return result


def __get_new_balances(account_id: str, account_address: str = None):
    balances_list: list = __get_balances_rsp(
        account_id=account_id, account_address=account_address).get('balances')
    balance_list: list = [balances.get('amount') for balances in balances_list if (balances.get(
        'account_address') == 'DEFAULT' and balances.get(
        'phase') == 'POSTING_PHASE_COMMITTED')]
    balance: float = 0 if balance_list == [] else float(balance_list[0])
    return balance


def __get_current_balances():
    balances_list: list = GetUtil.spec_get(
        ServiceOutput.Balances.GET_LIVE_BALANCES_RESPONSE).get('balances')
    current_balance_list: list = [balances.get('amount') for balances in balances_list if (balances.get(
        'account_address') == 'DEFAULT' and balances.get(
        'phase') == 'POSTING_PHASE_COMMITTED')]
    current_balance: float = 0 if current_balance_list == [
    ] else float(current_balance_list[0])
    print(current_balance)
    return current_balance


def __get_current_interest():
    balances_list: list = GetUtil.spec_get(
        ServiceOutput.Balances.GET_LIVE_BALANCES_RESPONSE).get('balances')
    current_interest_list: list = [balances.get('amount') for balances in balances_list if (balances.get(
        'account_address') == 'ACCRUAL_INTEREST' and balances.get(
        'phase') == 'POSTING_PHASE_COMMITTED')]
    current_interest: float = 0 if current_interest_list == [
    ] else float(current_interest_list[0])
    return current_interest


def __get_interest_from_product():
    product_versions_dict: dict = GetUtil.spec_get(
        ServiceOutput.Product.GET_PRODUCT_INFO_RESPONSE).get('product_versions')
    params_list: list = product_versions_dict[list(
        product_versions_dict.keys())[0]].get('params')
    interest_value_list: list = [params.get('value') for params in params_list if params.get(
        'name') == 'deposit_interest_rate']
    interest_value: float = 0 if interest_value_list == [
    ] else float(interest_value_list[0])
    return interest_value


def __calculate_interest(current_balance: str, current_interest: str, is_eom=False) -> tuple:
    interest_value: float = __get_interest_from_product()  # get interest from product
    daily_interest: float = interest_value/365
    accured_interest: float = round(
        daily_interest * current_balance, 2)+current_interest
    gl_posting: float = int(accured_interest)
    mod_interest: float = round(accured_interest-gl_posting, 2)
    balance: float = current_balance + \
        gl_posting if is_eom == True else current_balance
    return accured_interest, gl_posting, mod_interest, balance


def __handle_trx_amount() -> str:
    trx_amount: str = GetUtil.spec_get(
        WOneConst.SpecStoreKeys.PostingInstruction.TRANSACTION_AMOUNT)
    trx_amount = float(0) if trx_amount == '0' else float(trx_amount)
    return trx_amount


def __handle_auth_amount(client_trx_id_order: str):
    auth_amount_list: list = GetUtil.spec_get(
        WOneConst.SpecStoreKeys.PostingInstruction.AUTH_AMOUNT_LIST)
    auth_amount: str = ''
    try:
        auth_amount: str = '' if auth_amount_list == [] else auth_amount_list[
            int(client_trx_id_order)-1] if client_trx_id_order != 'latest_num' else auth_amount_list[-1]
    except IndexError as error:
        logger.error('auth_amount error')
        logger.error(error)
    return auth_amount


@step(['[API][Balances] Get balances of <account_id|current_account_id>', '[API][Balances] Get balances of <account_id|current_account_id> with account_address <account_address>'])
def get_balances_with_specific_account_address(account_id: str, account_address: str = None):
    result: ResponseObj = __get_balances_rsp(
        account_id=account_id, account_address=account_address)
    StoreUtil.spec_store(
        ServiceOutput.Balances.GET_LIVE_BALANCES_RESPONSE, result)


@step(['[API][Balances][Verify] Accrual Interest balance of <account_id|current_account_id> should be <amount|calculated_amount> at <EOD|EOM>'])
def verify_get_balances_with_interest_account_address_eom(account_id: str, amount: str, is_eom: str):
    result: ResponseObj = __get_balances_rsp(
        account_id=account_id, account_address='ACCRUAL_INTEREST')

    expected: float = round(float(result.get('balances')[0].get('amount')), 2)

    actual: float = 0 if amount == 'calculated_amount' else float(amount)
    if amount == 'calculated_amount':
        accured_interest, _, mod_interest, _ = __calculate_interest(
            current_balance=__get_current_balances(), current_interest=__get_current_interest(), is_eom=False) if is_eom == 'EOD' else __calculate_interest(
            current_balance=__get_current_balances(), current_interest=__get_current_interest(), is_eom=True)
        actual = accured_interest if is_eom == 'EOD' else mod_interest

    AssertUtil.equal(expected, actual,
                     f'Accrual interest amount incorrect\n\tExpectation: {expected}\n\tActual: {actual}')


@step(['[API][Balances][Verify] Default balance of <account_id|current_account_id> should be <amount|calculated_amount> with interest at <EOD|EOM>'])
def verify_get_balances_with_default_account_address_eom_interest(account_id: str, amount: str, is_eom: str = False):
    expected: float = __get_new_balances(
        account_id=account_id, account_address='DEFAULT')

    actual: float = 0 if amount == 'calculated_amount' else float(amount)
    if amount == 'calculated_amount':
        _, _, _, actual = __calculate_interest(
            current_balance=__get_current_balances(), current_interest=__get_current_interest(), is_eom=False) if is_eom == 'EOD' else __calculate_interest(
            current_balance=__get_current_balances(), current_interest=__get_current_interest(), is_eom=True)

    AssertUtil.equal(expected, actual,
                     f'Balance amount incorrect\n\tExpectation: {expected}\n\tActual: {actual}')


@step(['[API][Balances][Verify] Default balance of <account_id|current_account_id> should be <calculated_amount> after making transaction - <success|fail>'])
def verify_get_balances_with_default_account_address_transaction(account_id: str, amount: str, is_trx_success: str = 'success'):
    expected: float = __get_new_balances(
        account_id=account_id, account_address='DEFAULT')

    actual: float = 0 if amount == 'calculated_amount' else float(amount)
    if amount == 'calculated_amount':
        current_balance_before_trx: str = __get_current_balances()

        trx_amount: str = __handle_trx_amount()
        
        actual = float(current_balance_before_trx)-float(
            trx_amount) if is_trx_success == 'success' else float(current_balance_before_trx)

    AssertUtil.equal(expected, actual,
                     f'Balance amount incorrect\n\tExpectation: {expected}\n\tActual: {actual}')


@step(['[API][Balances][Verify] Default balance of <account_id|current_account_id> should be <calculated_amount> after getting credit - <success|fail>'])
def verify_get_balances_with_default_account_address_credit(account_id: str, amount: str, is_trx_success: str = 'success'):
    expected: float = __get_new_balances(
        account_id=account_id, account_address='DEFAULT')

    actual: float = 0 if amount == 'calculated_amount' else float(amount)
    if amount == 'calculated_amount':
        current_balance_before_trx: str = __get_current_balances()

        trx_amount: str = __handle_trx_amount()

        actual = float(current_balance_before_trx)+float(
            trx_amount) if is_trx_success == 'success' else float(current_balance_before_trx)

    AssertUtil.equal(expected, actual,
                     f'Balance amount incorrect\n\tExpectation: {expected}\n\tActual: {actual}')


@step(['[API][Balances][Verify] Default balance of <account_id|current_account_id> should be <calculated_amount> after making settlement - <success|fail> - client transaction id order <order_num|latest_num>'])
def verify_get_balances_with_default_account_address_settlement(account_id: str, amount: str, is_trx_success: str = 'success', client_trx_id_order: str = "1"):
    expected: float = __get_new_balances(
        account_id=account_id, account_address='DEFAULT')

    actual: float = 0 if amount == 'calculated_amount' else float(amount)
    if amount == 'calculated_amount':
        current_balance_before_trx: str = __get_current_balances()

        trx_amount: str = __handle_trx_amount()

        # get auth_amount to check with settle_amount
        auth_amount: str = __handle_auth_amount(
            client_trx_id_order=client_trx_id_order)

        actual = float(current_balance_before_trx)-float(
            trx_amount)-float(auth_amount) if is_trx_success == 'success' else float(current_balance_before_trx)

    AssertUtil.equal(expected, actual,
                     f'Balance amount incorrect\n\tExpectation: {expected}\n\tActual: {actual}')


@step(['[API][Balances][Verify] Default balance of <account_id|current_account_id> should be <calculated_amount> after making settlement with interest - <success|fail> - client transaction id order <order_num|latest_num>'])
def verify_get_balances_with_default_account_address_settlement_with_interest(account_id: str, amount: str, is_trx_success: str = 'success', client_trx_id_order: str = "1"):
    expected: float = __get_new_balances(
        account_id=account_id, account_address='DEFAULT')

    actual: float = 0 if amount == 'calculated_amount' else float(amount)
    if amount == 'calculated_amount':
        current_balance_before_trx: str = '0'
        # calculate interest
        _, _, _, current_balance_before_trx = __calculate_interest(
            current_balance=__get_current_balances(), current_interest=__get_current_interest(), is_eom=True)

        # trx amount
        trx_amount: str = __handle_trx_amount()

        # get auth_amount to check with settle_amount
        auth_amount: str = __handle_auth_amount(
            client_trx_id_order=client_trx_id_order)

        actual = float(current_balance_before_trx)-float(
            trx_amount)-float(auth_amount) if is_trx_success == 'success' else float(current_balance_before_trx)

    AssertUtil.equal(expected, actual,
                     f'Balance amount incorrect\n\tExpectation: {expected}\n\tActual: {actual}')
