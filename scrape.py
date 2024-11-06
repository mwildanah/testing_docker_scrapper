from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless (no UI)
chrome_options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open a website
driver.get("https://www.example.com")

# Wait for the page to load
time.sleep(2)

# Scrape an element (example)
element = driver.find_element(By.XPATH, "//h1")
print(f"Scraped text: {element.text}")

# Close the browser
driver.quit()
