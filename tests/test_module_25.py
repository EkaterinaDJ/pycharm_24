import pytest
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(ChromeDriverManager().install())
    # pytest.driver = webdriver.Chrome(r"C:\Users\User\Downloads\chromedriver.exe")
        # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()

def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys('lovepets@help.com')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('76543')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"