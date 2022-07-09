FROM python:3.8-slim-buster
# Add a work directory
WORKDIR /GraphQL_FastAPI_server
# Cache and Install dependencies
COPY requirements.txt requirements.txt
RUN apt update
RUN apt-get install -y build-essential
RUN apt-get install -y python3-psycopg2
# RUN apt-get install -y python3-pip
RUN apt install -y postgresql postgresql-contrib 
RUN apt install -y python3-dev libpq-dev
RUN apt install -y git
RUN pip3 install -r requirements.txt
COPY . .