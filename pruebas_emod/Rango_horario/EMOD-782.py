#Validar que sólo se puedan ingresar como máximo 3 rangos horarios
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://emod-frontend-qa.internal.tidnode.cl")
        inputId = driver.find_element_by_css_selector("#userid")
        inputId.send_keys("test")
        inputPass = driver.find_element_by_css_selector("#password")
        inputPass.send_keys("testing123")
        loginBtn = driver.find_element_by_css_selector(".btn.btn-primary")
        loginBtn.click()
        assert "Crear consulta" in driver.page_source

        crearConsultaBtn = driver.find_element_by_css_selector(".pull-right.btn.btn-primary")
        crearConsultaBtn.click()
        
        #Agregar todas las zonas de origen
        addOriginBtn = driver.find_element_by_css_selector("#add_origin")
        addOriginBtn.click()

        addAllBtn = driver.find_element_by_css_selector("#add_all")
        addAllBtn.click()

        pullRightBtn = driver.find_element_by_css_selector(".pull-right.btn.btn-primary")
        pullRightBtn.click()


        #Agregar todas las zonas de destino
        addDestinationBtn = driver.find_element_by_css_selector("#add_destination")
        addDestinationBtn.click()

        addAllBtn = driver.find_element_by_css_selector("#add_all")
        addAllBtn.click()

        pullRightBtn = driver.find_element_by_css_selector(".pull-right.btn.btn-primary")
        pullRightBtn.click()

        #Agregar 1er horario   
        assert "Agregar horario" in driver.page_source     
        addNewHourBtn = driver.find_element_by_css_selector("#add_new_hour_range")
        addNewHourBtn.click()

        #Agregar 2do horario
        assert "Agregar horario" in driver.page_source
        addNewHourBtn = driver.find_element_by_css_selector("#add_new_hour_range")
        addNewHourBtn.click()

        #Verificar que no se puede agregar 3er horario
        assert "Agregar horario" not in driver.page_source



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()