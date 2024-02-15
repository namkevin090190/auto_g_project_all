from platforms.perf import task, between, HttpUser
from platforms.perf.bench_login.bench_login_test import BenchLogin
from platforms.api.const import ServerConst


class BenchLoginRunner(HttpUser):
    wait_time = between(2, 5)

    def on_start(self):
        self.api = BenchLogin(client=self.client)

    @task
    def bench_login(self):
        token = self.api.pre_login(device_id='AE32EE18-1DF3-4D4A-87E6-D692BD0436FE',
                                   client_id='1f1sqesvlhqnigjgrfjmdotjfp')
        self.api.login(token=token,
                       device_id='AE32EE18-1DF3-4D4A-87E6-D692BD0436FE',
                       username='',
                       password='')
        self.api.get_account_info(cbs_account_no='')

    def on_stop(self):
        self.api.logout()
