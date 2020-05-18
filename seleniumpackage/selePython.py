
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

email = "abhi6900@gmail.com"
password = "Kolkata@1"

driver: WebDriver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
driver.get("https://ui.freecrm.com/")
title = driver.title
print(title)
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_xpath("//input[@placeholder='E-mail address']").send_keys(email)
driver.implicitly_wait(20)
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(password)
driver.find_element_by_xpath("//div[@class='ui fluid large blue submit button']").click()
driver.implicitly_wait(100)
driver.find_element_by_xpath("//div[@id='main-nav']/a[contains(@href,'/companies')]").click()
driver.implicitly_wait(20)
title1 = driver.title
print(title1)
driver.implicitly_wait(20)
btnnew = driver.find_element_by_xpath("//button[contains(text(),'New')]")
if(btnnew.is_displayed()):
    btnnew.click()
else:
    driver.quit()



title1 = driver.title
