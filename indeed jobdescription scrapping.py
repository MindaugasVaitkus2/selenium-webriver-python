import re
import json
import string
from bs4 import BeautifulSoup
from selenium import webdriver
import csv



def get_soup(url):
    driver = webdriver.Chrome(executable_path=r'C:\Users\Ashish Mishra\Desktop\chromedriver.exe')
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    driver.close()
    return soup

def get_job_links(soup):
    urls = []
    # Loop thru all the posting links

    for link in soup.find_all('h2', {'class': 'jobtitle'}):
        # Since sponsored job postings are represented by "a target" instead of "a href", no need to worry here
        partial_url = link.a.get('href')
        # This is a partial url, we need to attach the prefix
        url = 'https://www.indeed.co.in' + partial_url
        # Make sure this is not a sponsored posting
        urls.append(url)
    return urls


def get_urls(query, num_pages, location, state):
    # # h  https: // www.indeed.co. in / jobs?q ={}& l ={} + % 2C + Karnataka & start = 10
    #
    hey_url = 'https: // www.indeed.co.in / jobs?q = {}  & l = {}+,+{}'.format(query, location, state)

    base_url = hey_url.translate(({ord(c): None for c in string.whitespace}))
    print(base_url)
    soup = get_soup(base_url)
    urls = get_job_links(soup)
    # https: // www.indeed.co.in / jobs?q = [ % 27 % 22data + scientist % 22 % 27] & l = Bengaluru, +Karnataka
    # Get the total number of postings found
    # # https: // www.indeed.co. in / jobs?q = % 22data + engineer % 22 & l = Bengaluru % 2C + Karnataka
    posting_count_string = soup.find(name='div', attrs={'id': "searchCount"}).get_text()
    posting_count_string = posting_count_string[posting_count_string.find('of') + 2:].strip()
    try:
        posting_count = int(posting_count_string)
    except ValueError:  # deal with special case when parsed string is "360 jobs"
        posting_count = int(re.search('\d+', posting_count_string).group(0))
    finally:
        posting_count = 330  # setting to 330 when unable to get the total
        pass
    max_pages = round(posting_count / 10) - 3
    if num_pages > max_pages:
        print('returning max_pages!!')
        return max_pages
    if num_pages >= 2:
        for i in range(2, num_pages + 1):
            num = (i - 1) * 10
            # https: // www.indeed.co. in / jobs?q = % 22
            # etl + developer % 22 & l = Bengaluru, +Karnataka & start = 0
            # https: // www.indeed.co. in / jobs?q = % 22data + engineer % 22 & l = Bengaluru, +Karnataka & start = 0
            hey_url = 'https: // www.indeed.co.in / jobs?q = {}  & l = {}+,+{}&start={}'.format(query, location, state, num)

            base_url = hey_url.translate(({ord(c): None for c in string.whitespace}))
            try:
                soup = get_soup(base_url)
                urls += get_job_links(soup)
            except:
                continue


    return urls


def get_posting(url):
    soup = get_soup(url)
#h3 tag
    title = soup.find(name='h3').getText().lower()
    posting = soup.find(name='div', attrs={'class': "jobsearch-JobComponent"}).get_text()

    return title, posting.lower()



def get_data(query, num_pages, location):
    postings_dict = {}
    urls = get_urls(query, num_pages, location, state)

    if isinstance(urls, list):
        num_urls = len(urls)
        for i, url in enumerate(urls):
            try:
                title, posting = get_posting(url)
                postings_dict[i] = {}
                postings_dict[i]['title'], postings_dict[i]['posting'], postings_dict[i]['url'] = \
                    title, posting, url
            except:
                continue


        # with open('file_name'.csv, 'w') as file_name:
        #   csv.writer(file_name, postings_dict)

        file_name = query.replace('"', "") + '.json'
        with open(file_name, 'w+') as f:
            print('hey')
            print((file_name))
            json.dump(postings_dict, f)




        print('{} JobPostings have been scraped : '.format(num_urls))



if __name__ == "__main__":

    fs = open('watching_list2.csv', 'r+')
    lines = fs.readlines()

    i = 0

    while i < len(lines):
        lines[i] = lines[i].lower().rstrip()
        queries = lines
        i = i + 1
        d = queries[0]
    query = '"'+d+'"'
    print(query)
    num_pages = 1
    location = 'Bengaluru'
    state = 'Karnataka'

    get_data(query, num_pages, location)