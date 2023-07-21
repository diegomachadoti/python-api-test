import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

#pip install selenium
#pip install faker
def createUser():
    # Configurações do driver do Chrome (certifique-se de que o ChromeDriver esteja no PATH)
    driver = webdriver.Chrome()
    fake = Faker()
    driver.implicitly_wait(10)  # Adiciona uma espera implícita de 10 segundos

    try:
        # Abre a página de login do site
        driver.get('https://front.serverest.dev/login')

        # Insira o nome de usuário e senha nos campos de login
        cadastrar_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="cadastrar"]')
        cadastrar_button.click()

        name_input = driver.find_element(By.ID, 'nome')
        username_input = driver.find_element(By.ID, 'email')
        password_input = driver.find_element(By.ID, 'password')
        login_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="cadastrar"]')

        name = fake.name()
        user = fake.email()
        password = fake.password()
        name_input.send_keys(name)
        username_input.send_keys(user)
        password_input.send_keys(password)
        login_button.click()

        # Verifica se o login foi bem-sucedido redirecionando para uma página após o login
        # Neste exemplo, verificamos o título da página após o login

        # Validação
        h1_element = driver.find_element(By.XPATH, '//h1[text()="Serverest Store"]')
        assert h1_element.text == "Serverest Store", "Tela da Home não possui o texto!!"

        print('Teste de login bem-sucedido!')
        print(f'Nome gerado: {name} / {user} / {password}')

    except Exception as e:
        # Exibe mais detalhes sobre a exceção encontrada
        traceback.print_exc()
        print('Erro no preenchimento:', e)

    finally:
        # Fecha o navegador após o teste
        driver.quit()

# Chamada da função para executar o teste
createUser()
