""" this script will scrape and generate proxies from sslproxies.org """

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random


ua = UserAgent()  # from here we generate a random user agent
proxies = []  # will contain proxies [ip, port]

def get_proxy():
    """ get proxy function """

    # retrieve latest proxies
    proxies_req = Request('https://www.sslproxies.org/')
    proxies_req.add_header('User-Agent', ua.random)
    proxies_doc = urlopen(proxies_req).read().decode('utf8')

    soup = BeautifulSoup(proxies_doc, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

    # save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({'ip': row.find_all('td')[0].string,
                       'port': row.find_all('td')[1].string})

    # choose a random proxy
    proxy_index = random_proxy()
    proxy = proxies[proxy_index]

    # loop through proxies until a valid proxy is found
    for n in range(1, 100):
        req = Request('http://icanhazip.com')
        req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')

        try:
            # make the call
            my_ip = urlopen(req).read().decode('utf8')
            my_ip.strip()
            my_ip = my_ip + ":" + proxy['port']
            ip_dict = { "http": my_ip }
            return ip_dict
        except:
            # if error, delete this proxy and find another one
            del proxies[proxy_index]
            proxy_index = random_proxy()
            proxy = proxies[proxy_index]

def random_proxy():
    """ retrieve a random index proxy (we need the index to delete it if not working) """
    return random.randint(0, len(proxies) - 1)


if __name__ == '__main__':
    main()
