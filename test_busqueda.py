from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")

# Buscar campo de texto
buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("inmuebles en Bogotá")
buscador.send_keys(Keys.RETURN)

# Esperar hasta que aparezcan los resultados
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".react-results--main"))
)

# Validar que exista algún resultado
resultados = driver.find_elements(By.CSS_SELECTOR, ".react-results--main")
assert len(resultados) > 0, "No se encontraron resultados."

print("Prueba funcional completada con éxito")
driver.quit()
