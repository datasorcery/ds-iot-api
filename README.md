# DS IOT API

## Endpoint Tests - Local

* curl http://localhost:8080/sensor/8563
* curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"temp":"33", "humid": "78"}' \
  http://localhost:8080/sensor/8563

## Endpoint Tests - Remote

* curl https://sensor-api-z2fblziqeq-uc.a.run.app/sensor/8563
* curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"temp":"33", "humid": "78"}' \
  http://localhost:8080/sensor/8563


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
* `Service Name`: sensor-api
* `region`: us-central1 

Test by acessing:

* https://sensor-api-z2fblziqeq-uc.a.run.app
* https://sensor-api-z2fblziqeq-uc.a.run.app/sensor/8563
* curl --header "Content-Type: application/json"\
   --request PUT\
   --data '{"temp":"15", "humid": "55"}'\
   https://sensor-api-z2fblziqeq-uc.a.run.app/sensor/8563


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

# Referencias

* https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods
* https://www.restapitutorial.com/httpstatuscodes.html
* https://flask.palletsprojects.com/en/1.1.x/api/#flask.request
* https://www.restapitutorial.com/lessons/httpmethods.html#:~:text=The%20primary%20or%20most%2Dcommonly,but%20are%20utilized%20less%20frequently.
* https://cloud.google.com/run/docs/quickstarts/build-and-deploy#writing