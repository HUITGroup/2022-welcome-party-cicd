FROM python:alpine

WORKDIR /app

RUN pip install -U pip

COPY ./*.py ./
COPY ./templates ./templates/
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]