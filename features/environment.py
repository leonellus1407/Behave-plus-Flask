# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from datetime import datetime

from behave import fixture, use_fixture
from selene import config, browser
from selene.browsers import BrowserName
from selenium import webdriver


@fixture
def browser_chrome(context):
    config.browser_name = BrowserName.CHROME
    driver = webdriver.Chrome("/home/admink/snap/chromedriver")
    browser.set_driver(driver)
    context.browser = browser


def before_all(context):
    #use_fixture(driver_settings, context)
    #use_fixture(browser_chrome, context)
    #context.pzz = pzzBy()
    f = open("log.txt", 'a')
    write_to_file("\n" + "="*10 + "\nStart Session: " + str(datetime.now().strftime('%d.%m.%Y %H:%M:%S')))
    f.close()
    context.var = 0
    pass


def after_all(context):
    #context.browser.close()
    write_to_file("\nStop Session\n" + "="*10)
    pass


def before_scenario(context, scenario):
    #context.browser.close()
    write_to_file("\nStart Scenario")
    pass


def after_scenario(context, scenario):
    #context.browser.close()
    write_to_file("\nStop Scenario")
    pass


@fixture
def create_log(context, step, when_happend):
    #if re.search(r'^eq', step.name):

    try:
        write_to_file("\n========== START " + when_happend.upper() + " ==========")
        write_to_file("\nName of step: [" + str(step.name) + "]")
        write_to_file("\nStatus: " + str(step.status))
        write_to_file("\nhook_failed: " + str(step.hook_failed))
        write_to_file("\nduration: " + str(round(step.duration, 4)) + " sec")
        write_to_file("\nerror_message: " + str(step.error_message))
    except TypeError as ex:
        write_to_file("\nException: " + str(ex))
    finally:
        write_to_file("\n========== END OF " + when_happend.upper() + " ==========")


def write_to_file(string_to_write):
    f = open("log.txt", 'a')
    f.write(string_to_write)
    f.close()

def before_step(context, step):
    #create_log(context, step, "before")


    pass


def after_step(context, step):
    create_log(context, step, "after")
    # if str(step.status) == "Status.failed":
    #     file = open("log.txt", 'a')
    #     file.write("\n########## ReRUN ##########\n")
    #     next_step = 'When ' + step.name
    #     do_next_step = next_step[1:0]
    #     file.write("Next step: [" + str(next_step) + "]\n")
    #     try:
    #         a = context.execute_steps(do_next_step)
    #         file.write("Result: [" + str(a) + "], Type = [" + str(traceback.print_exc()) + "]\n")
    #     except Exception as ex:
    #         file.write("Exception: [" + str(ex) + "]\n")
    #     file.write("########## END ReRUN ##########\n\n")
    #     file.close()


@fixture
def browser_firefox(context):
    config.browser_name = BrowserName.FIREFOX
    driver = webdriver.Firefox()
    browser.set_driver(driver)
    context.browser = browser


@fixture
def driver_settings(context):
    config.timeout = 5
    context.NUM_OF_ITERATIONS = 5


