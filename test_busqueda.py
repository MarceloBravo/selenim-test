
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
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
)


# Cambiar a Bing para evitar bloqueos de DuckDuckGo en CI
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.duckduckgo.com/")

# Buscar campo de texto
buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("inmuebles en Bogotá")
buscador.send_keys(Keys.RETURN)


# Esperar hasta que aparezcan los resultados individuales (más general y más tiempo)
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".b_vList .b_algo, .b_search .b_algo, .b_algo, li"))
)

# Validar que exista algún resultado (más general)
resultados = driver.find_elements(By.CSS_SELECTOR, ".b_vList .b_algo, .b_search .b_algo, .b_algo, li")
if len(resultados) == 0:
    print(driver.page_source)  # Solo imprime el HTML si no hay resultados
assert len(resultados) > 0, "No se encontraron resultados."

print("Prueba funcional completada con éxito")
driver.quit()
