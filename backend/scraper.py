from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class BestBuyScraper:
    def __init__(self):
        # Configure Selenium WebDriver
        options = Options()
        options.add_argument("--headless")  # Run in headless mode (no browser UI)
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
        
        # Use WebDriver-Manager to install & manage ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "https://www.bestbuy.ca/en-ca/"

    def get_categories(self):
        categories = {}
        try:
            shop_by_category = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Shop by Category')]")))
            category_elements = shop_by_category.find_elements(By.XPATH, "following-sibling::button")
            
            for category in category_elements:
                try:
                    category_name = category.get_attribute("title")
                    category_link = category.find_element(By.XPATH, "following-sibling::div//a").get_attribute("href")
                    categories[category_name] = category_link
                except Exception as e:
                    print(f"Skipping category due to error: {e}")
        except Exception as e:
            print("Error finding categories:", e)
        return categories

    
    def scrape(self):
        self.driver.get(self.base_url)
        categories = self.get_categories()

        for cat_name, cat_url in categories.items():
            print(f"Scraping category: {cat_name} with {cat_url}")

if __name__ == "__main__":
    scraper = BestBuyScraper()
    products = scraper.scrape()
  