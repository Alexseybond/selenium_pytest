FROM python:3.11.1-alpine

LABEL "Creator"="Aleksey Bondarovich"

ADD . .

WORKDIR /tests_project/

COPY . /tests_project/

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV ENV=dev

CMD python -m pytest -s -v
