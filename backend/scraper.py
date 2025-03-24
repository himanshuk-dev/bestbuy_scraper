# Scrapes product and category data from BestBuy and stores it in a PostgreSQL database

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from database import DatabaseManager, create_database_if_not_exists

class BestBuyScraper:
    """Handles scraping of BestBuy product data using Selenium and stores results in PostgreSQL."""

    def __init__(self):
        # Setup Selenium in headless mode with standard viewport
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")

        # Automatically manage ChromeDriver via webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "https://www.bestbuy.ca"

        # Connect to PostgreSQL via custom database manager
        self.db = DatabaseManager()

    def get_categories(self):
        """
        Scrapes all categories from the BestBuy homepage under "Shop by Category".
        Stores category name and link into the database.
        """
        categories = {}
        try:
            # Wait for "Shop by Category" header to appear
            shop_by_category = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Shop by Category')]")))
            category_elements = shop_by_category.find_elements(By.XPATH, "following-sibling::button")

            # Loop through discovered categories
            for category in category_elements:
                try:
                    category_name = category.get_attribute("title")
                    category_link = category.find_element(By.XPATH, "following-sibling::div//a").get_attribute("href")
                    categories[category_name] = category_link

                    # Save category in DB
                    self.db.insert_category(category_name, category_link)
                except Exception as e:
                    print(f"⚠️ Skipping category due to error: {e}")
        except Exception as e:
            print("❌ Error locating categories:", e)

        return categories

    def get_products(self, category_name, category_url):
        """
        For a given category, scrapes product details (name, price, rating).
        Supports pagination via "Show More" button.
        Stores products in DB.
        """
        products = []
        next_page_url = category_url
        page_count = 0

        # Get category ID to associate products with category
        category_id = self.db.get_category_id_by_name(category_name)
        if not category_id:
            print(f"❌ Could not find category ID for '{category_name}', skipping products.")
            return products

        # Limit to 2 pages for performance (configurable)
        while next_page_url and page_count < 2:
            page_count += 1
            self.driver.get(next_page_url)
            time.sleep(4)  # Allow dynamic content to load
            
            try:
                # Find all product cards on the page
                product_elements = self.driver.find_elements(By.CSS_SELECTOR, "li[class*='productListItem']")
                print(f"🔍 Found {len(product_elements)} products in category '{category_name}', page {page_count}")

                for product in product_elements:
                    try:
                        name = product.find_element(By.CSS_SELECTOR, "h3[class*='productItemName']").text.strip()
                        price = product.find_element(By.CSS_SELECTOR, "div[class*='price']").text.strip()
                        rating_element = product.find_elements(By.CSS_SELECTOR, "meta[itemprop='ratingValue']")
                        rating = rating_element[0].get_attribute("content") if rating_element else None

                        product_data = {
                            "name": name,
                            "price": price,
                            "category": category_name,
                            "rating": rating or "No rating"
                        }
                        products.append(product_data)

                        # Save product in DB
                        self.db.insert_product(name, price, rating, category_id)
                    except Exception as e:
                        print(f"⚠️ Skipping product due to error: {e}")

                # Handle pagination
                try:
                    next_page_element = self.driver.find_element(By.CSS_SELECTOR, "a.buttonLoadMoreLink_THBoN")
                    relative_url = next_page_element.get_attribute("href")
                    if relative_url:
                        next_page_url = self.base_url + relative_url if relative_url.startswith("/") else relative_url
                    else:
                        next_page_url = None
                except:
                    next_page_url = None  # No "Show More" button means last page
            except Exception as e:
                print(f"❌ Error extracting products: {e}")
                break

        return products

    def scrape(self):
        """
        Triggers the scraping process:
        - Navigates to homepage
        - Collects all categories
        - Iterates over each category and scrapes products
        - Closes browser and DB connection
        """
        self.driver.get(self.base_url)
        categories = self.get_categories()

        all_products = []
        for cat_name, cat_url in categories.items():
            print(f"🚀 Scraping category: {cat_name}")
            category_products = self.get_products(cat_name, cat_url)
            print(f"✅ Extracted {len(category_products)} products for {cat_name}")
            all_products.extend(category_products)

        self.driver.quit()
        self.db.close_connection()
        return all_products

# Run this script directly to initialize DB and start scraping
if __name__ == "__main__":
    create_database_if_not_exists()
    db = DatabaseManager()
    db.initialize_db()
    scraper = BestBuyScraper()
    products = scraper.scrape()

    # Print sample output
    for product in products[:10]:
        print(product)
