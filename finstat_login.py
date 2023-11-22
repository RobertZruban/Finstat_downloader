import chromedriver_autoinstaller 
import random
import proxies
from selenium import webdriver    
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install() 

file_path = 'login_info.txt'
url = 'https://finstat.sk/Account/LogOn'

def credentials(file_path = file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            username = lines[0].strip()
            password = lines[1].strip()

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None, None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None, None
    
    return username, password

# Create a single instance of the browser
def get_browser():
    options = webdriver.ChromeOptions() 
    options.add_argument("--disable-blink-features=AutomationControlled") 
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    options.add_experimental_option("useAutomationExtension", False) 
    browser_instance = webdriver.Chrome(options=options) 
    return browser_instance

# login
def login():
    try:
        username, password = credentials()
        browser = get_browser()
        browser.get(url)
        input_field_name = browser.find_element(By.ID, 'Email')
        input_field_name.send_keys(username)
        input_field_password = browser.find_element(By.ID, 'Password')
        input_field_password.send_keys(password)
        input_field_password.send_keys(Keys.RETURN)
        return browser
    except Exception as e:
        print(f"Error has occurred: {e}")

