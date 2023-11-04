#Se debe poner la version instalada
FROM python:3.10 

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD bash -c "while true; do sleep 1; done"

## Para crear el docker
# sudo docker compose build 
## Para lanzarlo
# sudo docker compose up -d 
## Para ver el estado del contenedor
# sudo docker compose ps 
## Para conectarse al docker y desarrollar ahi 
# sudo docker compose exec app-csv bash 