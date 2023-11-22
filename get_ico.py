import requests
import finstat_login
import proxies
from  database import connect_database,query_table
from bs4 import BeautifulSoup
import time
import random

last_page = 25000
table_name = "ico_numbers"
database_name = "finstat"
schema = 'dbo'
conn = connect_database(database_name)
browser = finstat_login.login()

# Start 1000
# END 2080
for x in range(1671,last_page):

    print(f"Starting {x} itertion")
    url = 'https://finstat.sk/databaza-financnych-udajov?page=' + str(x)
    #print(url)
    #browser = requests.get(url)
   
    
    # proxies_list = proxies.get_300proxies()
    # random_proxy = random.choice(proxies_list)
    # proxy = {
    #     "http": f"http://{random_proxy}",
    #     "https": f"https://{random_proxy}"
    # }
    try:
        browser.get(url)
        html_code = browser.page_source
        soup = BeautifulSoup(html_code, 'html.parser')
        tables = soup.find_all('table')
        
        for tr in tables:
            for x in range(30):
                try:
                    ico_substring = str(soup.findAll('a', {'class': 'truncate openwindow'})[x])
                    ico_final = ico_substring[ico_substring.find('/') + 1:ico_substring.find('/') + 11]
                    ico_final = ico_final.replace('"', '')
                    ico_final = ico_final.strip()
                    print(str(ico_final))
                    
                    company_name = soup.find_all('a', {'class': 'truncate openwindow'})[x].get_text()
                    query = f"INSERT INTO {database_name}.{schema}.{table_name} (ico,spolocnost) VALUES ('{ico_final}','{company_name}')"
                    query_table(query, conn)
                    
                    delay = random.uniform(3, 6)
                    time.sleep(delay)
                except Exception as e:
                    print(f"Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the page. Error: {e}")
                        

       


