FROM python:3.11.4

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8081

CMD ["uwsgi", "app.ini"]