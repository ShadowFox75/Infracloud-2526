#!/bin/bash
mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static
cp weather_docker.py tempdir/
cp -r templates/* tempdir/templates/
cp -r static/* tempdir/static/
echo "FROM python:latest" > tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY weather_docker_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/weather_docker_app.py" >> tempdir/Dockerfile
cd tempdir
docker build -t weatherapp .
docker run -t -d -p 5050:5050 --name weatherrunning weatherapp
docker ps -a