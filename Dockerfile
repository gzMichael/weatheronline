FROM ubuntu:14.04
MAINTAINER gzMichael <michaelch@126.com>

RUN apt-get update && apt-get install -y vim python3 net-tools && \
    rm -rf /var/lib/apt/lists/* && mkdir -p /app
COPY . /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY web_start.sh /usr/local/bin/web_start.sh
EXPOSE 5000

ENTRYPOINT [“/app/web_start.sh"]

