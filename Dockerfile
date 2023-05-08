FROM python:3.9-alpine3.16
WORKDIR /usr/src
COPY requirements.txt /usr/src/requirements.txt

#env
ENV PYTHONDONTWRITEBYECODE 1
ENV PYTHONBUFFERED 1

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
COPY ./ /usr/src
