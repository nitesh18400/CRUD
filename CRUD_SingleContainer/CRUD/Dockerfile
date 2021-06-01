FROM ubuntu
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y software-properties-common
RUN apt-get -y install mysql-server libmysqlclient-dev
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install Django==3.1.3 PyMySQL==1.0.2

RUN mkdir /app
WORKDIR /app
COPY . /app/
CMD python3 manage.py makemigrations && python3 manage.py makemigrations && python3 manage.py runserver 0.0.0.0:8000 && mysql -h localhost -P 3306 --protocol=tcp -u root && service mysql restart
# ENTRYPOINT service ssh restart && bash