import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import requests
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome("C:/chromedriver.exe")
driver.maximize_window()
file1 = open("Myimages.txt","a") 
wait = WebDriverWait(driver, 3)
import urllib.request
for l in range(115,120):
    for i in range(1,40):
        driver.get("http://www.mangapanda.com/shingeki-no-kyojin/"+str(l)+"/"+str(i))
        img_tags = driver.find_elements_by_tag_name('img')
        imags = []
        print(len(img_tags))
        for img in img_tags:
            imags.append(img.get_attribute('src'))
            print(img.get_attribute('src'))
            f = open(img.get_attribute('alt')+'.jpg','wb')
            f.write(requests.get(img.get_attribute('src')).content)
            f.close()
