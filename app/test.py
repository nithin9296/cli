

# # from datetime import datetime
# import datetime

# s = '1 Oct 2018'

# format1 = '%d %b %Y'

# format2 = '%b-%y'

# d = datetime.datetime.strptime(s, format1).strftime(format2)
# # d = datetime.strptime(s, '%d %b %Y')

# print(d)

# print(d.strftime('%b''-''%y'))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pickle
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

import os, sys, inspect     # http://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe() ))[0]))



chromedriver = os.path.join(current_folder,"chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=/Users/nithinpathak/Library/Application Support/Google/Chrome")
driver = webdriver.Chrome(executable_path = chromedriver, chrome_options=chrome_options)

driver.get(('https://system.netsuite.com/pages/customerlogin.jsp?country=US&vid=wKQ6TkVqAmy0j1es&chrole=17&ck=W-NlUEVqAmm0j0VZ&cktime=158261&promocode=&promocodeaction=overwrite&sj=MF8zfuZp23EB8XjhGWzxGr4wS%3B1538828090192'))
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.ID, 'submitButton')))  
# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))


# driver.get(('https://system.netsuite.com/pages/customerlogin.jsp?country=US'))
# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#      driver.add_cookie(cookie)

# print(cookies)
