#Validar que el rango de hora inicio no pueda ser mayor al hora fin
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

        #Ingresar hora de inicio
        inputStartHour = driver.find_element_by_css_selector("#start_hour_0")
        inputStartHour.clear()
        inputStartHour.send_keys("15:00")
        #Ingresar hora de fin
        inputEndHour = driver.find_element_by_css_selector("#end_hour_0")
        inputEndHour.clear()
        inputEndHour.send_keys("11:00")

        assert "La hora de inicio debe ser menor a la hora fin, y el rango debe ser mayor o igual a 15 min." in driver.page_source

        execQueryBtn = driver.find_element_by_css_selector("#exec_query")
        execQueryBtn.click()

        assert "Por favor verifique los errores en la consulta" in driver.page_source
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()