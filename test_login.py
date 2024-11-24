import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
import os

class TestLoginSeleccionPerfil(unittest.TestCase):
    def setUp(self):
        
        service = Service(executable_path="C:\\Users\\elian\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)

    def test_login_y_seleccion_perfil(self):
        driver = self.driver
        driver.get("https://www.netflix.com/login")  

       
        username = driver.find_element(By.ID, ":r0:")  
        password = driver.find_element(By.ID, ":r3:")  
        username.send_keys("elianramos2603@gmail.com")
        password.send_keys("Elian2628")

       
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

       
        WebDriverWait(driver, 10).until(
            EC.url_contains("https://www.netflix.com/browse")
        )

        
        screenshot_path = os.path.join(os.getcwd(), "seleccion_perfil.png")
        driver.save_screenshot(screenshot_path)
        print(f"Captura de pantalla guardada en: {screenshot_path}")

        
        self.assertIn("Netflix", driver.title)
        self.assertTrue(driver.current_url.startswith("https://www.netflix.com/browse"))

    def tearDown(self):
        
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="reportes",  
            report_name="Reporte_TestLogin",  
            report_title="Resultados de Prueba - Login y Selección de Perfil"  
        )
    )
