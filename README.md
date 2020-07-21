# DS IOT API

## Endpoints

## Desenvolvimento e Testes

Para desenvolvimento desta API, faça checkout do repositório, crie um virtualenv e instale as dependências :

* Checkout do REPO: 
* Criar um virtualenv: `virtualenv venv`
* Ativar o virtualenv: `source venv/bin/activate`
* Instalar os requirements: `pip install -r requirements.txt` 

## Deploy via Cloud Run

Criar imagem do container

* gcloud builds submit --tag gcr.io/ds-iot-api/sensor-api

Deploy image

* gcloud run deploy --image gcr.io/ds-iot-api/sensor-api --platform managed

Test by acessing:

* https://sensor-api-z2fblziqeq-uc.a.run.app


# Deploy alternativo - Cloud Functions

Se vc quiser testar localmente instale o [functions-framework-python](https://github.com/GoogleCloudPlatform/functions-framework-python) e obtenha credenciais para acessar de sua máquina, se estiver utilizando outros serviços do GCP

* pip install functions-framework
* export GOOGLE_APPLICATION_CREDENTIALS=`pwd`"/gcp.json"
* functions-framework --target='function_name'

## Criando e atualizando Cloud Function

Para fazer deploy de uma Cloud Function, defina seu código no arquivo `main.py` e utilize o seguinte comando gcloud:

* gcloud functions deploy <nome_da_funcao> --runtime python37 --trigger-http --allow-unauthenticated

Para este projeto, utilize

* gcloud functions deploy sensor --runtime python37 --trigger-http --allow-unauthenticated