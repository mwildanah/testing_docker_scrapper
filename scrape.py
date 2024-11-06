from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set options for headless browsing
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # run in headless mode
options.add_argument('--no-sandbox')  # to avoid issues with Docker
options.add_argument('--disable-dev-shm-usage')  # to avoid shared memory issues

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Go to the webpage
driver.get('http://example.com')

# Example: Extract title
title = driver.title
print(f"Page Title: {title}")

# Close the driver
driver.quit()
