run:
	sudo docker-compose -f ./docker-compose.yml up --build -d
	alembic upgrade head
	python3 main.py