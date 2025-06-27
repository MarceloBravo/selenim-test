
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")  # Ejecutar sin interfaz gráfica
chrome_options.add_argument("--user-data-dir=/tmp/chrome-profile")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://duckduckgo.com/")

# Buscar campo de texto
buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("inmuebles en Bogotá")
buscador.send_keys(Keys.RETURN)

# Esperar hasta que aparezcan los resultados
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".results"))
)

# Validar que exista algún resultado
resultados = driver.find_elements(By.CSS_SELECTOR, ".results")
print(driver.page_source)  # Imprime el HTML actual de la página
assert len(resultados) > 0, "No se encontraron resultados."

print("Prueba funcional completada con éxito")
driver.quit()
