FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
COPY requirement.txt /app/requirement.txt
WORKDIR /app
RUN pip3 install --upgrade pip && pip3 install -r requirement.txt
WORKDIR /app
COPY . /app/
CMD python3 manage.py makemigrations && python3 manage.py makemigrations && python3 manage.py runserver 0.0.0.0:8000