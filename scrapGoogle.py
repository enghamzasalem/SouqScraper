from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import requests

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")
driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys("2*2-1")
driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(Keys.ENTER)
driver.maximize_window()
pages = driver.find_element_by_xpath("//span[@class='qv3Wpe']")
print(pages.get_attribute("innerHTML"))
