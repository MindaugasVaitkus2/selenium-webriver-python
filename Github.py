from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import json
import logging
from datetime import date

i=0

url_list =[]
output=[]

logging.basicConfig(filename=r"C:\Users\Ashish Mishra\PycharmProjects\Leading Indicators\headless_github_log.log",
                  format='%(asctime)s: %(levelname)s: %(message)s:',datefmt='%m/%d/%y %I:%M:%S  %p',level=logging.DEBUG)

base_urlpage = 'https://github.com/search?q='

fs = open('github_list.csv', 'r+')
lines = fs.readlines()
today = date.today()

d1 = today.strftime("%d/%m/%Y")

logger = logging.getLogger()
logger.debug("Logs will be generated")
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

count=0
while i<len(lines):
    z = lines[i].rstrip()
    url_list=base_urlpage+z
    driver = webdriver.Chrome(executable_path=os.path.abspath(r'C:\Users\Ashish Mishra\Desktop\chromedriver.exe'),
                              chrome_options=chrome_options)
    driver.get(url_list)
    count = count + 1
    driver.implicitly_wait(5)
    repository = driver.find_element_by_xpath("//div[@class='d-flex flex-column flex-md-row flex-justify-between border-bottom pb-3 position-relative']//h3")
    print(repository.text)
    output.append(repository.text)
    driver.quit()
    final_output = "Date", d1, "Skill", z, "Repository",output[i]
    with open('Github.json', 'a') as l:
         json.dump(final_output, l, indent=4, sort_keys=True)
    i = i + 1
