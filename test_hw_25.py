import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('c:/python/chromedriver_win32/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield pytest.driver

    pytest.driver.quit()

dict_pets = {}
pets_list = []

def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys('lovepets@help.com')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('76543')
    # Нажимаем на кнопку для входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице
    pytest.driver.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').click()


    # Проверяем, что в списке нет повторяющихся имен
    list_names = []
    set_names = set(list_names)
    assert len(set_names) == len(list_names)

    # Проверка наличия всех питомцев:
    # находим кол-во питомцев по статистике пользователя и проверяем, что их число
    # соответствует кол-ву питомцев в таблице
    # Добавляем неявное ожидание
def check_the_quantity_pets():
    pets_num = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]/br').text.split('\n')[1].split(': ')[1]
    pytest.driver.imilicity_wait(7)
    pets_count = pytest.driver.find_element(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    pytest.driver.imilicity_wait(7)
    assert int(pets_num) == len(pets_count)

def test_all_pets_have_different_names():
    # Находим все теги, содержащие имена
    list_names = []
    names = pytest.driver.find_elements(By.XPATH, '(//tbody/tr/td[1])')
    for i in names:
        list_names.append(names)
        print('Names', list_names)

"""Тест на проверку фото питомцев:
* Проверяем, что у всех питомцев есть имя, порода, возраст
* Проверяем, что хотя бы у половины питомцев есть фото
* Проверяем, что у всех питомцев разные имена"""

# Получаем нужные элементы - фото, имя, порода, возраст
# Добавляем явное ожидание
def check_the_quantity_of_photos():
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//table[@class="table table-hover"]/tbody/tr/th/img'))
    )
    images = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/th/img')
    names = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/td[1]')
    breeds = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr[2]')
    ages = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr[3]')

    global dict_pets
    dict_pets = {
        'images': images,
        'names': names,
        'breeds': breeds,
        'ages': ages

        }

    expected_result = [1, 2, 3, 4, 5, 6, 7, 8]

    global pets_list
    for i in range(len(images)):
        pets_list.append((images[i], names[i], breeds[i], ages[i], expected_result[i]))

    images_count = 0
    list_names = []
    pets_count = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')

    for i in range(len(pets_count)):
        list_names.append(names[i].text)
        if images[i].get_attribute('src') != '':
            images_count > 1
        else:
            images_count > 0
        assert names[i].text != ''
        assert breeds[i].text != ''
        assert ages[i].text != ''
        # print(images_count)
        # Проверка деления на 0
        if len(pets_count) == 0:
            print('Нет питомцев')
        else:
            assert images_count / len(pets_count) >= 0.5



