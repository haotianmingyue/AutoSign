import os
import sys
import requests
from lxml import etree
from io import BytesIO
from time import sleep


sys.path.append("My-Actions/function/nasiro/")

url = 'https://masiro.me/admin/auth/login'

url_a = 'https://masiro.me/admin'

session = requests.session()
session.headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

r = session.get(url)


def get_params(content):
    params = dict()
    parser = etree.HTMLParser()
    tree = etree.parse(BytesIO(content), parser=parser)

    for elem in tree.findall('//input'):
        name = elem.get('name')
        if name is not None:
            params[name] = elem.get('value', None)

    return params


params = get_params(r.content)
print(params)
params['username'] = os.environ['MASIRO_USER']
params['password'] = os.environ['MASIRO_PASS']

r1 = session.post(url, data=params)

d_r1 = r1.content.decode()

print(d_r1)

session.get(url_a)

sleep(2)

session.close()

