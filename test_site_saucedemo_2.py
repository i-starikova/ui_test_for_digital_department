from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver
def open_page(driver, url):
    driver.get(url)
def find_element_by_id(driver, locator):
    return driver.find_element(By.ID, locator)
def element_click(driver, locator):
    element = find_element_by_id(driver, locator)
    element.click()
def element_send_keys(driver, locator, text):
    element = find_element_by_id(driver, locator)
    element.send_keys(text)

browser = get_driver()
open_page(browser, URL)
element_send_keys(browser, 'user-name', LOGIN)
element_send_keys(browser, 'password', PASSWORD)
element_click(browser, 'login-button')
browser.quit()
