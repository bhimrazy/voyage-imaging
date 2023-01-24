# Voyage Imaging

## Installation and Setup

It is supposed that you open this repo in github codespace or gitpod.

```
    # create a .env file from .env.example
    $ cp .env.example .env

    # step 1 : start docker
    docker-compose up -d # ( "-d" in detached mode, remove "-d" for non detached mode)

    # check ip of database container
    $ docker inspect postgres_voyage_imaging # "IPAddress": "172.20.0.3", find something like this

    #open env.py under alembic
    # and change the ip under DATABAL to current  , leave it if the ip is same

    # migrate to db
    $ alembic upgrade head


```

## Project Structure

```
    .
    ├── alembic/            alembic database migrations
    ├── src/                main app logic with MVC, etc
    │   └── main.py
    ├── tests/              tests
    ├── manage.py           manager script
    ├── requirements.txt
    ├── alembic.ini
    └── README.md

```

## Authors

## Resources

<!--
   #create a python environment
    $ python -m venv venv
    #activate environment
    $ source venv/bin/activate # use venv/Scripts/activate for windows
    #install packages from requirements.txt file
    $ pip install -r requirements.txt

    # Run app
    $ uvicorn src.main:app --reload # dev
    $ uvicorn src.main:app # prod

    # Run test and coverage
    $ pytest
    $ coverage run -m pytest
    $ coverage report -i

    # Run flake8
    $ flake8

    # alembic migrations
    $ alembic revision --autogenerate -m "initial ....  migraion"

    -->
