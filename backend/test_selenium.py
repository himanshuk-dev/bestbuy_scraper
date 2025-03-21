from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Selenium WebDriver with WebDriver-Manager
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no browser UI)

# Use WebDriver-Manager to handle ChromeDriver installation
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Test if Selenium is working
driver.get("https://www.bestbuy.ca/en-ca/category/gaming-laptops/36712")
print("Page title:", driver.title)

driver.quit()
