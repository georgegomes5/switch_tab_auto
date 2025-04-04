import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Configuração do Firefox no Ubuntu
geckodriver_path = '/usr/local/bin/geckodriver'  # Certifique-se de que o geckodriver está instalado aqui

# Opções do Firefox (opcional)
firefox_options = Options()
firefox_options.add_argument("--start-maximized")  # Já inicia maximizado

# Inicializa o WebDriver do Firefox
service = Service(executable_path=geckodriver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

# Lista de URLs para abrir como abas
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

# Função para alternar entre todas as abas a cada 30 segundos
def switch_tabs(interval):
    while True:
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            time.sleep(interval)

# Chama a função com um intervalo de 30 segundos
switch_tabs(30)

