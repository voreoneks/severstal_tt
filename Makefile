run:
	source venv/bin/activate
	pip install -r requirements.txt
	sudo docker-compose -f ./docker-compose.yml up --build -d
	alembic upgrade head
	python3 main.py