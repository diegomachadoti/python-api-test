# python-api-test
Projeto realizando teste em API REST utilizando python.

### Pré Requisitos
* Python 3+
* Pip (gerenciador de pacotes do Python)
* Acesso à internet
* Algum editor de texto ou IDE (VsCode ou PyCharm)

### Instalação do Python
Acesse aqui: https://www.python.org/downloads/
> Faça o download da versão mais recente (ou de alguma versão recente, o importante é que utilizemos Python 3 porque o suporte ao Python 2 foi encerrado no fim de 2019.

Verificar python configurado
> python -V


### Instação bibliotecas do pytest
> pip install requests pytest

### Api de Teste
Vamos usar a API de exemplo Dummy Rest API
> Veja que ele nos oferece rotas com todos os verbos HTTP apresentados inicialmente e nos permite buscar, criar, deletar e atualizar empregados (employees)

http://dummy.restapiexample.com/api/v1/employees
https://reqres.in

### Executar Test
No terminal acessar a pasta do teste e executar:
> python getTest.py

### Analise de Código
Projeto configurado no sonarCloud
> https://sonarcloud.io/project/overview?id=diegomachadoti_python-api-test