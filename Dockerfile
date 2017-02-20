FROM daocloud.io/python:3.6
MAINTAINER gzMichael <michaelch@126.com>

RUN mkdir -p /app
COPY . /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY web_start.sh /usr/local/bin/web_start.sh
EXPOSE 5000

ENTRYPOINT [“/app/web_start.sh"]

