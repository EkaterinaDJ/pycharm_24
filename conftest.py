
# Пример фикстуры, где мы указываем браузеру стартовать в режиме киоска (защищённый полноэкранный режим без меню,
# применяемый в публичных местах)
import pytest
import uuid
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()





@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    browser.set_window_size(1400, 1000)

    # Return browser instance to test case:
    yield browser

    # Do tear down (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screenshot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Make screenshot for local debug:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # For happy debugging:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass # just ignore any errors here



# @pytest.fixture
# def chrome_options(chrome_options):
#     chrome_options.binary_location = "C:\Users\User\Downloads\chromedriver.exe\chromedriver.exe"
#     chrome_options.add_extension('/path/to/extension.crx')
#     chrome_options.add_argument('--kiosk')
#     return chrome_options
# # можем добавить уровень логирования для более сложных тестовых сценариев (debug):
# import pytest
# @pytest.fixture
# def driver_args():
#     return ['--log-level=LEVEL']
# # Например, вы можете запустить несколько тестов для настоящей веб-страницы, создать PDF или просто проверить,
# # как браузер отображает страницу.
# import pytest
# @pytest.fixture
# def chrome_options(chrome_options):
#     chrome_options.set_headless(True)
#     return chrome_options

