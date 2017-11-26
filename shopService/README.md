# Micro service shop (product) ##

## Instalação:

### Primeiro crie um ambiente virtual com o seguinte comando:

virtualenv -p python3 shop-service

### Em seguida ative a virtualenv, da seguinte forma (ambientes unix):

source shop-service/bin/activate 

### Instale as dependências do sistema:

pip install -r requirements.txt

### Rode o projeto:

python manage.py runserver IP:PORTA (Ex: 127.0.0.1:8000)


