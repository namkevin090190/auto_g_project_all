import json
from platforms.api.const.services_const import ServiceOutput
from platforms.api.const.ws1.ws1_const import WOneConst
from platforms.api.services.ws1_core_tm.casa import CasaServices
from platforms import step

from cores.utils import StoreUtil, DataGeneratorUtil, GetUtil, AssertUtil, logger
from cores.model import ResponseObj

from datetime import datetime

import uuid


def __get_casa_rsp(account_id: str, pause_time: str = None) -> ResponseObj:
    account_id = GetUtil.spec_get(ServiceOutput.Casa.CREATE_CASA_RESPONSE).get(
        'id') if account_id == 'current_account_id' else WOneConst.TARGET_ACCOUNT_ID if account_id == 'default_account_id' else account_id
    result: ResponseObj = CasaServices().get_casa(
        account_id=account_id, pause_time=pause_time)
    return result


def __get_new_limit(is_ekyc: str, is_daily_limit: str, trx_code: str, account_id: str,  pause_time: str = None) -> float:
    account_id = GetUtil.spec_get(ServiceOutput.Casa.CREATE_CASA_RESPONSE).get(
        'id') if account_id == 'current_account_id' else account_id
    result: ResponseObj = __get_casa_rsp(
        account_id=account_id, pause_time=pause_time)
    derived_instance_param_vals: dict = result.get(
        'derived_instance_param_vals')
    account_limit: str = str(derived_instance_param_vals.get(
        'remaining_debit_daily_limit')) if is_daily_limit == 'daily' else str(derived_instance_param_vals.get('remaining_debit_monthly_limit'))
    expectation: float = float(json.loads(account_limit).get(
        'SOFT_OTP').get(is_ekyc).get(trx_code))
    return expectation


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


def daily_ekyc_limit(trx_code) -> str:
    limit: str = ''
    if trx_code == 'VIKKI_TO_VIKKI':
        limit = WOneConst.AccountLimit.EKYC_VIKKI_TO_VIKKI_DAILY_LIMIT
    elif trx_code == 'VIKKI_TO_HDBANK':
        limit = WOneConst.AccountLimit.EKYC_VIKKI_TO_HDBANK_DAILY_LIMIT
    elif trx_code == 'VIKKI_TO_NAPAS':
        limit = WOneConst.AccountLimit.EKYC_VIKKI_TO_NAPAS_DAILY_LIMIT
    elif trx_code == 'INTERNAL_TRANSFER':
        limit = WOneConst.AccountLimit.EKYC_INTERNAL_TRANSFER_DAILY_LIMIT
    elif trx_code == 'VIRTUAL_CARD_CARD_NOT_PRESENT':
        limit = WOneConst.AccountLimit.EKYC_VIRTUAL_CARD_CARD_NOT_PRESENT_DAILY_LIMIT
    elif trx_code == 'VIRTUAL_CARD_FX_CARD_NOT_PRESENT':
        limit = WOneConst.AccountLimit.EKYC_VIRTUAL_CARD_FX_CARD_NOT_PRESENT_DAILY_LIMIT
    elif trx_code == 'E_BANKING':
        limit = WOneConst.AccountLimit.EKYC_E_BANKING_DAILY_LIMIT
    elif trx_code == 'CARD':
        limit = WOneConst.AccountLimit.EKYC_CARD_DAILY_LIMIT
    elif trx_code == 'CASA':
        limit = WOneConst.AccountLimit.EKYC_CASA_DAILY_LIMIT
    return limit


def monthly_ekyc_limit(trx_code) -> str:
    limit: str = ''
    if trx_code == 'E_BANKING':
        limit = WOneConst.AccountLimit.EKYC_E_BANKING_MONTHLY_LIMIT
    elif trx_code == 'CARD':
        limit = WOneConst.AccountLimit.EKYC_CARD_MONTHLY_LIMIT
    elif trx_code == 'CASA':
        limit = WOneConst.AccountLimit.EKYC_CASA_MONTHLY_LIMIT
    return limit


def daily_vkyc_limit(trx_code) -> str:
    limit: str = ''
    if trx_code == 'VIKKI_TO_VIKKI':
        limit = WOneConst.AccountLimit.VKYC_VIKKI_TO_VIKKI_DAILY_LIMIT
    elif trx_code == 'VIKKI_TO_HDBANK':
        limit = WOneConst.AccountLimit.VKYC_VIKKI_TO_HDBANK_DAILY_LIMIT
    elif trx_code == 'VIKKI_TO_NAPAS':
        limit = WOneConst.AccountLimit.VKYC_VIKKI_TO_NAPAS_DAILY_LIMIT
    elif trx_code == 'INTERNAL_TRANSFER':
        limit = WOneConst.AccountLimit.VKYC_INTERNAL_TRANSFER_DAILY_LIMIT
    elif trx_code == 'VIRTUAL_CARD_CARD_NOT_PRESENT':
        limit = WOneConst.AccountLimit.VKYC_VIRTUAL_CARD_CARD_NOT_PRESENT_DAILY_LIMIT
    elif trx_code == 'VIRTUAL_CARD_FX_CARD_NOT_PRESENT':
        limit = WOneConst.AccountLimit.VKYC_VIRTUAL_CARD_FX_CARD_NOT_PRESENT_DAILY_LIMIT
    elif trx_code == 'E_BANKING':
        limit = WOneConst.AccountLimit.VKYC_E_BANKING_DAILY_LIMIT
    elif trx_code == 'CARD':
        limit = WOneConst.AccountLimit.VKYC_CARD_DAILY_LIMIT
    elif trx_code == 'CASA':
        limit = WOneConst.AccountLimit.VKYC_CASA_DAILY_LIMIT
    return limit


def monthly_vkyc_limit(trx_code) -> str:
    limit: str = ''
    if trx_code == 'E_BANKING':
        limit = WOneConst.AccountLimit.VKYC_E_BANKING_MONTHLY_LIMIT
    elif trx_code == 'CARD':
        limit = WOneConst.AccountLimit.VKYC_CARD_MONTHLY_LIMIT
    elif trx_code == 'CASA':
        limit = WOneConst.AccountLimit.VKYC_CASA_MONTHLY_LIMIT
    return limit


@step('[API][CASA] Create CASA account - opening at <opening_time_stamp|current_time_stamp> with product version id <product_version_id|current_product_version_id|official_product_version_id>')
def create_casa_account(opening_time_stamp: str, product_version_id: str):
    opening_time_stamp = f'{datetime.utcnow().replace(microsecond=0).isoformat()}Z' if opening_time_stamp == 'current_time_stamp' else opening_time_stamp
    product_version_id = WOneConst.PRODUCT_VERSION_ID if product_version_id == 'official_product_version_id' else GetUtil.spec_get(
        ServiceOutput.Product.CREATE_PRODUCT_RESPONSE).get('id') if product_version_id == 'current_product_version_id' else product_version_id
    result: ResponseObj = CasaServices().create_casa(
        request_id=f'e2e_{str(uuid.uuid4())}', product_version_id=product_version_id, opening_timestamp=opening_time_stamp, stakeholder_ids=[GetUtil.spec_get(ServiceOutput.Customer.CREATE_CUSTOMER_RESPONSE).get('id')], id=f'e2e_{DataGeneratorUtil().random_number_generator(length=7)}')
    StoreUtil.spec_store(
        ServiceOutput.Casa.CREATE_CASA_RESPONSE, result)


@step(['[API][CASA] Get CASA account with id <account_id|current_account_id>', '[API][CASA] Get CASA account with id <account_id|current_account_id> with pause time <pause_time>'])
def get_casa_account(account_id: str, pause_time: str = None):
    StoreUtil.spec_store(
        ServiceOutput.Casa.GET_CASA_RESPONSE, __get_casa_rsp(
            account_id=account_id, pause_time=pause_time))


def __get_current_amount_limit(is_daily_limit: str, is_ekyc: str, trx_code: str) -> float:
    current_derived_instance_param_vals: dict = GetUtil.spec_get(
        ServiceOutput.Casa.GET_CASA_RESPONSE).get(
        'derived_instance_param_vals')
    current__account_limit: str = str(current_derived_instance_param_vals.get(
        'remaining_debit_daily_limit')) if is_daily_limit == 'daily' else str(current_derived_instance_param_vals.get('remaining_debit_monthly_limit'))
    current_amount: float = json.loads(current__account_limit).get(
        'SOFT_OTP').get(is_ekyc).get(trx_code)
    return current_amount


@step(['[API][CASA] Verify account <EKYC|VKYC> - <daily|monthly> limit - <trx_code> of CASA account with id <account_id|current_account_id> should be correct after making transaction - <success|fail>', '[API][CASA] Verify account <EKYC|VKYC> - <daily|monthly> limit - <trx_code> of CASA account with id <account_id|current_account_id> should be correct after making transaction - <success|fail> with pause time <pause_time>'])
def verify_casa_account_equal(is_ekyc: str, is_daily_limit: str, trx_code: str, account_id: str, is_trx_success: str, pause_time: str = None):
    expectation: float = __get_new_limit(is_ekyc=is_ekyc, is_daily_limit=is_daily_limit, trx_code=trx_code,
                                         account_id=account_id,  pause_time=pause_time)

    # calculate amount
    before_trx_amount: str = __get_current_amount_limit(
        is_daily_limit=is_daily_limit, is_ekyc=is_ekyc, trx_code=trx_code)
    trx_amount: str = GetUtil.spec_get(
        WOneConst.SpecStoreKeys.PostingInstruction.TRANSACTION_AMOUNT)

    actual: float = float(before_trx_amount)-float(
        trx_amount) if is_trx_success == 'success' else float(before_trx_amount)
    # Business rule:
    # https://galaxyfinx.atlassian.net/wiki/spaces/DCT/pages/134709712/Current+Account+Template+Parameters#debit_monthly_limit
    # https://hdbank.atlassian.net/browse/VWCBT-791
    actual = float(-1) if ((is_ekyc == 'VKYC' and is_daily_limit == 'monthly' and trx_code in ('E_BANKING', 'CASA')) or (is_ekyc == 'VKYC' and is_daily_limit ==
                                                                                                                         'daily' and trx_code in ('INTERNAL_TRANSFER'))) else max(0, actual)
    # --------
    AssertUtil.equal(expectation, actual,
                     f'Limit amount incorrect\n\tExpectation: {expectation}\n\tActual: {actual}')


@step(['[API][CASA] Verify account <EKYC|VKYC> - <daily|monthly> limit - <trx_code> of CASA account with id <account_id|current_account_id> should be full limit', '[API][CASA] Verify account <EKYC|VKYC> - <daily|monthly> limit - <trx_code> of CASA account with id <account_id|current_account_id> should be full limit with pause time <pause_time>'])
def verify_casa_account_reset(is_ekyc: str, is_daily_limit: str, trx_code: str, account_id: str, pause_time: str = None):
    expectation: float = __get_new_limit(is_ekyc=is_ekyc, is_daily_limit=is_daily_limit, trx_code=trx_code,
                                         account_id=account_id,  pause_time=pause_time)

    # reset
    actual: float = 0
    if is_daily_limit == 'daily':
        actual = daily_ekyc_limit(
            trx_code) if is_ekyc == 'EKYC' else daily_vkyc_limit(trx_code)
    else:
        actual = monthly_ekyc_limit(
            trx_code) if is_ekyc == 'EKYC' else monthly_vkyc_limit(trx_code)

    AssertUtil.equal(expectation, actual,
                     f'Limit amount incorrect\n\tExpectation: {expectation}\n\tActual: {actual}')


@step(['[API][CASA] Verify account EKYC - <daily|monthly> limit - <trx_code> of CASA account with id <account_id|current_account_id> should be correct after upgrading to VKYC', '[API][CASA] Verify account EKYC - <daily|monthly> limit - <trx_code> of CASA account with id <account_id|current_account_id> should be correct as <amount> after upgrading to VKYC'])
def verify_casa_account_after_upgrading_ekyc_vkyc(is_daily_limit: str, trx_code: str, account_id: str, amount: str = None):
    # After upgrading - vkyc
    expectation: float = __get_new_limit(
        is_ekyc='VKYC', is_daily_limit=is_daily_limit, trx_code=trx_code, account_id=account_id)

    # Before upgrading - ekyc
    before_upgrade_amount: float = __get_current_amount_limit(
        is_daily_limit=is_daily_limit, is_ekyc='EKYC', trx_code=trx_code)

    diff: float = float(daily_vkyc_limit(trx_code=trx_code))-float(daily_ekyc_limit(
        trx_code=trx_code)) if is_daily_limit == 'daily' else float(monthly_vkyc_limit(trx_code=trx_code)) - float(monthly_ekyc_limit(trx_code=trx_code))

    # Business rule:
    # https://galaxyfinx.atlassian.net/wiki/spaces/DCT/pages/134709712/Current+Account+Template+Parameters#debit_monthly_limit
    # https://hdbank.atlassian.net/browse/VWCBT-791
    actual = float(-1) if ((is_daily_limit == 'monthly' and trx_code in ('E_BANKING', 'CASA')) or (is_daily_limit ==
                                                                                                   'daily' and trx_code in ('INTERNAL_TRANSFER'))) else float(amount) if amount != None else max(0, float(before_upgrade_amount)+diff)
    # --------
    AssertUtil.equal(expectation, actual,
                     f'Limit amount incorrect\n\tExpectation: {expectation}\n\tActual: {actual}')


@step(['[API][CASA] Verify account <EKYC|VKYC> - <daily|monthly> limit - <trx_code> of CASA account with id <account_id|current_account_id> should be correct after making release - <success|fail> - client transaction id order <order_num|latest_num>', '[API][CASA] Verify account <EKYC|VKYC> - <daily|monthly> limit - <trx_code> of CASA account with id <account_id|current_account_id> should be correct after making release - <success|fail> - client transaction id order <order_num|latest_num> with pause time <pause_time>'])
def verify_casa_account_equal(is_ekyc: str, is_daily_limit: str, trx_code: str, account_id: str, is_trx_success: str, client_trx_id_order: str = '1', pause_time: str = None):
    expectation: float = __get_new_limit(
        is_ekyc=is_ekyc, is_daily_limit=is_daily_limit, trx_code=trx_code, account_id=account_id, pause_time=pause_time)

    # calculate amount
    before_trx_amount: float = __get_current_amount_limit(
        is_daily_limit=is_daily_limit, is_ekyc=is_ekyc, trx_code=trx_code)

    trx_amount: str = __handle_auth_amount(
        client_trx_id_order=client_trx_id_order)

    actual = float(before_trx_amount)+float(
        trx_amount) if is_trx_success == 'success' else float(before_trx_amount)
    # Business rule:
    # https://galaxyfinx.atlassian.net/wiki/spaces/DCT/pages/134709712/Current+Account+Template+Parameters#debit_monthly_limit
    # https://hdbank.atlassian.net/browse/VWCBT-791
    actual = float(-1) if ((is_ekyc == 'VKYC' and is_daily_limit == 'monthly' and trx_code in ('E_BANKING', 'CASA')) or (is_ekyc == 'VKYC' and is_daily_limit ==
                                                                                                                         'daily' and trx_code in ('INTERNAL_TRANSFER'))) else max(0, actual)
    # --------
    AssertUtil.equal(expectation, actual,
                     f'Limit amount incorrect\n\tExpectation: {expectation}\n\tActual: {actual}')
