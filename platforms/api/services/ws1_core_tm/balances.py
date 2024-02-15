from cores.utils import RequestUtil, PrepareObj
from cores.model import ResponseObj, RequestObj

from platforms.api.const import ServicesConst, ServerConst
from platforms.api.models.ws1_core_tm.balances import BalancesModel


class BalancesServices:

    def __init__(self):
        self.m_balances = BalancesModel()

    def query_balances(self, account_id: str, account_address: str = None):
        url = ServerConst.CORE_SERVER + ServicesConst.Balances.LIVE + \
            f'?account_addresses={account_address}&page_size=10000&account_ids={account_id}' if account_address != None else ServerConst.CORE_SERVER + ServicesConst.Balances.LIVE + \
            f'?page_size=10000&account_ids={account_id}'
        data: RequestObj = PrepareObj.preparation(self.m_balances)
        r: ResponseObj = RequestUtil.request(method=data.method,
                                             url=url, data=data)
        return r
