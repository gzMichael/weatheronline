FROM ubuntu:14.04
MAINTAINER gzMichael <michaelch@126.com>

RUN apt-get update && apt-get install -y python3 python-pip python-dev build-essential net-tools && \
    rm -rf /var/lib/apt/lists/* && mkdir -p /app
COPY . /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY web_start.sh /usr/local/bin/web_start.sh
EXPOSE 5000

ENTRYPOINT [“/app/web_start.sh"]

