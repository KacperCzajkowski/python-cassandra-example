build:
	docker-compose build

console:
	docker-compose run base bash

cassandra:
	docker-compose up cassandra -d

down:
	docker-compose down

list-containers:
	docker ps