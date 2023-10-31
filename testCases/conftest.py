from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launch Chrome Browser")
    elif browser == 'chrome':
        driver = webdriver.Firefox()
        print("Launch firefox Browser")
    else:
        driver =webdriver.Ie()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("browser")

###### Pytest Html Report ######
# it is hook for adding environment info to HTML Report
# def pytest_config(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'customers'
#     config._metadata['Tester'] = 'Pavan'

### it is hook for delete/modify environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)




