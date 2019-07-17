FROM python:3.7-slim-stretch
MAINTAINER Toomas Ormisson

COPY ./ /app
WORKDIR /app

RUN pip install .

EXPOSE 5000

CMD ["fpl-exporter", "-v"]
