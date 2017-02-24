FROM python:3-onbuild

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app

EXPOSE 5000

CMD ["python","./run.py --runserver 0.0.0.0"]