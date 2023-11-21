import requests
from  database import connect_database,query_table
from datetime import date
from bs4 import BeautifulSoup

last_page = 25000
table_name = "ico_numbers"
database_name = "finstat"
schema = 'dbo'
conn = connect_database(database_name)
date_today = '2023-11-21'

for x in range(1,last_page):
    
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
                ico_final = ico_final.strip()
                ico_final = int(ico_final)
                formatted_date = f"'{date_today}'"
                query = f"INSERT INTO {schema}.{table_name} (ico, date) VALUES ({ico_final}, {formatted_date})"
                query_table(query, conn)
            except:
                pass
            


