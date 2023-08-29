#! usr/bin/env python3  
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version='114.0.5735.90').install()))
url = 'https://www.youtube.com/results?search_query=Developer'
driver.get(url)

source_list = []
duration_list = []
for i in range(10):
    # scroll 1000 px
    driver.execute_script('window.scrollTo(0,(window.pageYOffset+1000))')
    time.sleep(3)
    # Selenium just removed that method (driver.find_elements_by_xpath()) in version 4.3.0.
    # See the CHANGES (https://github.com/SeleniumHQ/selenium/blob/a4995e2c096239b42c373f26498a6c9bb4f2b3e7/py/CHANGES):
    elements = driver.find_elements("xpath", '//yt-formatted-string[@class = "style-scope ytd-video-renderer"]')
    for element in elements:
        source_list.append(element.text)
print(source_list)
