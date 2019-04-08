from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
caps = DesiredCapabilities().CHROME
caps["marionette"] = True
driver = webdriver.Chrome(executable_path=r'C:\Users\Ashish Mishra\Desktop\chromedriver.exe')

driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")
email_phone.send_keys("Ashish.mishra@edureka.co")
driver.find_element_by_id("identifierNext").click()
password = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
)
password.send_keys("Anurag11#")
driver.find_element_by_id("passwordNext").click()