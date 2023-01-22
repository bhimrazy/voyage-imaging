# Voyage Imaging

## Installation and Setup

```
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
