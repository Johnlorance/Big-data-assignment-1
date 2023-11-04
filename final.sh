#!/bin/bash


docker run -d --name peaceful_chaum ubuntu
docker exec -it peaceful_chaum python dpre.py
docker exec -it peaceful_chaum python eda.py
docker exec -it peaceful_chaum python vis.py
docker exec -it peaceful_chaum python model.py

sleep 5

docker cp peaceful_chaum:/path/to/dpre-output/ /Users/mayermamdouh/Desktop/Assignment1/bd-a1/service-result/
docker cp peaceful_chaum:/path/to/eda-output/ /Users/mayermamdouh/Desktop/Assignment1/bd-a1/service-result/
docker cp peaceful_chaum:/path/to/vis-output/ /Users/mayermamdouh/Desktop/Assignment1/bd-a1/service-result/
docker cp peaceful_chaum:/path/to/model-output/ /Users/mayermamdouh/Desktop/Assignment1/bd-a1/service-result/

docker stop peaceful_chaum
docker rm peaceful_chaum