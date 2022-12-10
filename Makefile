build:
	docker-compose build

console:
	docker-compose run base bash

cassandra:
	docker-compose up -d cassandra

down:
	docker-compose down

list-containers:
	docker ps
