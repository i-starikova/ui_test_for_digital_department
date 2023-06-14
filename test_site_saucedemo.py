from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

driver.get(URL)
input_user_name = driver.find_element(By.ID, 'user-name')
input_password = driver.find_element(By.ID, 'password')
input_user_name.send_keys(LOGIN)
input_password.send_keys(PASSWORD)
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()
driver.quit()


