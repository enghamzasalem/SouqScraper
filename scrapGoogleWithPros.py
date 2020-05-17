from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.google.com/")
search = driver.find_element_by_name("q")
search.send_keys("2*6+8-4")
search.send_keys(Keys.RETURN)
result = driver.find_element_by_xpath("//span[@class='qv3Wpe']")
print(result.get_attribute("innerHTML"))
