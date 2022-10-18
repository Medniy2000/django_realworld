Django Real World
====================

Django Real World description

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

Run app local
^^^^^^^^^^^^^^

To run app local use::

    $ cd <path_to_app_root>
    $ cp .env.example .env

    # to run app perform:
        # install, run postgres, actualize .env

    # install python dependencies:
    $ pip3 install -r requirements/local.txt

    # for local purposes
    $ python manage.py runserver
    $ docker-compose -f docker-compose-local.yml up

    # for production purposes
    $ TODO


API docs here::

    # http://127.0.0.1:8000//api/docs/
    # http://127.0.0.1:8000/api/redoc/


To check code quality[black, flake8, mypy]::

    # use commands

    $ bash beautify.sh

