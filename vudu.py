# Make sure to replace USERNAME and PASSWORD with your own username and password

# Import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
    browser.get(login_url)

    time.sleep(10)

    # Login
    username = browser.find_element_by_name('email')
    password = browser.find_element_by_name('password')

    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)

    browser.find_element_by_css_selector('.custom-button').click()

    time.sleep(5)

    browser.get(url)

    # If the above line doesn't work, use the one below (Included to plan for the future)
    # browser.find_element_by_xpath("""//*[@id="widgetContainer"]/div/div/div[1]/div/div[5]/div[2]/div[1]""").click()

    time.sleep(5)

    movielist = []
    print(movielist)

    counter = 1

    # Get movie names
    for _ in range(1, 22):
        # for _ in range(1,3):
        all_images = browser.find_elements_by_css_selector('.border .gwt-Image')
        # for image in all_images[:5]: # first five elements
        for image in all_images:
            # print('image:', image.get_attribute('src'))
            # print('alt:', image.get_attribute('alt'))
            movienames = image.get_attribute('alt')

            # Add movie name to list
            movielist.append(movienames)

            print(counter, "Scraping Done")
            counter += 1

        # Scroll down the page to load more dynamic content
        for _ in range(1, 25):
            ActionChains(browser).send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(5)

    # Sort movie name list and delete duplicates
    movielist = list(set(movielist))
    movielist.sort()

    print(movielist)
    # Write movie names to a csv file
    file = "Example2.csv"
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        # writer.writerows([movielist])

        movielist2 = []
        for movie in movielist:
            movielist2.append([movie])
        writer.writerows(movielist2)
    print("Writing complete")


if __name__ == '__main__':
    main()
