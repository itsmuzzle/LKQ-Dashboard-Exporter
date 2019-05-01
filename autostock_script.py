from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import credentials
import requests
import time

# Dashboard properties
dashboard_login_url = credentials.login['dashboard_login_url']
dashboard_search_url = credentials.login['dashboard_search_url']
dashboard_username = credentials.login['dashboard_username']
dashboard_password = credentials.login['dashboard_password']
products_to_search = credentials.login['products_to_search']
date_search_from = credentials.login['date_search_from']
date_search_until = credentials.login['date_search_until']
path_to_chrome_driver = credentials.login['path_to_chrome_driver']

def download_data():
    # Create a new Chrome session and navigate to the login page
    driver = webdriver.Chrome(path_to_chrome_driver)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(dashboard_login_url)

    # Find the login fields, enter and click submit
    driver.find_element_by_class_name("user").send_keys(dashboard_username)
    driver.find_element_by_class_name("pass").send_keys(dashboard_password)
    driver.find_element_by_class_name("loginButton").click()

    # Search for each product in the given date range and export as a CSV
    for product in products_to_search:
        time.sleep(5)
        driver.get(dashboard_search_url + "{}/{}/{}".format(product, date_search_from, date_search_until))
        driver.implicitly_wait(5)
        driver.find_element_by_link_text('Export').click()
        driver.find_element_by_xpath("//*[@id=\"modalSuccess\"]/div/div/div[3]/button").click()
    driver.quit()
    print("Mission completed!")

download_data()
# TODO: combine csv's with pandas