## [MustWatch](https://xanhex.pythonanywhere.com/)

The app that provides you with a collection of must-watch movies
and the opportunity to make your own watch lists. The application can be
accessed through a web interface or REST API using
[mustwatch](https://github.com/xanhex/mustwatch-app/) app.

Website has original design, it's fluid responsive and comes with the dark
theme. Two language support with API: EN/RU.

## Stack

- Python
- Django
- REST API
- SQLite
- Bootstrap
- Unittest

## Standards

- pep8
- flake8
- black
- djlint
- pymarkdown
- OpenAPI

## How to run

1. Clone project from git repository.
2. Create a virtual environment.
3. Install dependencies from `requirements.txt`.
4. Make migrations and run server in root project folder:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

## Authorization

Use the standard authentication method through the website.
For now, only administrators can create content: through  Django admin panel or
through API. Token authorization is available for admins only (see API spec).

## API specification

website_address/redoc/

## Demo

![screenshot](https://github.com/xanhex/mustwatch-django/blob/master/demo.jpg)
