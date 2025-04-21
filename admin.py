from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome() 
driver.maximize_window()

try:
    
    driver.get("https://www.guru99.com/")  
    WebDriverWait(driver, 100)

    
    
    print("Offer created successfully:", success_message.text)

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()