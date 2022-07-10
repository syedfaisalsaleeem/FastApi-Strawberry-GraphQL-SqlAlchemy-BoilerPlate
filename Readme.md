<h1> Fast Api Strawberry GraphQL Async SQL Alchemy Boiler Plate </h1>

Description
--------

This code is a boiler plate for the implementation of GraphQL with Fast Api using Strawberry Library.
For GraphQL server we have used Strawberry.

Features
--------

- Async Connection of SQL Alchemy with POSTGRESQL DataBase

- CRUD Operations of GraphQL using Strawberry Library

- Written Test Cases using Pytest to test GraphQL endpoints

- Directory Struture for GraphQL

- Get the data only from the columns using SQL Alchmey which are specified in GraphQL Query

- Deployment using Docker Container through Docker Compose file

- Deployed code at specific endpoint to test GraphQL

Installation
------------

To run the project in your local environment::

  1. Clone the repository::

        $ git clone https://github.com/syedfaisalsaleeem/FastApi-Strawberry-GraphQL-SqlAlchemy-BoilerPlate.git
        $ cd FastApi-Strawberry-GraphQL-SqlAlchemy-BoilerPlate

  2. Create and activate a virtual environment::

        virtualenv env -p python3
        source env/bin/activate

  3. Install requirements::

        pip install -r requirements.txt

  4. Run the application::

        python main_dev.py

To run the project using Docker Container:

  1. Clone the repository::

        git clone https://github.com/syedfaisalsaleeem/FastApi-Strawberry-GraphQL-SqlAlchemy-BoilerPlate.git
        cd FastApi-Strawberry-GraphQL-SqlAlchemy-BoilerPlate

  2. Run this command on CMD::

        docker-compose up -d --build

Usage Examples
--------------

Launch the fast api server at specified port default 5000 (open the UI at http://localhost:5000/graphql): ::

    $ python main_dev.py

Launch using docker: ::

    $ docker-compose up -d --build

Tests
-----

Test are run with *pytest*. If you are not familiar with this package you can get some more info from `their website <https://pytest.org/>`_.

To run the tests, from the project directory, simply::

    pip install -r requirements.txt
    python test.py

You should see output similar to::

    .............................................
    ----------------------------------------------------------------------
    Ran 102 tests in 13.132s

    OK

If you have any question about this opinionated list, do not hesitate to contact me [@SyedFaisal](https://www.linkedin.com/in/syedfaisalsaleem/) on Linkedin or open an issue on GitHub.
