import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Configuração do Firefox no Ubuntu
geckodriver_path = '/usr/local/bin/geckodriver'

# Opções do Firefox
firefox_options = Options()
firefox_options.add_argument("--start-maximized")

# Inicializa o WebDriver
service = Service(executable_path=geckodriver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

# Lista de URLs
urls = [
    "https://app.powerbi.com/groups/me/reports/1fc5b222-b34e-468e-bdfb-6896e58cb6ce/fb8c5ac5d90d9c99a93a?chromeless=true&experience=power-bi",
    "https://app.powerbi.com/groups/me/reports/1fc5b222-b34e-468e-bdfb-6896e58cb6ce/03ece03b7ec53bd61f4e?chromeless=true&experience=power-bi",
    "https://app.powerbi.com/groups/me/reports/1fc5b222-b34e-468e-bdfb-6896e58cb6ce/5badfa4e9031d9c33974?chromeless=true&experience=power-bi",
    "https://app.powerbi.com/groups/me/reports/1fc5b222-b34e-468e-bdfb-6896e58cb6ce/4f15e80ed0b9580481e0?chromeless=true&experience=power-bi",
    "https://app.powerbi.com/groups/me/reports/1fc5b222-b34e-468e-bdfb-6896e58cb6ce/0cd786648a987de0ddb1?chromeless=true&experience=power-bi",
    "https://app.powerbi.com/groups/me/reports/1fc5b222-b34e-468e-bdfb-6896e58cb6ce/92f311729b4d2e920cd3?chromeless=true&experience=power-bi"
]

# Abre cada URL em uma nova aba
for url in urls:
    driver.execute_script(f"window.open('{url}', '_blank');")

# Fecha a aba inicial vazia (opcional)
if len(driver.window_handles) > len(urls):
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# Função aprimorada para alternar e atualizar abas
def switch_and_refresh_tabs(switch_interval, refresh_interval):
    last_refresh_time = time.time()
    
    while True:
        current_time = time.time()
        
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            
            # Atualiza a aba se passou 1 hora
            if current_time - last_refresh_time >= refresh_interval:
                driver.refresh()
                last_refresh_time = current_time  # Reinicia o contador
            
            time.sleep(switch_interval)

# Chama a função com:
# - 30 segundos para alternar entre abas
# - 3600 segundos (1 hora) para atualizar
switch_and_refresh_tabs(30, 3600)

