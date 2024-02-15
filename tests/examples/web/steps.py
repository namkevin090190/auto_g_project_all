from .web_example import WebSample
from platforms import step

from cores.const.common import EnvironmentConst
from cores.utils import GetUtil


@step('[Web][Google] Open page')
def step_imp():
    WebSample(GetUtil.suite_get(EnvironmentConst.Driver.DRIVER)
              ).open_homepage('https://google.com')


@step('[Web][Google] Verify button display')
def step_imp():
    p = WebSample(GetUtil.suite_get(EnvironmentConst.Driver.DRIVER))
    p.verify_btn_display()
