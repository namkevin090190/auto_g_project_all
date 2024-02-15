from cores.utils import logger, StoreUtil, StringUtil
from cores.utils.drivers import LocatorModify

from platforms.web import By


class Kafka:

    def __init__(self, driver):
        LocatorModify.set_locators(self._admin_login_locators)
        super().__init__(driver)

    _kafka_locators = {
        'adLoginUsernameInput': ('XPATH', '//input[@name="identifier"]', By.XPATH),
        'adLoginPasswordInput': ('XPATH', '//input[@name="password"]', By.XPATH),
        'adSigninButton': ('XPATH', './/button[@name="method"]', By.XPATH),
    }
