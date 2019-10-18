# Database sever for HIA


## Quickstart

### Local development

This project is built using the Flask web framework. It runs on Python 3.4+.

To run the sever locally follow these steps:

1. Clone this repository and `cd` into `database_sever` folder.

1. Create a new virtual environment and activate it :

    ``
    python3 -m venv venv``

    ``source venv/bin/activate
    ``

1. Install the requirements.

    ``
    pip install -r requirements.txt
    ``

1. Initial the database.

    ``
    python3 manage.py db init
    ``

1. Run the migration.

    ``
    python3 manage.py db migrate -m "initial migration"``

    ``python3 manage.py db upgrade
    ``

1. Start the database server.

    ``
    python3 manage.py runserver -p [portnum]
    ``
