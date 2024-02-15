import os
import json

from cores.model import EnvObj

from cores.utils.logger_util import logger
from cores.utils.common.store_util import GetUtil, StoreUtil
from cores.utils.drivers.selenium.selenium_driver import InitDriver
from cores.utils.drivers.appium.appium_server import AppiumServer
from cores.utils.drivers.appium.mobile_driver import DriverAppiumUtil
from cores.utils.drivers.appium.virtual_device_util import VirtualDeviceUtil

from cores.const.common import EnvironmentConst
from cores.const.mobile import AppiumConst, DeviceConst

from cores.decorators import parse_driver_config, parse_app_config


import os
import json

from cores.model import EnvObj

from cores.utils.logger_util import logger
from cores.utils.common.store_util import GetUtil, StoreUtil
from cores.utils.drivers.selenium.selenium_driver import InitDriver
from cores.utils.drivers.appium.appium_server import AppiumServer
from cores.utils.drivers.appium.mobile_driver import DriverAppiumUtil
from cores.utils.drivers.appium.virtual_device_util import VirtualDeviceUtil

from cores.const.common import EnvironmentConst
from cores.const.mobile import AppiumConst, DeviceConst

from cores.decorators import parse_driver_config, parse_app_config


class DriverHandler:

    @staticmethod
    def open_browser(headless: bool = True, browser: str = None):
        """
        open a web browser for next step
        :return: driver
        """
        env_obj: EnvObj = GetUtil.suite_get(
            EnvironmentConst.Environment.ENV_OBJ)
        if not headless and not browser:
            driver = InitDriver.create_driver(
                env_obj.is_headless, env_obj.browser)
        else:
            driver = InitDriver.create_driver(headless, browser)
        env_obj.is_web = True
        StoreUtil.suite_store(EnvironmentConst.Driver.DRIVER, driver)
        return driver

        # drivers = os.getenv(DriverConst.DRIVER).split(',')
        # admin_url = GetUtil.suite_get(EnvironmentConst.ENV_OBJ).admin_base_url
        # driver_list = []
        # for d in drivers:
        #     driver = WebDriverUtil.create_driver(headless, browser)
        #     if driver:
        #         StoreUtil.suite_store(d, driver)
        #         if d == RoleConst.ADMIN:
        #             logger.info(f"{d} role: {admin_url} browser {browser} with Headless: %s" % ('on' if headless else 'off'))
        #             driver.get(admin_url)
        #         else:
        #             logger.info(f"{d} role: {url} browser {browser} with Headless: %s" % ('on' if headless else 'off'))
        #             driver.get(url)
        #         driver_list.append(driver)
        #     else:
        #         raise Exception("Driver can't start.")
        # StoreUtil.suite_store(DriverConst.DRIVER, driver_list)
        # return driver_list

    @staticmethod
    def close_browsers():
        """
        close_browsers will close all active browsers
        """
        for driver in GetUtil.suite_get(EnvironmentConst.Driver.DRIVER):
            driver.quit()
        StoreUtil.scenario_store(
            (EnvironmentConst.Environment.ENV_OBJ).is_web, None)

    @parse_driver_config(os.getenv(AppiumConst.Client.PLATFORM_NAME))
    @parse_app_config(os.getenv(EnvironmentConst.Environment.PROJECT_NAME))
    def close_browsers():
        """
        close_browsers will close all active browsers
        """
        for driver in GetUtil.suite_get(EnvironmentConst.Driver.DRIVER):
            driver.quit()
        StoreUtil.scenario_store(
            (EnvironmentConst.Environment.ENV_OBJ).is_web, None)

    @parse_driver_config(os.getenv(AppiumConst.Client.PLATFORM_NAME))
    @parse_app_config(os.getenv(EnvironmentConst.Environment.PROJECT_NAME))
    def open_app():
        device_conf = GetUtil.suite_get(DeviceConst.OBJ)
        app_conf = GetUtil.suite_get(
            EnvironmentConst.Configuration.CONFIG_APP_OBJ)
        # If start success simulator and appium server -> create appium driver
        condition_start_driver = AppiumServer.start() and VirtualDeviceUtil.start(
            platform=os.getenv(AppiumConst.Client.PLATFORM_NAME))
        # if app is installed. Remove and re-install
        platform_name = os.getenv(AppiumConst.Client.PLATFORM_NAME)

        if VirtualDeviceUtil.is_device_online() and VirtualDeviceUtil.is_app_installed_on_device(platform_name):
            VirtualDeviceUtil.remove_app(platform_name)  # remote app
        # install app
        VirtualDeviceUtil.install_app(platform_name, is_cloud_app=json.loads(
            app_conf.get(DeviceConst.IS_CLOUD_APP).lower()))

        if condition_start_driver:
            driver = DriverAppiumUtil.create_appium_driver(platform_name=os.getenv(AppiumConst.Client.PLATFORM_NAME),
                                                           platform_version=os.getenv(
                AppiumConst.Client.PLATFORM_VERSION),
                device_name=os.getenv(
                AppiumConst.Client.DEVICE_NAME),
                automation_name=device_conf.get(
                AppiumConst.Client.AUTOMATION_NAME),
                app_package=app_conf.get(
                AppiumConst.Client.APP_PACKAGE),
                app_activity=app_conf.get(
                AppiumConst.Client.APP_ACTIVITIES),
                bundle_id=app_conf.get(
                DeviceConst.iOS.BUNDLE_IDENTIFIER)
                if os.getenv(AppiumConst.Client.PLATFORM_NAME) == DeviceConst.iOS.IOS
                else ''
            )
            StoreUtil.suite_store(
                EnvironmentConst.Configuration.MOBILE_DRIVER, driver)
            logger.info('Heading to Application')
            return driver
        else:
            raise Exception("Failed to setup appium server")
        device_conf = GetUtil.suite_get(DeviceConst.OBJ)
        app_conf = GetUtil.suite_get(
            EnvironmentConst.Configuration.CONFIG_APP_OBJ)
        # If start success simulator and appium server -> create appium driver
        condition_start_driver = AppiumServer.start() and VirtualDeviceUtil.start(
            platform=os.getenv(AppiumConst.Client.PLATFORM_NAME))
        # if app is installed. Remove and re-install
        platform_name = os.getenv(AppiumConst.Client.PLATFORM_NAME)

        if VirtualDeviceUtil.is_device_online() and VirtualDeviceUtil.is_app_installed_on_device(platform_name):
            VirtualDeviceUtil.remove_app(platform_name)  # remote app
        # install app
        VirtualDeviceUtil.install_app(platform_name, is_cloud_app=json.loads(
            app_conf.get(DeviceConst.IS_CLOUD_APP).lower()))

        if condition_start_driver:
            driver = DriverAppiumUtil.create_appium_driver(platform_name=os.getenv(AppiumConst.Client.PLATFORM_NAME),
                                                           platform_version=os.getenv(
                AppiumConst.Client.PLATFORM_VERSION),
                device_name=os.getenv(
                AppiumConst.Client.DEVICE_NAME),
                automation_name=device_conf.get(
                AppiumConst.Client.AUTOMATION_NAME),
                app_package=app_conf.get(
                AppiumConst.Client.APP_PACKAGE),
                app_activity=app_conf.get(
                AppiumConst.Client.APP_ACTIVITIES),
                bundle_id=app_conf.get(
                DeviceConst.iOS.BUNDLE_IDENTIFIER)
                if os.getenv(AppiumConst.Client.PLATFORM_NAME) == DeviceConst.iOS.IOS
                else ''
            )
            StoreUtil.suite_store(
                EnvironmentConst.Configuration.MOBILE_DRIVER, driver)
            logger.info('Heading to Application')
            return driver
        else:
            raise Exception("Failed to setup appium server")
