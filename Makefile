up:
	docker compose up

migration:
	alembic revision --autogenerate

migrate:
	alembic upgrade head