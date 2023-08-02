# arquivo: test_login_app.py

import time
import pytest
from appium_driver import AppiumDriver

# Teste de login bem-sucedido
def test_login_successful():
    driver = AppiumDriver.get_driver()

    # Restante do código de teste permanece o mesmo

    driver.quit()

# Teste de login com credenciais inválidas
def test_login_invalid_credentials():
    driver = AppiumDriver.get_driver()

    # Restante do código de teste permanece o mesmo

    driver.quit()
