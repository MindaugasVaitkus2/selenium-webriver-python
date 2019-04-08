import urllib.request
from bs4 import BeautifulSoup
from datetime import date
from selenium import webdriver
import time
import os
import logging
from time import sleep


from selenium.webdriver.chrome.options import Options

logging.basicConfig(filename=r"C:\Users\Ashish Mishra\PycharmProjects\Leading Indicators\medium_blog_count_log.log",
                  format='%(asctime)s: %(levelname)s: %(message)s:',datefmt='%m/%d/%y %I:%M:%S  %p',level=logging.DEBUG)

fs = open('watching_list.csv', 'r+')
lines = fs.readlines()
f=0
z=0
temp=[]

import datetime

x = datetime.datetime.now()


today = x.strftime("%c")


logger = logging.getLogger()
logger.debug("Logs will be generated")

while z < len(lines):
    lines[z] = lines[z].lower().rstrip()
    queries = lines
    z = z + 1
    d = queries[f]
    f = f + 1
    print(d)


    base_urlpage = "https://medium.com/tag/" + d + "/archive/2019"
    print(base_urlpage)
    #print(base_urlpage)
    # run firefox webdriver from executable path of your choice

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    driver = webdriver.Chrome(executable_path=os.path.abspath(r'C:\Users\Ashish Mishra\Desktop\chromedriver.exe'), chrome_options=chrome_options)




    # get web page
    for url in base_urlpage:
        driver.get(base_urlpage)
        scroll_var = [2, 3]
    # execute script to scroll down the page
        time.sleep(5)


        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight-2000);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        count = 1
        #i = 1

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # sleep for 30s
        time.sleep(5)
    # driver.quit()

        results = driver.find_elements_by_xpath("//div[@class='postArticle-readMore']")
        time.sleep(5)

    #results = driver.find_elements_by_xpath("//*[@id='main-content']/section/div[2]/div[1]/div[369]/div/a/div[3]/h3")
        print("------------------------------------------------------------------")
        print(today," Total Number of blogs of : ",d, len(results) )

        driver.quit()

for result in results:
    print(result.text)
    driver.quit()