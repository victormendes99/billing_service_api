.PHONY: build run run-test

build: 
	docker-compose build

run: 
	docker-compose run --rm --name billing_service_api --service-ports billing_service_api

run-test:
	pytest ./tests

run-unit-test:
	pytest ./tests/unit

run-integration-test:
	pytest ./tests/integration

migration:
	docker exec billing_service_api alembic revision --autogenerate

migrate:
	docker exec billing_service_api alembic upgrade head