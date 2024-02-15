
import os
import csv

from cores.utils import PathUtil
from cores.const.config import DataConfigConst

from platforms.api.services.authen import PreLoginService


class BaseActions:

    @staticmethod
    def generate_mass_tokens(list_user_file: str, ):
        """
        This method to generate a bunch of live tokens then store and write to csv file for further usage
        It will help to reduce the load on re-generate the token everytime token was called.
        """
        data = []
        file = PathUtil.join_prj_root_path(list_user_file)
        TOKEN_LIST = PathUtil.join_prj_root_path(DataConfigConst.TOKEN_LIST)
        with open(file, 'r') as f:
            for i in csv.reader(f):
                token = ''
                data.append(token)
        f.close()
        with open(PathUtil.join_prj_root_path(TOKEN_LIST), 'w', newline='') as f_csv:
            writer = csv.writer(f_csv)
            for _d in data:
                writer.writerow([_d])
        f_csv.close()

    @staticmethod
    def generate_token(device_id: str, client_id: str) -> str:
        r = PreLoginService().pre_login(
            device_id=device_id,
            client_id=client_id
        )
        return r.response_data['accessToken']
