
import json

from datetime import date

from selenium import webdriver

import os
from selenium.webdriver.chrome.options import Options

import logging

from selenium.webdriver.common.keys import Keys

logging.basicConfig(filename=r"C:\Users\Ashish Mishra\PycharmProjects\Leading Indicators\headless_indeed_job_count_log.log",
                  format='%(asctime)s: %(levelname)s: %(message)s:',datefmt='%m/%d/%y %I:%M:%S  %p',level=logging.DEBUG)
a = ['15', '7', '3', '1']
fs = open('watching_list2.csv', 'r+')
lines = fs.readlines()
z=0
f=0
location = 'Bengaluru'
today = date.today()

d1 = today.strftime("%d/%m/%Y")
#print("d1 =", d1)
k=1
# if lines == 'NULL':
logger = logging.getLogger()
logger.debug("Logs will be generated")

while z < len(lines):
    lines[z] = lines[z].lower().rstrip()
    queries = lines
    z = z + 1
    d = queries[f]
    f = f + 1
    query = '{' + d + '}'


    base_url = "https://www.indeed.co.in/jobs?as_and=&as_phr=%22"+query+"%22&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=25&l="+location+"%2C+Karnataka&fromage="
    i = 1
    extended_url = "&limit=10&sort=&psf=advsrch"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    driver = webdriver.Chrome(executable_path=os.path.abspath(r'C:\Users\Ashish Mishra\Desktop\chromedriver.exe'), chrome_options=chrome_options)

    #driver = webdriver.Chrome(executable_path=r'C:\Users\Ashish Mishra\Desktop\chromedriver.exe')
    #driver.set_window_size(1120, 550)
    j=0
    # header = {'Date ':'', 'Location ':'', 'Job_title ':'', 'Source ':'', 'Days :':''}
    # df = pd.Series(header)
    # print(df)
    while j < 4:
        main_url = base_url + a[j] + extended_url

        driver.get(main_url)
        result = driver.find_element_by_id('searchCount')
        temp = result.text
        temp_1 = [temp[i:i + 10] for i in range(0, len(temp), 10)]
        m=d.split(
            "+")
        p = m[0]+' '+m[1]
        #print(p)
        # date = {k, d1 }
        # Data_location = {k, location}
        # Job_data = {k, p}
        # source = {k, 'Indeed'}
        # data_temp = {k, temp_1[1]}
        # data = {'S.No': k, 'Date ': date, 'Location ': Data_location, 'Job_title ': Job_data, 'Source ': source, 'Days :': data_temp}
        # df = pd.DataFrame(data)
        # import json
        g = "Date : ",d1," ",location  , "Job Title : " , p,"  "  "within"" ",a[j]," " + "days : ", temp_1[1]
        with open('data.json', 'a') as l:
            json.dump(g, l, indent=4, sort_keys=True)
        k =k +1
               #print("Date : ",d1," ",location  , "Job Title : " , p,"  "  "within"" ",a[j]," " + "days : ", temp_1[1])
        j = j + 1
    driver.quit()





