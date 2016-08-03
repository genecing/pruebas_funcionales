import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://emod-frontend-qa.internal.tidnode.cl")
        #Deja en blanco y luego hace click
        loginBtn = driver.find_element_by_css_selector(".btn.btn-primary")
        loginBtn.click()
        assert "Por favor introduce tu nombre" in driver.page_source

        #Ahora ingresa usuario
        inputId = driver.find_element_by_css_selector("#userid")
        inputId.send_keys("test")
        loginBtn = driver.find_element_by_css_selector(".btn.btn-primary")
        loginBtn.click()
        assert "Por favor introduce tu contraseña" in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
