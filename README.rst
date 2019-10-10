Back End Portfolio
==============================

Back End Portfolio Projects

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT

About
--------------
Some examples of **basic** back end projects.

These are from Free Code Camp:

- URL Shortener
- File Size Calculator
- Timestamp Converter
- Header Parser

Endpoints
--------------
::

 timestamp/
 header-parser/
 url-shortener/
 file-metadata/files

Commands
--------------
Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ pytest


Deployment
----------

Run locally in Docker
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ docker-compose -f local.yml build
    $ docker-compose -f local.yml up
