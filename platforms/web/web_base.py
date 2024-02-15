from cores.utils.drivers import SeleniumBase
from cores.utils import AssertUtil, MultiAssertsUtil


class CommonWebBase(SeleniumBase, AssertUtil, MultiAssertsUtil):

    def __init__(self, driver):
        SeleniumBase.__init__(self, driver=driver)
        AssertUtil.__init__(self)
        MultiAssertsUtil.__init__(self)
