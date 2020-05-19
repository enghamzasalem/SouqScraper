from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.google.com/")
search = driver.find_element_by_name("q")
search.send_keys("تعلم البرمجة")
search.send_keys(Keys.RETURN)
#result = driver.find_element_by_xpath("//span[@class='qv3Wpe']")
results = driver.find_elements_by_tag_name("h3")
print(results)
for i in results:
  print(cleanhtml(i.get_attribute("innerHTML")))
print(driver.current_url)
 
