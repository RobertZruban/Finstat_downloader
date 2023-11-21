import finstat_login
import database
from bs4 import BeautifulSoup 

companies_table = database.get_ico_table()
run_login = finstat_login.login()



# for loop to get balance sheet 
for company in range(database.get_ico_len()):
    current_company = companies_table['ico'][company]
    url = f"https://finstat.sk/{current_company}/suvaha"
    run_login.get(url)
    html_source = run_login.page_source  
    soup = BeautifulSoup(html_source,'html.parser')
    print(soup)
