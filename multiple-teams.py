import undetected_chromedriver as uc
import json
import time

uc.install()

from selenium.webdriver import Chrome

def get_credentials():
    with open('credentials.json') as file:
        credentials = json.load(file)
    
    return credentials

def open_teams(credential, driver):
    print("Trying to login with: " + credential["usr"])
    driver.get("https://teams.microsoft.com")
    time.sleep(5)
    # Get search box element from webElement 'q' using Find Element
    email = driver.find_element_by_name("loginfmt")
    next_button = driver.find_element_by_class_name("ext-primary")

    email.send_keys(credential["usr"])
    time.sleep(1)
    next_button.click()

    time.sleep(5)
    password = driver.find_element_by_name("passwd")
    password.send_keys(credential["pwd"])
    time.sleep(1)
    password.submit()

    time.sleep(1)
    yes_button = driver.find_element_by_class_name("ext-primary")
    yes_button.click()  


credentials = get_credentials()
for credential in credentials["accs"]:
    driver = uc.Chrome()
    try:
        open_teams(credential, driver)
    except:
        print("An exception occurred") 

#   Run forever
while True:
    a = input()