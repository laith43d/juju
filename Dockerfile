FROM python:3.6-slim

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends

RUN mkdir /app
WORKDIR /app

RUN pipenv install

COPY . .
RUN pipenv install -e .

LABEL maintainer="Layth Zahid <L@LZAH.online>"

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "app:main"
