import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# ---- Proxy & User-Agent ----
proxy = None  # Format: "http://username:password@proxy_ip:port" if needed
user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/90.0.4430.212 Safari/537.36"
)

# ---- Chrome Setup ----
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument(f"user-agent={user_agent}")
if proxy:
    options.add_argument(f"--proxy-server={proxy}")

driver = uc.Chrome(options=options)

try:
    search = input("Enter the topic to search: ").strip()

    # 🌐 Open Google
    driver.get("https://www.google.com")
    time.sleep(random.uniform(2, 4))

    # 🍪 Accept cookies if shown
    try:
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept all') or contains(text(), 'I agree')]"))
        )
        consent_button.click()
        print("✅ Accepted cookies")
        time.sleep(2)
    except:
        print("ℹ️ No cookie popup detected")

    # 🔓 Try to sign out if logged in
    try:
        account_button = driver.find_element(By.XPATH, "//a[contains(@href, 'SignOutOptions')]")
        account_button.click()
        print("✅ Clicked on account/profile button")
        time.sleep(2)

        signout_button = driver.find_element(By.XPATH, "//a[contains(@href, 'Logout') or contains(text(), 'Sign out')]")
        signout_button.click()
        print("✅ Signed out successfully")
        time.sleep(3)
    except:
        print("ℹ️ No account/sign-out option visible — either already signed out or not logged in.")

    # 🔍 Perform search
    try:
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.clear()
        search_box.send_keys(search)
        time.sleep(random.uniform(1, 2))
        search_box.send_keys(Keys.RETURN)
        print("✅ Search submitted")
    except Exception as e:
        print(f"❌ Could not interact with search box: {e}")
        raise

    time.sleep(3)  # Let results load

    # 🧠 Check for CAPTCHA / Block page
    if "sorry" in driver.current_url.lower() or "captcha" in driver.page_source.lower():
        driver.save_screenshot("captcha_page.png")
        print("❌ Google triggered a bot protection page. Screenshot saved as 'captcha_page.png'.")
        raise Exception("Blocked by CAPTCHA")

    # 📸 Screenshot for reference
    driver.save_screenshot("search_results.png")

    # ✅ VALIDATION SECTION
    print("🔍 Validating search results...")
    print(search.lower())
    # 1. Title check
    if search.lower() in driver.title.lower():
        print("✅ Title contains search term")
    else:
        print("❌ Title doesn't contain search term")

    # 2. URL check
    if f"q={search.replace(' ', '+')}" in driver.current_url:
        print("✅ URL contains query")
    else:
        print("❌ URL doesn't contain query")

    # 3. Search results container check
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "search")))
        print("✅ Search results container found")
    except:
        print("❌ Could not find search results container")

    # 4. Search term in result titles
    try:
        results = driver.find_elements(By.CSS_SELECTOR, 'div#search h3')
        if results:
            found = any(search.lower() in r.text.lower() for r in results)
            print("✅ Search term found in results" if found else "❌ Search term not in result titles")
        else:
            print("❌ No search results found")
    except Exception as e:
        print(f"❌ Error reading results: {e}")

    print("⌛ Waiting 60 seconds to review (check 'search_results.png')...")
    time.sleep(60)

except Exception as e:
    print("❌ ERROR:", e)

finally:
    try:
        driver.quit()
    except Exception as e:
        print("⚠️ Driver quit error:", e)
    print("👋 Browser closed")
