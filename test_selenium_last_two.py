import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome('Driver/chromedriver')

def test_petfriends_login():
    # Open PetFriends base page:
    driver.implicitly_wait(10)
    driver.get('http://petfriends.skillfactory.ru/login')

    # find and put your e-mail into email form
    search_email_input_form = driver.find_element(By.XPATH, "//input[@type='email']")


    search_email_input_form.clear()
    search_email_input_form.send_keys("ww@rwf.ru")

    # find and put your password into password form
    search_email_input_form = driver.find_element(By.XPATH, "//input[@type='password']")


    search_email_input_form.clear()
    search_email_input_form.send_keys("123")


    # find and click on button Vojti
    search_email_input_form = driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    search_email_input_form.click()

    # checking main page
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"


# using web driver wait, checking all pets cards number
def test_web_driver_wait():
    # web driver wait photo
    images = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//img[@class='card-img-top']")))

    # web driver wait names
    names = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//h5[@class='card-title']")))

    # web driver wait breed and age
    age_and_breed = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//p[@class='card-text']")))


    assert len(names) == len(age_and_breed)



# using web driver IMPLICITY wait
def test_web_driver_implicitly_wait():
    driver.implicitly_wait(10)


    driver.get('http://petfriends.skillfactory.ru/my_pets')

    # getting number of all pets count by cross
    count_pets_cross = driver.find_elements(By.XPATH, "//div[@title='Удалить питомца']")

    # getting number of all names, ages and breed
    all_names = driver.find_elements(By.XPATH, "//table//tr//td[1]")
    all_breeds = driver.find_elements(By.XPATH, "//table//tr//td[2]")
    all_age = driver.find_elements(By.XPATH, "//table//tr//td[3]")

    assert len(all_names) == len(count_pets_cross)
    assert len(all_breeds) == len(count_pets_cross)
    assert len(all_age) == len(count_pets_cross)
