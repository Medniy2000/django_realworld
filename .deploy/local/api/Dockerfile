FROM python:3.9.12
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install --upgrade pip
RUN pip install -r requirements/local.txt
