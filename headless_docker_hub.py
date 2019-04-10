import json

from datetime import date
import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
from selenium.webdriver.chrome.options import Options

logging.basicConfig(filename=r"C:\Users\Ashish Mishra\PycharmProjects\Leading Indicators\headless_docker_hub_logs.log",
                  format='%(asctime)s: %(levelname)s: %(message)s:',datefmt='%m/%d/%y %I:%M:%S  %p',level=logging.DEBUG)

results = []

temp =[]

f=0
z=0
j=0
fs = open('docker_hub.csv', 'r+')
lines = fs.readlines()
clean_urls = []
dock_dict_pulls = {}

today = date.today()

d1 = today.strftime("%d/%m/%Y")
logger = logging.getLogger()
logger.debug("Logs will be generated")
for line in lines:
    clean_line = line.lower().rstrip()
    clean_urls.append(clean_line)


# driver = webdriver.Chrome(executable_path=r'C:\Users\Ashish Mishra\Desktop\chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome(executable_path=os.path.abspath(r'C:\Users\Ashish Mishra\Desktop\chromedriver.exe'), chrome_options=chrome_options)

for url in clean_urls:
    driver.get(url)
    driver.implicitly_wait(60)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"//div[@class='styles__pullCount___2MIKx']"))
        )
        temp = element.text
        if 'Pulls' in temp:
                temp = temp.split('\n')
                temp = temp[1]

        temp_split = url.rsplit('/', 1)
        dock_dict_pulls[temp_split[1]] = temp
        final_layout = "Date/Time :"+d1+",Skill Name:"+temp_split[1]+" Number :"+temp
        #final_layout = d1+','+ temp_split[1] + " Number :" + temp

        print(type(final_layout))
        driver.quit()
        with open('docker_hub_.json', 'a') as l:
            json.dump(final_layout, l, indent=4, sort_keys=True)

    finally:
        driver.quit()
        #print(dock_dict_pulls)


