FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

RUN pip install poetry \
  && apt update \
  && apt install -y git

WORKDIR /app
COPY pyproject.toml .
COPY poetry.lock .

RUN poetry conf settings.virtualenvs.create false \
  && poetry install \
  && apt autoremove -y git \
  && rm -rf ~/.cache/pypoetry/cache/repositories/pypi/* \
  && rm -rf ~/.cache/pip \
  && rm -rf /var/lib/apt/lists/*

COPY . .


EXPOSE 8000
CMD ["python", "manage.py", "runserver_plus", "0.0.0.0:8000"]
