
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


import logging
from selenium import webdriver
import time
import json
logging.basicConfig(filename=r"C:\Users\Ashish Mishra\PycharmProjects\Leading Indicators\headless_stackoveflow_log.log",
                  format='%(asctime)s: %(levelname)s: %(message)s:',datefmt='%m/%d/%y %I:%M:%S  %p',level=logging.DEBUG)

logger=logging.getLogger()
logger.debug("Logs will be generated")
base_urlpage = 'https://stackoverflow.com/tags/'
url_list = []
tags_no ={}
fs = open('watching_list.csv', 'r+')
lines = fs.readlines()
#print(lines)
z=0
f=0
# lines = lines.rstrip("")


for line in lines:
        print(line)
        url_list.append(base_urlpage+line)

for url in url_list:
        print(url)

# specify the url

# run firefox webdriver from executable path of your choice

#driver = webdriver.Chrome(executable_path=r'C:\Users\Ashish Mishra\Desktop\chromedriver.exe')


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome(executable_path=os.path.abspath(r'C:\Users\Ashish Mishra\Desktop\chromedriver.exe'),   chrome_options=chrome_options)

for url in url_list:
    # get web page
    driver.get(url)
    # execute script to scroll down the page
    time.sleep(0)

    results = driver.find_elements_by_xpath("//*[@class='grid--cell fl1 fs-body3 mr12']")

    for result in results:
        #print(result.text)
        temp = result.text.split(' ')
        #print(int(temp[0]))
        temp_tag = url.split('/')
        tag = temp_tag[len(temp_tag)-1]
        tags_no[tag] = temp[0]
with open('stackdata.json', 'a') as l:
    json.dump(tags_no, l, indent=4, sort_keys=True)
#print(tags_no)


driver.quit()
