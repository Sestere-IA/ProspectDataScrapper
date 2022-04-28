import requests
import random
from bs4 import BeautifulSoup as bs

proxies = [
    '167.172.248.53:3128',
    '194.226.34.132:5555',
    '203.202.245.62:80',
    '141.0.70.211:8080',
    '118.69.50.155:80',
    '201.55.164.177:3128',
    '51.15.166.107:3128',
    '91.205.218.64:80',
    '128.199.237.57:8080',
]


def get_session(proxies):
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session

for i in range(5):
    s = get_session(proxies)
    try:
        print("Request page with IP:", s.get("http://icanhazip.com", timeout=1.5).text.strip())
    except Exception as e:
        continue