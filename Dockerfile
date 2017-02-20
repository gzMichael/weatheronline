FROM python:3-onbuild

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app

EXPOSE 80

ENTRYPOINT ["./python","run.py"]