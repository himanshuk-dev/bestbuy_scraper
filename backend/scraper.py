from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

    def get_products(self, category_name, category_url):
        self.driver.get(category_url)
        time.sleep(2)
        
        products = []
        while True:
            try:
                product_elements = self.driver.find_elements(By.CSS_SELECTOR, "li[class*='productListItem']")
                print(f"Found {len(product_elements)} products in category {category_name}")
                
                for product in product_elements:
                    try:
                        name = product.find_element(By.CSS_SELECTOR, "h3[class*='productItemName']").text.strip()
                        price = product.find_element(By.CSS_SELECTOR, "div[class*='price']").text.strip()
                        rating_element = product.find_elements(By.CSS_SELECTOR, "meta[itemprop='ratingValue']")
                        rating = rating_element[0].get_attribute("content") if rating_element else "No rating"
                        
                        products.append({
                            "name": name,
                            "price": price,
                            "category": category_name,
                            "rating": rating
                        })
                    except Exception as e:
                        print(f"Skipping product due to error: {e}")
                
                # Check if the "Show More" button is present
                try:
                    show_more = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Show more')]")
                    self.driver.execute_script("arguments[0].click();", show_more)
                    time.sleep(3)
                except:
                    break  # No more products to load
            except Exception as e:
                print(f"Error extracting products: {e}")
                break  # Exit if no more pagination

            # print('products found',products)
        return products

    def scrape(self):
        self.driver.get(self.base_url)
        categories = self.get_categories()

        all_products = []
        for cat_name, cat_url in categories.items():
            print(f"Scraping category: {cat_name} with {cat_url}")
            category_products = self.get_products(cat_name, cat_url)
            print(f"Extracted {len(category_products)} products for category {cat_name}")
            all_products.extend(category_products)
        
        self.driver.quit()
        return all_products

if __name__ == "__main__":
    scraper = BestBuyScraper()
    products = scraper.scrape()
    for product in products[:10]:
        print(product)
