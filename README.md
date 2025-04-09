# Segunda Atualização: focada para Ubuntu e Firefox

# Passo a passo para funcionamento do script e Dependências:
sudo snap remove geckodriver

# Baixe a versão mais recente (Linux 64-bit)
wget https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux64.tar.gz

# Extraia o arquivo
tar -xvzf geckodriver-v0.36.0-linux64.tar.gz

# Mova para /usr/local/bin e dê permissão
sudo mv geckodriver /usr/local/bin/
sudo chmod +x /usr/local/bin/geckodriver
