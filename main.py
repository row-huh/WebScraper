from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.libertybooks.com/")

search = driver.find_element(By.ID , 'search-bar')
search.send_keys("9780571382453")

submit = driver.find_element(By.CLASS_NAME, 'search')
submit = submit.find_element(By.CLASS_NAME, "icon-search")
submit.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "price"))
    )
finally:
    print("exiting try block")

price = driver.find_element(By.CLASS_NAME, 'price').text.strip("Rs ")
print(price)
time.sleep(5)
driver.quit()