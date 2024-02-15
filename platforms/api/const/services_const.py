from cores.const.__const import Const


class ServicesConst(Const):
    class Authen:
        LOGIN_ENDPOINT = 'api/authentication/v1/auth/login'
        PRE_LOGIN_ENDPOINT = 'api/authentication/v1/auth/pre-login'
        SIGNUP_ENDPOINT = 'api/authentication/v1/internal/auth/signup'

    class Payment:
        INIT_PAYMENT_ENDPOINT = 'payments/intra/payment-orders'
        CONFIRM_PAYMENT_ENDPOINT = 'payments/intra/payment-orders/{payment_id}/confirm'
        CONFIRM_PAYMENT_ENDPOINT = 'payments/intra/payment-orders/{payment_id}/confirm'

    class Account:
        ACCOUNT_DETAIL_ENDPOINT = 'api/account-service/v1/internal/accounts/get-account-detail'
        ACCOUNT_BALANCE_ENDPOINT = 'api/account-service/v1/balance'
        ACCOUNT_CREATE_ENDPOINT = 'api/account-service/v1/internal/accounts'

    class Parties:
        CIF_CREATE_ENDPOINT = 'api/party-service/v2/internal/parties/cif'
        CBS_ACCOUNCT_CREATE_ENDPOINT = 'api/party-service/v2/internal/parties/cbs-customer'
        VIKKI_ACCOUNT_VIEW_ENDPOINT = 'api/party-service/v2/internal/parties/van'
        PARTY_CREATE_ENDPOINT = 'api/party-service/v2/internal/parties'
        ACCOUNT_INFO_ENDPOINT = 'api/party-service/v2/parties/profiles'

    class Card:
        CARD_CREATE_ENDPOINT = 'api/card-service/internal/v1/cards'

    class Customer:
        CREATE_CUSTOMER = 'v1/customers'

    class Casa:
        CREATE_CASA = 'v1/accounts'
        GET_CASA = 'v1/accounts/'

    class SchedulerTag:
        CREATE_SCHEDULER_TAG = 'v1/account-schedule-tags'
        UPDATE_SCHEDULER_TAG = 'v1/account-schedule-tags/'

    class Product:
        CREATE_PRODUCT = 'v1/product-versions'
        GET_PRODUCT_INFO = 'v1/product-versions:batchGet'

    class Flag:
        UPDATE_FLAG = 'v1/flags'

    class PostingInstruction:
        POSTING_INSTRUCTION_ASYNC_CREATE = 'v1/posting-instruction-batches:asyncCreate'
        POSTING_INSTRUCTION = 'v1/posting-instruction-batches'
        POSTING_INSTRUCTION_ASYNC_OPERATION_BATCH_GET = 'v1/posting-instruction-batches/async-operations:batchGet'

    class Balances:
        LIVE = 'v1/balances/live'


class ServiceOutput(Const):
    class Authen:
        LOGIN_RESPONSE = 'LOGIN_RESPONSE'

    class Payment:
        INIT_PAYMENT_RESPONSE = 'INIT_PAYMENT_RESPONSE'
        CONFIRM_PAYMENT_RESPONSE = 'CONFIRM_PAYMENT_RESPONSE'

    class Account:
        ACCOUNT_INFO_RESPONSE = 'ACCOUNT_INFO_RESPONSE'
        ACCOUNT_BALANCE_RESPONSE = 'ACCOUNT_BALANCE_RESPONSE'
        ACCOUNT_CREATE_RESPONSE = 'ACCOUNT_CREATE_RESPONSE'

    class Parties:
        CREATE_CIF_NO_RESPONSE = 'CREATE_CIF_NO_RESPONSE'
        CREATE_CBS_ACC_RESPONSE = 'CREATE_CBS_ACC_RESPONSE'

    class Customer:
        CREATE_CUSTOMER_RESPONSE = 'CREATE_CUSTOMER_RESPONSE'

    class Casa:
        CREATE_CASA_RESPONSE = 'CREATE_CASA_RESPONSE'
        GET_CASA_RESPONSE = 'GET_CASA_RESPONSE'

    class SchedulerTag:
        CREATE_SCHEDULER_TAG_RESPONSE = 'CREATE_SCHEDULER_TAG_RESPONSE'
        UPDATE_SCHEDULER_TAG_RESPONSE = 'UPDATE_SCHEDULER_TAG_RESPONSE'

    class Product:
        CREATE_PRODUCT_RESPONSE = 'CREATE_PRODUCT_RESPONSE'
        GET_PRODUCT_INFO_RESPONSE = 'GET_PRODUCT_INFO_RESPONSE'

    class Flag:
        UPDATE_VKYC_FLAG_RESPONSE = 'UPDATE_VKYC_FLAG_RESPONSE'

    class PostingInstruction:
        INBOUND_HARD_SETTLEMENT_RESPONSE = 'INBOUND_HARD_SETTLEMENT_RESPONSE'
        OUTBOUND_HARD_SETTLEMENT_RESPONSE = 'INBOUND_HARD_SETTLEMENT_RESPONSE'
        TRANSFER_RESPONSE = 'TRANSFER_RESPONSE'
        AUTH_RESPONSE = 'AUTH_RESPONSE'
        SETTLE_RESPONSE = 'SETTLE_RESPONSE'
        RELEASE_RESPONSE = 'RELEASE_RESPONSE'
        LATEST_TRANSFER_RESPONSE = 'LATEST_TRANSFER_RESPONSE'
        GET_LIST_POSTING_RESPONSE = 'GET_LIST_POSTING_RESPONSE'
        GET_POSTING_RESPONSE = 'GET_POSTING_RESPONSE'

    class Balances:
        GET_LIVE_BALANCES_RESPONSE = 'GET_LIVE_BALANCES_RESPONSE'
