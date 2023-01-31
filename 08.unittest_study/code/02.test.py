from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest


class Blog(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.chrome
        self.driver.get("http://www.cnblogs.com/yoyoketang")

    def test_blog(self):
        time.sleep(3)
        result = EC.title_is(u'上海-悠悠 - 博客园')(self.driver)
        print(result)
        self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
