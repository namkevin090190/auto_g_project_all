from cores.utils.drivers import SeleniumActions
from cores.utils import AssertUtil, MultiAssertsUtil


class CommonBase(SeleniumActions, AssertUtil, MultiAssertsUtil):
    def __init__(self, driver):
        super().__init__()
        SeleniumActions.__init__(self, driver=driver)
        AssertUtil.__init__(self)
