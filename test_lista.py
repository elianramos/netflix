import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import HtmlTestRunner  

class TestSeleccionarPerfilYListas(unittest.TestCase):
    def setUp(self):
        
        service = Service(executable_path="C:\\Users\\elian\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)

    def test_seleccionar_perfil_y_listas(self):
        driver = self.driver
        driver.get("https://www.netflix.com/login")

        
        email_field = driver.find_element(By.ID, ":r0:")
        password_field = driver.find_element(By.ID, ":r3:")
        email_field.send_keys("elianramos2603@gmail.com")
        password_field.send_keys("Elian2628")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        time.sleep(5)  

        
        try:
            perfil = driver.find_element(By.XPATH, "//span[text()='Elian']")
            perfil.click()
        except Exception as e:
            raise Exception("No se encontraron perfiles disponibles o no se pudo seleccionar el perfil.") from e

        time.sleep(5)  

        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/browse/my-list']")))

        
        series_link = driver.find_element(By.XPATH, "//a[@href='/browse/my-list']")
        series_link.click()

        time.sleep(5)  

        
        self.assertIn("/browse/my-list", driver.current_url)

    def tearDown(self):
        try:
           
            screenshot_path = "screenshot_seleccionar_perfil_y_listas.png"
            self.driver.save_screenshot(screenshot_path)
        except Exception as e:
            print(f"Error en tearDown: {e}")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="reportes",  
            report_name="Reporte_SeleccionarPerfilYListas", 
            combine_reports=True,  
            add_timestamp=True  
        )
    )
