from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.libertybooks.com/")

search = driver.find_element(By.ID , 'search-bar')
search.send_keys("moby dick")
search.send_keys(Keys.RETURN)
time.sleep(5)

submit = driver.find_element(By.CLASS_NAME, 'search')
submit = submit.find_element(By.CLASS_NAME, "icon-search")

submit.click()
time.sleep(5)
driver.quit()