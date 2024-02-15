from cores.const.__const import Const
from cores.const.common import EnvironmentConst
import os


class ServerConst(Const):
    __env = os.getenv('env')
    if not __env:
        __env = EnvironmentConst.Environment.SIT_ENV
        CORE_SERVER = f'https://core-api.finx-vault-uat.com/'
    if __env == EnvironmentConst.Environment.SIT_ENV:
        CORE_SERVER = f'https://core-api.finx-vault-uat.com/'
        X_AUTH_TOKEN = None if not os.getenv(
            'SIT_X_AUTH_TOKEN') else os.getenv('SIT_X_AUTH_TOKEN')  # get SIT_X_AUTH_TOKEN from local .env file - sentitive data
    elif __env == EnvironmentConst.Environment.UAT_ENV:
        CORE_SERVER = f'https://core-api.tracer.preprod.saas.tmachine.io/'
        X_AUTH_TOKEN = None if not os.getenv(
            'UAT_X_AUTH_TOKEN') else os.getenv('UAT_X_AUTH_TOKEN')  # get UAT_X_AUTH_TOKEN from local .env file - sentitive data
    INTERNAL_SERVER = f'https://api-int.{__env}.galaxyfinx.cloud/'
    INGRESS_SERVER = f'https://ingress-int.{__env}.galaxyfinx.in/'
