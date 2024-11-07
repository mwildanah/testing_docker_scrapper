import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.binary_location = "/usr/bin/chromium"

service = Service(executable_path='/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


url = 'https://www.neuralnine.com/books'

driver.get(url)
soup = BeautifulSoup(driver.page_source, features='lxml')

headings = soup.find_all(name='h2', attrs={'class':'elementor-heading-title'})
for heading in headings:
    print(heading.getText())
time.sleep(5)

driver.quit()

import os

print("Saving file to:", os.path.abspath("/data/scraped_data.csv"))

import pandas as pd

data = {
    'name':['Alice','Bob','Charlie'],
    'age':[25,30,35]
}

df = pd.DataFrame(data)
output_file = '/data/scraped_data.csv'
df.to_csv(output_file, index=False)

print(f'Data saved to {output_file}')
