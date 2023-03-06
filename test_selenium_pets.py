# import pytest
# from pytest_selenium import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
#
#
#
# @pytest.fixture(autouse=True)
# def testing(selenium):
#     #
#     driver = webdriver.Chrome('c:/python/chromedriver_win32/chromedriver.exe')
#     # Переходим на страницу авторизации
#     driver.get('https://petfriends.skillfactory.ru/login')
#
#     yield
#
#     driver.quit()
#
# def test_my_pets(selenium):
#     selenium.find_element(By.ID, 'email').send_keys('lovepets@help.com')
#     selenium.find_element(By.ID, 'pass').send_keys('76543')
#     selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#     selenium.get('https://petfriends.skillfactory.ru/my_pets')
#
#     WebDriverWait(selenium, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
#
#     left_info = selenium.find_element(By.XPATH, ('//body/div[1]/div[1]/div[1]'))
#     num = left_info.get_attribute('innerText')
#
#     assert str(len(quantity) - 1) in num