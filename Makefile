all:
	docker compose up --build

down:
	docker compose down

clean:
	docker compose down -v

prune: clean
	docker system prune -a --volumes

stop:
	docker compose stop

restart:
	docker compose up --remove-orphans
	docker compose down
	docker compose up --build

migrations:
	docker compose run django python manage.py makemigrations core

migrate:
	docker compose run django python manage.py migrate

createsuperuser:
	docker compose run django python manage.py createsuperuser

showmigrations:
	docker compose run django python manage.py showmigrations

jedi:
	docker stop $$(docker ps -aq) 2>/dev/null || true
	docker rm $$(docker ps -aq) 2>/dev/null || true
	docker rmi -f $$(docker images -q) 2>/dev/null || true
	docker volume rm $$(docker volume ls -q) 2>/dev/null || true
	docker network rm $$(docker network ls -q | grep -v 'bridge\|host\|none') 2>/dev/null || true

sith:
	docker stop $$(docker ps -aq) 2>/dev/null || true
	docker rm $$(docker ps -aq) 2>/dev/null || true
	docker system prune -a --volumes -f 2>/dev/null || true
	rm -rf ./data

re: down all
