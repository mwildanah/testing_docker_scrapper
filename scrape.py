from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the driver in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the webpage
driver.get("https://example.com")

# Wait for an element to be visible
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
element = wait.until(EC.visibility_of_element_located((By.ID, "some_element_id")))

print("Element is visible and ready for interaction")

# Close the driver
driver.quit()
