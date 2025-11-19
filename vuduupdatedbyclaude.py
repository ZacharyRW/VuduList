# Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Login Information
USERNAME = "example@gmail.com"
PASSWORD = "example"

# URLs
login_url = "https://my.vudu.com/MyLogin.html?type=sign_in&url=https%3A%2F%2Fwww.vudu.com%2F"
url = "https://www.vudu.com/movies/#my_vudu/my_movies"

def main():
    # Open Browser
    chromedriver = 'C:\\chromedriver.exe'
    browser = webdriver.Chrome(chromedriver)
    
    try:
        browser.get(login_url)
        
        # Use WebDriverWait instead of fixed sleep times
        wait = WebDriverWait(browser, 10)
        
        # Login - FIXED: Updated to new Selenium syntax
        username = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
        password = browser.find_element(By.NAME, 'password')
        
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        browser.find_element(By.CSS_SELECTOR, '.custom-button').click()
        
        time.sleep(5)
        browser.get(url)
        time.sleep(5)
        
        movielist = []
        print(movielist)
        counter = 1
        
        # Get movie names
        for _ in range(1, 22):
            # FIXED: Updated to new syntax
            all_images = browser.find_elements(By.CSS_SELECTOR, '.border .gwt-Image')
            
            for image in all_images:
                movienames = image.get_attribute('alt')
                # Check if movie already in list to avoid duplicates
                if movienames and movienames not in movielist:
                    movielist.append(movienames)
                    print(counter, "Scraping Done")
                    counter += 1
            
            # Scroll down the page to load more dynamic content
            for _ in range(1, 25):
                ActionChains(browser).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(5)
        
        # Sort movie name list (no need to delete duplicates now)
        movielist.sort()
        print(f"\nTotal movies found: {len(movielist)}")
        print(movielist)
        
        # Write movie names to a csv file
        file = "Example2.csv"
        with open(file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, dialect='excel')
            for movie in movielist:
                writer.writerow([movie])
        
        print("Writing complete")
    
    except Exception as e:
        print(f"Error occurred: {e}")
    
    finally:
        # Always close the browser
        browser.quit()

if __name__ == '__main__':
    main()
