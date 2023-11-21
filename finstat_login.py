import chromedriver_autoinstaller 
from selenium import webdriver    
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
chromedriver_autoinstaller.install() 

file_path = 'login_info.txt'
url = 'https://finstat.sk/Account/LogOn'

try:
    with open(file_path, 'r') as file:
        # Read lines from the file
        lines = file.readlines()
        username = lines[0].strip()
        password = lines[1].strip()


except FileNotFoundError:
    print(f"The file {file_path} was not found.")

except Exception as e:
    print(f"An error occurred: {str(e)}")


# Create Chromeoptions instance 
options = webdriver.ChromeOptions() 
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option("useAutomationExtension", False) 
browser = webdriver.Chrome(options=options) 
browser.get(url)

# login
try:
    input_field_name = browser.find_element(By.ID, 'Email')
    input_field_name.send_keys(f"{username}")
    input_field_password = browser.find_element(By.ID, 'Password')
    input_field_password.send_keys(f"{password}")
    input_field_password.send_keys(Keys.RETURN)
except Exception as e:
    print(f"Error has occured {e}")
