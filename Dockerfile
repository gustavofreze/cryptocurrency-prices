FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apk update && apk add --no-cache bash \
    && rm /var/cache/apk/*

RUN python -m pip install --upgrade pip -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/app"
