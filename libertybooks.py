from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_price_by_isbn(isbn):
    # initialize driver
    driver = webdriver.Chrome()

    driver.get("https://www.libertybooks.com/")

    search = driver.find_element(By.ID , 'search-bar')
    search.send_keys(isbn)

    submit = driver.find_element(By.CLASS_NAME, 'search')
    submit = submit.find_element(By.CLASS_NAME, "icon-search")
    submit.click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "price"))
        )
    except:
        driver.quit()

    price = driver.find_element(By.CLASS_NAME, 'price').text.strip("Rs ")
    driver.quit()
    return price