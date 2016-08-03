
from ..Modulos.config import *

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = config.baseURL
print("url", url)

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://emod-frontend-qa.internal.tidnode.cl")
        #driver.get(url)
        inputId = driver.find_element_by_css_selector("#userid")
        inputId.send_keys("test")
        inputPass = driver.find_element_by_css_selector("#password")
        inputPass.send_keys("testing123")
        loginBtn = driver.find_element_by_css_selector(".btn.btn-primary")
        loginBtn.click()
        assert "Crear consulta" in driver.page_source
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()