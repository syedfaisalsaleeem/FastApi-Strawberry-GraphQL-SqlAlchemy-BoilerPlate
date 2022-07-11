<h1> Fast Api Strawberry GraphQL Async SQL Alchemy Boiler Plate </h1>
<a><img src=https://user-images.githubusercontent.com/49129677/178163601-3ff563a4-67a1-45ca-a3cb-6ea193ca10da.png> </a>

## Description

This code is a boiler plate for the implementation of GraphQL with Fast Api using Strawberry Library.
For GraphQL server we have used Strawberry.

## Features

- Production ready Python web server using Uvicorn and Gunicorn.

- Python <a href="https://github.com/tiangolo/fastapi" class="external-link" target="_blank">**FastAPI**</a> backend

- Async Connection of SQL Alchemy with POSTGRESQL DataBase.

- CRUD Operations of GraphQL using Strawberry Library.

- Written Async Unit Tests using Pytest to test GraphQL queries and mutations.

- Boiler Plate directory struture for GraphQL Python.

- Get the data only from the columns using SQL Alchmey which are specified in GraphQL Query.

- Deployment using Docker Container through Docker Compose file.

- Deployed code at specific endpoint to test GraphQL.

- Alembic migrations.

-  Jenkins (continuous integration).
## Installation

To run the project in your local environment::

  1. Clone the repository::
```
  $ git clone https://github.com/syedfaisalsaleeem/FastApi-Strawberry-GraphQL-SqlAlchemy-BoilerPlate.git
  $ cd FastApi-Strawberry-GraphQL-SqlAlchemy-BoilerPlate
```
  2. Create and activate a virtual environment::
```
  $ virtualenv env -p python3
  $ source env/bin/activate
```
  3. Install requirements::
```
  $ pip install -r requirements.txt
```
  4. Run the application::
```
  $ python main_dev.py
```
To run the project using Docker Container:

  1. Clone the repository::
```
  $ git clone https://github.com/syedfaisalsaleeem/FastApi-Strawberry-GraphQL-SqlAlchemy-BoilerPlate.git
  $ cd FastApi-Strawberry-GraphQL-SqlAlchemy-BoilerPlate
```
  2. Run this command on CMD::
```
  $ docker-compose up -d --build
```
## Usage Examples

Launch the fast api server at specified port default 5000 (open the UI at http://localhost:5000/graphql): ::

    $ python main_dev.py

Launch using docker: ::

    $ docker-compose up -d --build

## Tests

Test are run with *pytest*. If you are not familiar with this package you can get some more info from `their website <https://pytest.org/>`_.

To run the tests, from the project directory, simply::

```
$ pip install -r requirements.txt
$ python test.py
```

You should see output similar to::
```
----------- coverage: platform win32, python 3.8.8-final-0 -----------
Name                                Stmts   Miss  Cover
-------------------------------------------------------
tests\conftest.py                      18      4    78%
tests\graphql\mutations.py              3      0   100%
tests\graphql\queries.py                2      0   100%
tests\graphql\test_stickynotes.py       0      0   100%
tests\graphql\test_user.py             43      0   100%
tests\load_test_env.py                  4      4     0%
-------------------------------------------------------
TOTAL                                  70      8    89%


=================== 8 passed in 0.59s =================
```
## Migrations

To run the project in your local environment::

```
$ alembic revision --autogenerate -m "migration string"
$ alembic upgrade head
```
## License

This project is licensed under the terms of the MIT license. If you have any question about this opinionated list, do not hesitate to contact me [@SyedFaisal](https://www.linkedin.com/in/syedfaisalsaleem/) on Linkedin or open an issue on GitHub.
