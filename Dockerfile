FROM python:3.6

RUN mkdir -p /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
COPY qwonline_start.sh /usr/local/bin/qwonline_start.sh
RUN chmod +x /usr/local/bin/qwonline_start.sh

EXPOSE 80

ENTRYPOINT ["qwonline_start.sh"]