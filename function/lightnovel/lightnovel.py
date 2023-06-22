
import undetected_chromedriver as uc
import os
import sys
from time import sleep

sys.path.append("My-Actions/function/lightnovel/")

if __name__ == '__main__':
    driver = uc.Chrome(headless=True,use_subprocess=False)
    driver.get('https://www.lightnovel.us/')

    b = list()

    while len(b) == 0:
        b = driver.find_elements(by="class name", value='hover')

    print(len(b), type(b))
    for i in range(len(b)):
        # print(b[i].text)
        if b[i].text == '登入':
            b[i].click()
            break
    sleep(3)
  
    count = driver.find_elements(by='class name', value='input-control')
    print(len(count), type(count))
    

    user = os.environ['LIGHT_NOVEL_USER']
    password = os.environ['LIGHT_NOVEL_PASS']

    if user == '' or password == '':
        print("请输入账号密码")
        exit(0)
  
    count[0].send_keys(user)
    count[1].send_keys(password)
    sleep(1)

    login = driver.find_elements(by='class name', value='btn-140')
    print(len(login))
    for t in login:
        if t.text == '登入':
            t.click()
            print('login')
    sleep(5)

    
    driver.close()
    # driver.save_screenshot('nowsecure.png')
