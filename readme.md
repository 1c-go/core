## install

**requirements:**
- python 3.7+
- pip
- poetry
- docker (optional)

```shell script
pip install poetry
poetry install --no-dev
```

## launch

```shell script
poetry run python manage.py runserver &
poetry run python manage.py qcluster
```

## docker

```shell script
docker-compose -f docker/docker-compose.yml run backend python manage.py migrate
docker-compose -f docker/docker-compose.yml up -d
```
