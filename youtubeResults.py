from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
url = 'https://www.youtube.com/results?search_query=Developer'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

source_list = []
duration_list = []
for i in range(10):
    #scroll 1000 px
    driver.execute_script('window.scrollTo(0,(window.pageYOffset+1000))')
    time.sleep(3)
    elements = driver.find_elements_by_xpath('//yt-formatted-string[@class = "style-scope ytd-video-renderer"]')
    for element in elements:
        source_list.append(element.text)
print(source_list)
