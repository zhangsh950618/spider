# coding=utf-8
__author__ = 'zsh'

import unittest

from selenium import webdriver


class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []

    def test_loginpass(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("登录").click()
        driver.implicitly_wait(30)
        driver.switch_to_frame("login_iframe")
        driver.find_element_by_id("pass_login_username_0").send_keys("name")
        driver.find_element_by_id("pass_login_password_0").send_keys("pwd")
        driver.find_element_by_id("pass_login_input_submit_0").click()

    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
