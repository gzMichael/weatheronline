FROM python:3.6

RUN mkdir -p /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python","run.py"]