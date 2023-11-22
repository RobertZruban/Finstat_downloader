
import requests
from bs4 import BeautifulSoup

# Get the list of free proxies as proxyIP:port
def get_300proxies():
    # list of proxies to be filled
    proxies = []

    # get the webpage content
    res = requests.get('https://free-proxy-list.net/', headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(res.text,'html.parser')
    for items in soup.select("tbody tr"):
        # get proxyIP:port
        proxy_list = ':'.join([item.text for item in items.select("td")[:2]])
        proxies.append(proxy_list)
    return proxies # return list with proxyIP:port items

