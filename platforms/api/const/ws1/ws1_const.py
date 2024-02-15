from cores.const.__const import Const
from cores.const.common import EnvironmentConst

import os


class WOneConst(Const):
    __env = os.getenv('env')
    if not __env:
        __env = EnvironmentConst.Environment.SIT_ENV
    if __env == EnvironmentConst.Environment.SIT_ENV:
        PRODUCT_VERSION_ID = None if not os.getenv(
            'SIT_PRODUCT_VERSION_ID') else os.getenv('SIT_PRODUCT_VERSION_ID')  # get SIT_PRODUCT_VERSION_ID from local .env file - sentitive data
        TARGET_ACCOUNT_ID = None if not os.getenv(
            'SIT_TARGET_ACCOUNT_ID') else os.getenv('SIT_TARGET_ACCOUNT_ID')  # get SIT_TARGET_ACCOUNT_ID from local .env file - sentitive data
    elif __env == EnvironmentConst.Environment.UAT_ENV:
        PRODUCT_VERSION_ID = None if not os.getenv(
            'UAT_PRODUCT_VERSION_ID') else os.getenv('UAT_PRODUCT_VERSION_ID')  # get UAT_PRODUCT_VERSION_ID from local .env file - sentitive data
        TARGET_ACCOUNT_ID = None if not os.getenv(
            'UAT_TARGET_ACCOUNT_ID') else os.getenv('UAT_TARGET_ACCOUNT_ID')  # get UAT_TARGET_ACCOUNT_ID from local .env file - sentitive data

    VIKKI_TO_VIKKI: str = 'PMNT_IRCT_BOOK'
    VIKKI_TO_HDB: str = 'PMNT_IRCT_HDBA'
    VIKKI_TO_NAPAS: str = 'PMNT_IRCT_DMCT'
    DOMESTIC_CARD: str = 'PMNT_CCRD_ECOM'
    FOREIGN_CARD: str = 'PMNT_CCRD_XBCP'

    class AccountLimit:
        EKYC_VIKKI_TO_VIKKI_DAILY_LIMIT: float = 100000000
        EKYC_VIKKI_TO_HDBANK_DAILY_LIMIT: float = 100000000
        EKYC_VIKKI_TO_NAPAS_DAILY_LIMIT: float = 100000000
        EKYC_INTERNAL_TRANSFER_DAILY_LIMIT: float = 100000000
        EKYC_VIRTUAL_CARD_CARD_NOT_PRESENT_DAILY_LIMIT: float = 50000000
        EKYC_VIRTUAL_CARD_FX_CARD_NOT_PRESENT_DAILY_LIMIT: float = 0
        EKYC_E_BANKING_DAILY_LIMIT: float = 100000000
        EKYC_CARD_DAILY_LIMIT: float = 50000000
        EKYC_CASA_DAILY_LIMIT: float = 100000000

        EKYC_E_BANKING_MONTHLY_LIMIT: float = 100000000
        EKYC_CARD_MONTHLY_LIMIT: float = 100000000
        EKYC_CASA_MONTHLY_LIMIT: float = 100000000

        VKYC_VIKKI_TO_VIKKI_DAILY_LIMIT: float = 2000000000
        VKYC_VIKKI_TO_HDBANK_DAILY_LIMIT: float = 2000000000
        VKYC_VIKKI_TO_NAPAS_DAILY_LIMIT: float = 2000000000
        VKYC_INTERNAL_TRANSFER_DAILY_LIMIT: float = 2000000000
        VKYC_VIRTUAL_CARD_CARD_NOT_PRESENT_DAILY_LIMIT: float = 200000000
        VKYC_VIRTUAL_CARD_FX_CARD_NOT_PRESENT_DAILY_LIMIT: float = 200000000
        VKYC_E_BANKING_DAILY_LIMIT: float = 2000000000
        VKYC_CARD_DAILY_LIMIT: float = 200000000
        VKYC_CASA_DAILY_LIMIT: float = 2000000000

        VKYC_E_BANKING_MONTHLY_LIMIT: float = -1
        VKYC_CARD_MONTHLY_LIMIT: float = 200000000
        VKYC_CASA_MONTHLY_LIMIT: float = -1

    class SpecStoreKeys:
        class PostingInstruction:
            TRANSACTION_AMOUNT = 'TRANSACTION_AMOUNT'
            AUTH_CLIENT_TRX_ID_LIST = 'AUTH_CLIENT_TRX_ID_LIST'
            AUTH_AMOUNT_LIST = 'AUTH_AMOUNT_LIST'
