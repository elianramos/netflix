import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
import HtmlTestRunner  

class TestSeleccionarPerfilYPeliculas(unittest.TestCase):
    def setUp(self):
       
        service = Service(executable_path="C:\\Users\\elian\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)

    def test_seleccionar_perfil_y_peliculas(self):
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
            print(f"Perfil seleccionado: {perfil.get_attribute('style')}")
            perfil.click()
        except Exception as e:
            raise Exception("No se encontraron perfiles disponibles o no se pudo seleccionar el perfil.") from e

        time.sleep(5) 

        try:
            
            peliculas_link = driver.find_element(By.XPATH, "//a[@href='/browse/genre/34399']")
            peliculas_link.click()
        except Exception as e:
            raise Exception("No se pudo encontrar el enlace de Películas.") from e

        time.sleep(5)  
        self.assertIn("Películas", driver.title) 

    def tearDown(self):
        try:
            
            screenshot_path = "screenshot_seleccionar_perfil_y_peliculas.png"
            self.driver.save_screenshot(screenshot_path)
        except Exception as e:
            print(f"Error en tearDown: {e}")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="reportes",  
            report_name="Reporte_SeleccionarPerfilYPeliculas", 
            combine_reports=True, 
            add_timestamp=True  
        )
    )
