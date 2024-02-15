import os
from getgauge.python import data_store, before_scenario, before_suite, before_spec, after_suite, after_spec, \
    after_scenario, after_step, before_step
from selenium.webdriver.chrome.webdriver import WebDriver


from cores.const.common import EnvironmentConst, CommonTypeUsageConst
from cores.const.api import APIConst
from cores.const.mobile import AppiumConst

from cores.model import EnvObj
from cores.utils.logger_util import logger
from cores.utils.common.store_util import GetUtil, StoreUtil
from cores.utils.common.string_util import StringUtil, StringFormat
# from cores.utils.testlink.base_test_link import BaseTestLink
from cores.utils.backend.data_setup_util import DataSetup
from cores.utils.drivers.appium.virtual_device_util import VirtualDeviceUtil
from cores.utils.drivers.appium.appium_server import AppiumServer

from .helpers.setup import CommonUsage
from .helpers.driver_handler import DriverHandler


def suite_set_up():
    """
        This wrapper will run first and check all environments define in config file
        It will double-check the config and setup the env to execute test.
        e.g.
        if is_api:
            ==> We will execute api test
        if is_web:
            ==> We will execute web test
        if is_mobile:
          ==> execute mobile test: ios or android
        if is_e2e:
          ==> execute combination test on all platforms

    """

    env: str = os.getenv(EnvironmentConst.Environment.ENV_OBJ)
    is_api: bool = True if os.getenv(
        EnvironmentConst.Configuration.IS_API) == CommonTypeUsageConst.TRUE.upper() else False
    is_web: bool = True if os.getenv(
        EnvironmentConst.Configuration.IS_WEB) == CommonTypeUsageConst.TRUE.upper() else False
    is_e2e: bool = True if os.getenv(
        EnvironmentConst.Configuration.IS_E2E) == CommonTypeUsageConst.TRUE.upper() else False
    is_mobile: bool = True if os.getenv(EnvironmentConst.Configuration.IS_IOS) \
        or os.getenv(EnvironmentConst.Configuration.IS_ANDROID) == CommonTypeUsageConst.TRUE.upper()\
        else False
    is_headless: bool = True if os.getenv(
        EnvironmentConst.Configuration.IS_HEADLESS) == CommonTypeUsageConst.TRUE.upper() else False
    is_testlink: bool = True if os.getenv(
        EnvironmentConst.Configuration.IS_TEST_LINK) == CommonTypeUsageConst.TRUE.upper() else False
    api_key: str = None
    api_name: str = None
    browser: str = os.getenv(EnvironmentConst.Environment.BROWSER)
    project_name: str = os.getenv(EnvironmentConst.Environment.PROJECT_NAME)
    base_api_url = os.getenv(APIConst.API_URL)
    api_key = os.getenv(APIConst.API_KEY)
    api_name = os.getenv(APIConst.API_NAME)
    token: str = None
    platform: str = None
    version: str = None
    url: str = None
    base_domain = None
    log_level: str = os.getenv(EnvironmentConst.Environment.LOG_LEVEL).upper() \
        if os.getenv(EnvironmentConst.Environment.LOG_LEVEL) else EnvironmentConst.Logger.INFO
    root_user: str = os.popen('whoami').read().strip()
    # flag = True if (os.getenv(EnvironmentConst.Environment.TOKEN) != CommonTypeUsageConst.FALSE
    #                 or not os.getenv(EnvironmentConst.Environment.TOKEN)) else False
    # if is_api:
    #     token = CommonUsage.__generate_token()
    # else:
    #     pass
    if is_web:
        url = os.getenv(EnvironmentConst.Environment.BASE_URL) % {
            'env': env, 'domain': base_domain}
    else:
        pass
    _d = dict(env=env,
              project_name=project_name,
              base_url=url,
              base_api_url=base_api_url,
              browser=browser,
              log_level=log_level,
              is_api=is_api,
              is_web=is_web,
              is_mobile=is_mobile,
              is_headless=is_headless,
              is_testlink=is_testlink,
              is_e2e=is_e2e,
              active_user=root_user,
              api_key=api_key,
              api_name=api_name,
              token=token,
              ms_projects=project_name,
              base_domain=base_domain)
    StoreUtil.suite_store(keyword=EnvironmentConst.Environment.ENV_OBJ,
                          data=EnvObj(**_d))

    print("\t INFORMATION")
    print("\t -----------")
    print(f"\t * Test Environment: {env}")
    print(f"\t * Project Name: {project_name}")
    if url:
        print(f"\t * Test URL: {url}")
    if platform:
        print(f"\t * Platform: {platform}")
    if version:
        print(f"\t * Version: {version}")
    data_store.suite.dict_test_cases_result = []
    if not (is_api or is_web or is_mobile):
        logger.warning("Not Support!")
    else:
        if is_testlink:
            CommonUsage.__test_link_generator()
        if is_api:  # api case
            # SwaggerUtil.parsing_swagger(
            #     url=swagger_url, is_gitlab=flag, prj_name=project_name)
            pass
        if is_web and url:  # Web test
            DataSetup.set_up_data()
            DriverHandler.open_browser(
                headless=is_headless, browser=browser)
        if is_mobile:  # Mobile test
            DataSetup.set_up_data()
            DriverHandler.open_app()  # Install and open application
        if is_e2e:
            pass


def suite_teardown():
    """
        This wrapper will help to clean all stored data withing suite level.
        if mobile or web testing, we will also close and quit all drivers
    """
    logger.debug("\n\t SUITE TEARDOWN")
    env_obj: EnvObj = GetUtil.suite_get(EnvironmentConst.Environment.ENV_OBJ)
    drivers = list()
    if env_obj.is_web or env_obj.is_mobile:
        drivers.append(GetUtil.suite_get(EnvironmentConst.Driver.DRIVER))
    # if env_obj.is_mobile:
    #     drivers.append(data_store.suite.get(
    #         EnvironmentConst.Driver.MOBILE_DRIVER))

    if drivers:
        if env_obj.is_mobile:
            is_removed = False  # hard code for remove app before suite
            if not is_removed:
                VirtualDeviceUtil.remove_app(platform=os.getenv(
                    AppiumConst.Client.PLATFORM_NAME))
        for d in drivers:
            d.quit()
        if env_obj.is_mobile:
            AppiumServer.stop()
            VirtualDeviceUtil.stop(os.getenv(AppiumConst.Client.PLATFORM_NAME))
    else:
        pass

    if env_obj.is_web or env_obj.is_mobile:
        running_testcases_failed = '&'
        for item in data_store.suite.dict_test_cases_result:
            running_testcases_failed += f'{item}|'
        if len(running_testcases_failed) > 1:
            logger.info(f"Running failed case ids: {running_testcases_failed}")
    else:
        pass
    data_store.suite.clear()


def spec_teardown():
    data_store.spec.clear()


def scenario_teardown():
    """
    This wrapper will help to clean all stored data withing scenario level
    """

    def __close_multi_tabs(tabs):
        tabs = driver.window_handles
        if len(tabs) > 1:
            logger.info(f"\t SCENARIO: Close {len(tabs) - 1} tabs")
            for tab in tabs[1:]:
                driver.switch_to.window(tab)
                driver.close()
            driver.switch_to.window(tabs[0])

    if GetUtil.suite_get(keyword=EnvironmentConst.Environment.ENV_OBJ).is_web:
        logger.info("\t SCENARIO: Reset browser")
        # drivers = GetUtil.suite_get(keyword=EnvironmentConst.Driver.DRIVER)
        # for item in drivers:
        driver: WebDriver = GetUtil.suite_get(EnvironmentConst.Driver.DRIVER)
        __close_multi_tabs(driver)
        driver.delete_all_cookies()
        driver.get(driver.current_url)

    if GetUtil.suite_get(keyword=EnvironmentConst.Environment.ENV_OBJ).is_api:
        pass
    if GetUtil.suite_get(keyword=EnvironmentConst.Environment.ENV_OBJ).is_mobile:
        # clear app data
        # app_conf = GetUtil.suite_get(EnvironmentConst.CONFIG_APP_OBJ)
        # os.popen(CommandConst.ADB.CLEAR_APP_DATA %
        #          {'app_package': app_conf.get(AppiumConst.Client.APP_PACKAGE)})
        # re-open application
        driver = GetUtil.suite_get(EnvironmentConst.Driver.MOBILE_DRIVER)
        driver.launch_app()
    data_store.scenario.clear()


@before_suite
def before_suite_hook():
    suite_set_up()


@after_suite
def after_suite_hook():
    suite_teardown()


@before_spec
def before_spec_hook(context):
    logger.info(
        '--------------------------------------------Spec Name--------------------------------------------')
    logger.info(context._ExecutionContext__specification._Specification__name)
    logger.info(
        '-------------------------------------------------------------------------------------------------')


@after_spec
def after_spec_hook():
    spec_teardown()


@after_step
def after_every_step(context):
    if GetUtil.suite_get(keyword=EnvironmentConst.Environment.ENV_OBJ).is_testlink and context._ExecutionContext__step._Step__is_failing:
        pre = data_store.suite.error_message

        error_message = context._ExecutionContext__step._Step__error_message
        step_text = context._ExecutionContext__step._Step__text
        data_store.suite.error_message = f"{pre}\n{step_text}\n{error_message}"
        # You can now work with the error_message as needed, such as logging or reporting it
    else:
        pass


@after_scenario
def after_scenario_hook(context):
    # if GetUtil.suite_get(keyword=EnvironmentConst.Environment.ENV_OBJ).is_web \
    #         or GetUtil.suite_get(keyword=EnvironmentConst.Environment.ENV_OBJ).is_mobile:
    #     """ Remove id is duplicated when retry by gauge command"""
    #     is_failing = context._ExecutionContext__specification._Specification__is_failing
    #     test_id_tag = context.scenario.tags[-1]
    #     dict_test_cases_result = list(dict.fromkeys(
    #         data_store.suite.dict_test_cases_result))
    #     """ Check tag id is valid"""
    #     if test_id_tag[1:].isnumeric() or test_id_tag[2:].isnumeric():
    #         """ If test case is failed, add to list else remove it if it retry success"""
    #         valid_id_tag = StringUtil.format_string_with_re(
    #             re_format=StringFormat.FORMAT_AB_123_PATTERN, repl=StringFormat.FORMAT_AB_123_REPL, value=test_id_tag)

    #         if is_failing:
    #             if test_id_tag not in dict_test_cases_result:
    #                 dict_test_cases_result.append(test_id_tag)
    #         else:
    #             if test_id_tag in dict_test_cases_result:
    #                 dict_test_cases_result.remove(test_id_tag)

    # if is_testlink:
    # browser = GetUtil.suite_get(
    #     keyword=EnvironmentConst.Environment.ENV_OBJ).browser
    # is_testlink = GetUtil.suite_get(
    #     keyword=EnvironmentConst.Environment.ENV_OBJ).is_testlink
    #     try:
    #         test_case_execution = SetTestCaseResult(
    #             build_name=data_store.suite.build_name, test_plan_id=data_store.suite.test_plan_id)
    #         status, notes = test_case_execution.generate_testcase_execution_status(browser=browser, error_message=data_store.suite.error_message) if is_failing \
    #             else test_case_execution.generate_testcase_execution_status(browser=browser, is_passed=True)

    #         test_case_execution.set_test_case_result(test_case_external_id=valid_id_tag,
    #                                                  status=status,
    #                                                  notes=notes)
    #     except Exception as err:
    #         logger.warning(
    #             TestLinkConst.ERROR_SET_TC_EXECUTE_STATUS.format(err))

    #     else:
    #         logger.warning(f"Invalid tags id format: {context.scenario.tags}")

    #     data_store.suite.dict_test_cases_result = dict_test_cases_result
    # else:
    #     pass
    scenario_teardown()


@before_scenario
def before_scenario_hook(context):
    data_store.scenario.clear()
    # if GetUtil.suite_get(keyword=EnvironmentConst.Environment.ENV_OBJ).is_testlink:
    #     test_id_tag = context.scenario.tags[-1]

    #     if test_id_tag[1:].isnumeric() or test_id_tag[2:].isnumeric():
    #         try:
    #             test_case = AddRemoveTestCase(
    #                 project_id=data_store.suite.project_id, test_plan_id=data_store.suite.test_plan_id)
    #             test_case.add_all_test_cases_to_test_plan(
    #                 test_case_external_ids=[test_id_tag])
    #         except Exception as err:
    #             logger.warning(
    #                 TestLinkConst.ERROR_ADD_TC_EXECUTE_STATUS.format(err))


@before_step
def before_step_hook(context):
    logger.info(
        '\n')
    logger.info(
        '--------------------------------------------Step Text--------------------------------------------')
    logger.info(context._ExecutionContext__step._Step__text)
    logger.info(
        '-------------------------------------------------------------------------------------------------')
