import requests
from  database import connect_database,query_table
from bs4 import BeautifulSoup

last_page = 25000
table_name = "ico_numbers"
database_name = "finstat"
schema = 'dbo'
conn = connect_database(database_name)
date_today = '2023-11-21'

for x in range(1,2):
    
    url = 'https://finstat.sk/databaza-financnych-udajov?page=' + str(x)
    #print(url)
    browser = requests.get(url)  
    soup = BeautifulSoup(browser.text,'html.parser')
    tables = soup.find_all('table')
    for tr in tables:
        for x in range(30):
            try:
                ico_substring = str(soup.findAll('a', {'class' : 'truncate openwindow'})[x])
                ico_final = ico_substring[ico_substring.find('/')+1:ico_substring.find('/')+11]
                ico_final = ico_final.replace('"','')
                ico_final = ico_final.strip()
                formatted_date = f"'{date_today}'"
                company_name = soup.find_all('a', {'class' : 'truncate openwindow'})[x].get_text()
                query = f"INSERT INTO {schema}.{table_name} (ico,spolocnost, date) VALUES ('{ico_final}','{company_name}',{formatted_date})"
                query_table(query, conn)
            except:
                print("error")  
                
            


