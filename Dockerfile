FROM python:3.6

RUN mkdir -p /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN chmod +x /app/qwonline_start.sh

EXPOSE 80

ENTRYPOINT ["/app/qwonline_start.sh"]