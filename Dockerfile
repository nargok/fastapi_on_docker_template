FROM python:3.9-buster

RUN mkdir /app
WORKDIR /app

COPY main.py main.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD uvicorn main:app --host "0.0.0.0" --reload