from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options for headless mode
options = Options()
options.add_argument("--headless")  # Ensure headless mode
options.add_argument("--disable-gpu")  # Disable GPU acceleration
options.add_argument("--no-sandbox")  # Bypass sandbox restrictions (needed for Docker)
options.add_argument("--remote-debugging-port=9222")  # Allow debugging

# Initialize the Chrome driver with ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Set timeout for waiting elements
wait = WebDriverWait(driver, 30)  # Increase wait time to 30 seconds

# Example: Wait until an element is present
element = wait.until(EC.presence_of_element_located((By.ID, "some_element_id")))

# Example operation (navigate to a page)
driver.get("https://www.example.com")
print(driver.title)

# Close the browser after the task
driver.quit()
