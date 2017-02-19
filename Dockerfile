FROM daocloud.io/python:3.6
MAINTAINER gzMichael <michaelch@126.com>

RUN mkdir -p /app
COPY . /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD python /app/run.py runserver --host 0.0.0.0

EXPOSE 5000

