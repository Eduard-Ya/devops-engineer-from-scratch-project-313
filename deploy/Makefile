.PHONY: run install clean test lint format ci docker-build docker-run docker-run-sentry


PORT ?= 8080
HOST ?= 0.0.0.0

# Зависимости			
install:
	uv sync

# Запуск приложения
run:
	uv run python main.py


# Запуск тестов
test:
	PYTHONPATH=. uv run pytest tests/ -v


# Линтер
lint:
	uv run ruff check .


# Автоформат
format:
	uv run ruff format .
	uv run ruff check --fix .


# Очистка кеша
clean:
	rm -rf .venv
	rm -rf .uv
	rm -rf __pycache__
	rm -rf .pytest_cache


# формат линт тест
ci:
	make format
	make lint
	make test


# сборка образа
docker-build:
	docker build -t devops-example-app .


# запуск без Sentry
docker-run:
	docker run -p 8080:8080 -e PORT=8080 devops-example-app


# запуск с Sentry
docker-run-sentry:
	docker run -p 8080:8080 \
		-e PORT=8080 \
		-e SENTRY_DSN=$(SENTRY_DSN) \
		devops-example-app