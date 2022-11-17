import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# python3 -m pytest -v --driver-path Driver/chromedriver  test_selenium_login_my_profile_pets.py
driver = webdriver.Chrome('Driver/chromedriver')

def test_petfriends_login():
    # Open PetFriends base page:
    driver.implicitly_wait(10)
    driver.get("https://petfriends.skillfactory.ru/")


    # click on the new user button
    search_button = driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    search_button.click()


    # click on the У меня уже есть аккауент button
    search_exist_account_button = driver.find_element(By.XPATH, "//a[@href='/login']")
    search_exist_account_button.click()


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


    # find and click on button Moi pitomci
    search_email_input_form = driver.find_element(By.XPATH, "//a[@class='nav-link'][@href='/my_pets']")
    search_email_input_form.click()


    if driver.current_url == 'https://petfriends.skillfactory.ru/my_pets':
        # Make the screenshot of browser window:
        driver.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")


def test_petfriends_all_pets_show_up():
    driver.implicitly_wait(10)
    # checking pets number under profile information
    search_how_many_pets = driver.find_element(By.XPATH, "//div[@class='.col-sm-4 left']['Питомцев:']")

    user_stat_arr = search_how_many_pets.text.split('\n')

    number_of_pets_from_profile_info = re.search('(?<=Питомцев: )(.*)', user_stat_arr[1])
    print("hello")
    print(number_of_pets_from_profile_info.group())

    # checking all pets name
    pets_names = driver.find_elements(By.XPATH, "//div[@title='Удалить питомца']")
    print(len(pets_names))
    pets_count = int(number_of_pets_from_profile_info.group())
    assert len(pets_names) == pets_count


def test_petfriends_half_pets_has_photos():
    driver.implicitly_wait(10)
    # getting pets number count by cross
    count_pets_cross = driver.find_elements(By.XPATH, "//div[@title='Удалить питомца']")


    # getting all pets photos tags
    search_pets_photos = driver.find_elements(By.XPATH, "//th//img")
    exist_photo_counter = 0

    for i in range(len(search_pets_photos)):
        if search_pets_photos[i].get_attribute('src') != '':
            exist_photo_counter = exist_photo_counter + 1

    assert exist_photo_counter >= len(count_pets_cross)/2


def test_petfriends_half_pets_has_name_age_and_breed():
    driver.implicitly_wait(10)
    # getting number of all pets count by cross
    count_pets_cross = driver.find_elements(By.XPATH, "//div[@title='Удалить питомца']")

    # getting number of all names, ages and breed
    all_names = driver.find_elements(By.XPATH, "//table//tr//td[1]")
    all_breeds = driver.find_elements(By.XPATH, "//table//tr//td[2]")
    all_age = driver.find_elements(By.XPATH, "//table//tr//td[3]")

    assert len(all_names) == len(count_pets_cross)
    assert len(all_breeds) == len(count_pets_cross)
    assert len(all_age) == len(count_pets_cross)


def test_petfriends_all_pets_have_different_names():
    driver.implicitly_wait(10)
    # getting all names
    all_names = driver.find_elements(By.XPATH, "//table//tr//td[1]")

    print(all_names[0].text)

    not_repeating_list_names = []

    for i in all_names:
        if i.text not in not_repeating_list_names:
            not_repeating_list_names.append(i.text)


    assert len(all_names) == len(not_repeating_list_names)


def test_petfriends_all_pets_not_repeating():
    driver.implicitly_wait(10)
    # getting number of all pets
    count_pets_cross = driver.find_elements(By.XPATH, "//div[@title='Удалить питомца']")

    # creating lists with name, breed, age
    all_names = driver.find_elements(By.XPATH, "//table//tr//td[1]")
    all_breeds = driver.find_elements(By.XPATH, "//table//tr//td[2]")
    all_age = driver.find_elements(By.XPATH, "//table//tr//td[3]")

    arr_with_pets = []

    for i in range(0, len(count_pets_cross)):
        arr_pet = []
        arr_pet.append(all_names[i].text)
        arr_pet.append(all_breeds[i].text)
        arr_pet.append(all_age[i].text)

        if ''.join(arr_pet) not in arr_with_pets:
            arr_with_pets.append(''.join(arr_pet))

    assert len(arr_with_pets) == len(count_pets_cross)










