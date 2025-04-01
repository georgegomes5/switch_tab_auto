import time
from selenium import webdriver

# Inicializa o WebDriver do Edge
driver = webdriver.Edge()

# Lista de URLs para abrir como abas
urls = [
    "https://www.google.com",
    "https://powerbi.microsoft.com",
    "https://www.bing.com",
    "https://www.microsoft.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.stackoverflow.com",
    "https://www.amazon.com",
    "https://www.wikipedia.org",
    "https://www.facebook.com"
]

# Abre cada URL em uma nova aba
for url in urls:
    driver.execute_script(f"window.open('{url}', '_blank');")

# Maximiza a janela para tela cheia
driver.maximize_window()

# Função para alternar entre todas as abas a cada 30 segundos
def switch_tabs(interval):
    while True:
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            time.sleep(interval)

# Chama a função com um intervalo de 30 segundos
switch_tabs(30)

