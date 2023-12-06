from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_price(name):
    # initialize driver
    driver = webdriver.Chrome()

    driver.get("https://www.libertybooks.com/")

    search = driver.find_element(By.ID , 'search-bar')
    search.send_keys(name)

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



# Uses a name or isbn to look for the book
# if more than one instances are returned, will return a list of dicts with information of
# all books #
def getPricesAndNames(key):
        # initialize driver
    driver = webdriver.Chrome()
    # initialize the website where the book needs to be searched
    driver.get("https://www.libertybooks.com/")
    search = driver.find_element(By.ID , 'search-bar') # look for the search bar
    search.send_keys(key)   # type the key on it 

    submit = driver.find_element(By.CLASS_NAME, 'search') 
    submit = submit.find_element(By.CLASS_NAME, "icon-search")
    submit.click() # find and click on the magnifying glass (search) icon

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "price"))
        )
    except:
        print("Something went wrong")
        driver.quit()

    prices = driver.find_elements(By.CLASS_NAME, 'price')
    book_names = driver.find_elements(By.CLASS_NAME, 'caption')
    
    for i in range(len(prices)):
        prices[i] = prices[i].text
        book_names[i] = book_names[i].text
     
    print(book_names)
    driver.quit()
    return book_names