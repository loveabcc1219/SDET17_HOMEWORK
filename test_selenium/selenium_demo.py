import json

import pytest
from selenium import webdriver

class TestCookieLogin(object):
    def setup_method(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.debugger_address = '127.0.0.1:9222'
        self.driver_debug = webdriver.Chrome(options=chrome_option)
        self.driver_debug.implicitly_wait(10)

        self.driver_new = webdriver.Chrome()
        self.driver_new.implicitly_wait(10)

    def teardown_method(self, method):
        self.driver_debug.quit()
        # self.driver_new.quit()


    def write_login_driver_to_txt(self, filename="./cookie.txt"):
        '''
            获取debug模式下已登录的浏览器cookie，并写入txt文件
        '''
        cookies = self.driver_debug.get_cookies()
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(cookies, f)

    def test_login_by_cookie_txt(self, filename="./cookie.txt"):
        '''
        打开新的浏览器窗口，并利用txt文件中的cookie进行登录
        '''
        self.write_login_driver_to_txt()

        self.driver_new.get('https://work.weixin.qq.com/wework_admin/frame#index')

        with open("cookie.txt", "r", encoding='utf-8') as f:
            cookies = json.load(f)
        for cookie in cookies:
            print("*********", cookie)
            if 'work.weixin.qq.com' in cookie['domain']:
                self.driver_new.add_cookie(cookie)
        # self.driver_new.refresh()
        self.driver_new.get('https://work.weixin.qq.com/wework_admin/frame#contacts')

if __name__ == '__main__':
    pytest.main()
