import json
from cores.const.api.request import RequestConst
from cores.utils import RequestUtil, PrepareObj, PathUtil, logger
from cores.model import ResponseObj, RequestObj

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models.ws1_core_tm.product import ProductModel

import os


class ProductServices:

    def __init__(self):
        self.m_product = ProductModel()

    def __parse_params(self):
        vkyc_flags: dict = self.m_product.params(
            name='vkyc_flags', display_name='Video KYC flag', description='Flag definition id to be used for Video KYC', level='LEVEL_PRODUCT', is_optional=False, value='VKYC').to_dict()
        minimum_customer_debit_daily_limit: dict = self.m_product.params(
            name='minimum_customer_debit_daily_limit', display_name='Minimum customer debit daily limit', description='The minimum value of customer debit daily limit for each transaction type', level='LEVEL_PRODUCT', is_optional=False, value='{\"EKYC\": {\"VIRTUAL_CARD_CARD_NOT_PRESENT\": \"1000000\", \"VIRTUAL_CARD_FX_CARD_NOT_PRESENT\": \"1000000\", \"VIKKI_TO_NAPAS\": \"50000000\"}, \"VKYC\": {\"VIRTUAL_CARD_CARD_NOT_PRESENT\": \"1000000\", \"VIRTUAL_CARD_FX_CARD_NOT_PRESENT\": \"1000000\", \"VIKKI_TO_NAPAS\": \"50000000\"}}').to_dict()
        credit_transaction_limit: dict = self.m_product.params(
            name='credit_transaction_limit', display_name='Credit transaction limit', description='The limit of credit funding can receive in one transaction', level='LEVEL_PRODUCT', is_optional=False, value='{\"SOFT_OTP\": {\"EKYC\": {}, \"VKYC\": {}}}').to_dict()
        debit_transaction_limit: dict = self.m_product.params(
            name='debit_transaction_limit', display_name='Debit transaction limit', description='The limit of debit funding can make in one transaction', level='LEVEL_PRODUCT', is_optional=False, value='{\"SOFT_OTP\": {\"EKYC\": {\"VIKKI_TO_VIKKI\": \"100000000\", \"VIKKI_TO_HDBANK\": \"100000000\", \"VIKKI_TO_NAPAS\": \"100000000\", \"VIRTUAL_CARD_CARD_NOT_PRESENT\": \"50000000\",\"VIRTUAL_CARD_FX_CARD_NOT_PRESENT\": \"0\"}, \"VKYC\": {\"VIKKI_TO_VIKKI\": \"499999999\", \"VIKKI_TO_HDBANK\": \"499999999\", \"VIKKI_TO_NAPAS\": \"499999999\", \"VIRTUAL_CARD_CARD_NOT_PRESENT\": \"50000000\", \"VIRTUAL_CARD_FX_CARD_NOT_PRESENT\": \"50000000\"}}}').to_dict()
        credit_daily_limit: dict = self.m_product.params(
            name='credit_daily_limit', display_name='Credit daily limit', description='The limit of credit funding can receive in one day', level='LEVEL_PRODUCT', is_optional=False, value='{\"SOFT_OTP\": {\"EKYC\": {}, \"VKYC\": {}}}').to_dict()
        debit_daily_limit: dict = self.m_product.params(
            name='debit_daily_limit', display_name='Debit daily limit', description='The limit of debit funding can make in one day', level='LEVEL_PRODUCT', is_optional=False, value='{\"SOFT_OTP\": {\"EKYC\": {\"VIKKI_TO_VIKKI\": \"100000000\", \"VIKKI_TO_HDBANK\": \"100000000\", \"VIKKI_TO_NAPAS\": \"100000000\",\"INTERNAL_TRANSFER\": \"100000000\", \"VIRTUAL_CARD_CARD_NOT_PRESENT\": \"50000000\",\"VIRTUAL_CARD_FX_CARD_NOT_PRESENT\": \"0\", \"E_BANKING\": \"100000000\", \"CARD\": \"50000000\", \"CASA\": \"100000000\"}, \"VKYC\": {\"VIKKI_TO_VIKKI\": \"2000000000\", \"VIKKI_TO_HDBANK\": \"2000000000\", \"VIKKI_TO_NAPAS\": \"2000000000\", \"INTERNAL_TRANSFER\": \"-1\",\"VIRTUAL_CARD_CARD_NOT_PRESENT\": \"200000000\", \"VIRTUAL_CARD_FX_CARD_NOT_PRESENT\": \"200000000\", \"E_BANKING\": \"2000000000\", \"CARD\": \"200000000\", \"CASA\": \"2000000000\"}}}').to_dict()
        debit_monthly_limit: dict = self.m_product.params(
            name='debit_monthly_limit', display_name='Debit monthly limit', description='The limit of debit funding can make in one month', level='LEVEL_PRODUCT', is_optional=False, value='{\"SOFT_OTP\": {\"EKYC\": {\"E_BANKING\": \"100000000\",\"CARD\": \"100000000\",\"CASA\": \"100000000\"},\"VKYC\": {\"E_BANKING\": \"-1\",\"CARD\": \"200000000\",\"CASA\": \"-1\"}}}').to_dict()
        acquisition_channel: dict = self.m_product.params(
            name='acquisition_channel', display_name='Acquisition channel', description='Acquisition channel that the product belongs to, it is purely for reporting purpose only.', level='LEVEL_PRODUCT', is_optional=False, value='Vikki Mobile App').to_dict()
        deposit_interest_rate: dict = self.m_product.params(
            name='deposit_interest_rate', display_name='Interest rate (p.a.)', description='Receive the annual standard interest rate.', level='LEVEL_PRODUCT', is_optional=False, value='0.005').to_dict()
        denomination: dict = self.m_product.params(
            name='denomination', display_name='Denomination', description='The main currency in which the product operates. The following features will only be available for the main denomination: deposit interest, and other fees. Contract defined limitations will also only apply to postings made in this currency.', level='LEVEL_PRODUCT', is_optional=False, value='VND').to_dict()
        interest_accrual_days_in_year: dict = self.m_product.params(
            name='interest_accrual_days_in_year', display_name='Interest accrual days in year', description='The days in the year for interest accrual calculation. Valid values are \"365\"', level='LEVEL_PRODUCT', is_optional=False, value='365').to_dict()
        accrual_precision: dict = self.m_product.params(
            name='accrual_precision', display_name='Interest accrual precision', description='Precision needed for interest accruals.', level='LEVEL_PRODUCT', is_optional=False, value='2').to_dict()
        fulfilment_precision: dict = self.m_product.params(
            name='fulfilment_precision', display_name='Interest fulfilment precision', description='Precision needed for interest fulfilment.', level='LEVEL_PRODUCT', is_optional=False, value='0').to_dict()
        minimum_balance: dict = self.m_product.params(
            name='minimum_balance', display_name='Minimum balance', description='Minimum balance required to maintain the account.', level='LEVEL_PRODUCT', is_optional=False, value='0').to_dict()
        internal_account_for_interest_accrual: dict = self.m_product.params(
            name='internal_account_for_interest_accrual', display_name='Accrual interest expense', description='This is the GL account for collecting daily accrual interest', level='LEVEL_PRODUCT', is_optional=False, value='480100007.00').to_dict()
        internal_account_for_payable_interest: dict = self.m_product.params(
            name='internal_account_for_payable_interest', display_name='Interest payables to current account', description='This is the GL account for collecting payable interest', level='LEVEL_PRODUCT', is_optional=False, value='249110001.00').to_dict()
        internal_account_for_interest_application: dict = self.m_product.params(
            name='internal_account_for_interest_application', display_name='Interest expense - Current account', description='This is the GL account for collecting apply interest', level='LEVEL_PRODUCT', is_optional=False, value='480100003.00').to_dict()
        return [vkyc_flags, minimum_customer_debit_daily_limit, credit_transaction_limit, debit_transaction_limit, credit_daily_limit, debit_daily_limit, debit_monthly_limit, acquisition_channel, deposit_interest_rate, denomination, interest_accrual_days_in_year, accrual_precision, fulfilment_precision, minimum_balance, internal_account_for_interest_accrual, internal_account_for_payable_interest, internal_account_for_interest_application]

    def __handle_code(self, schedule_tag_id: str):
        code: str = ''
        # Handle code ----------
        # Read text from create_product_code.txt file
        file_path = os.path.join(PathUtil.get_prj_root_path(), 'platforms',
                                 'api', 'const', 'ws1', 'create_product_code.txt')
        with open(file_path, 'r') as file:
            code = file.read()
        # Replace schedule tag id, then replace escape characters. Ex: \r,\n,\",\/ with other characters, then change back.
        replaced_account_schedule_tag_id: str = '{{account_schedule_tag_id}}'
        if replaced_account_schedule_tag_id not in code:
            logger.error(
                f'NOT FOUND {replaced_account_schedule_tag_id} in {file_path} to replace with new tag')
            return ''
        code = code.replace(replaced_account_schedule_tag_id, schedule_tag_id).replace(r'\r\n', '.r.n').replace(
            r'\"', '$').replace(r'\/', '%').replace('.r.n', '\r\n').replace(
            '$', '\"').replace('%', '\/')
        return code

    def create_product(self, request_id: str, product_id: str, schedule_tag_id: str):
        product_version: dict = self.m_product.product_version(
            product_id=product_id, code=self.__handle_code(schedule_tag_id=schedule_tag_id), params=self.__parse_params()).to_dict()
        self.m_product.request_data = self.m_product.RequestData(
            request_id=request_id, product_version=product_version).to_dict()
        data: RequestObj = PrepareObj.preparation(self.m_product)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=ServerConst.CORE_SERVER + ServicesConst.Product.CREATE_PRODUCT,
                                             data=data, is_convert=False)
        return r

    def get_product_info(self, product_version_id: str):
        self.m_product.request_data = None
        self.m_product.method = RequestConst.Method.QUERY
        url = ServerConst.CORE_SERVER + ServicesConst.Product.GET_PRODUCT_INFO + \
            f'?ids={product_version_id}&view=PRODUCT_VERSION_VIEW_INCLUDE_PARAMETERS'
        data: RequestObj = PrepareObj.preparation(self.m_product)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=url,
                                             data=data, is_convert=False)
        return r
