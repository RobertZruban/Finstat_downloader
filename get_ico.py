import requests
#import connect_database
from datetime import date
from bs4 import BeautifulSoup

last_page = 25000
ico_list = []
date_today = []

for x in range(1,4):
    
    url = 'https://finstat.sk/databaza-financnych-udajov?page=' + str(x)
    print(url)
    browser = requests.get(url)  
    soup = BeautifulSoup(browser.text,'html.parser')
    tables = soup.find_all('table')
    for tr in tables:
        for x in range(30):
            try:
                #print(tables)
                #print(soup.find_all('a', {'class', 'truncate openwindow'})[x].get_text())
                ico_substring = str(soup.findAll('a', {'class' : 'truncate openwindow'})[x])
                ico_final = ico_substring[ico_substring.find('/')+1:ico_substring.find('/')+11]
                ico_list.append(ico_final)
                date_today.append(date.today())
            except:
                pass
            


