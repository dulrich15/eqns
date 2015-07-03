# Eqns

A Django-based Physics equations API.

## What is it?

It works using [Django REST Framework](http://www.django-rest-framework.org/).
The API can be accessed via `http://<your-domain>/eqns/api/`. It only supports 
`GET` requests now. The only way to add equations is through the Django admin.

To pull the data for a specific equation, use `GET /eqns/api/equations/2/`. 
You'll get something like:

    {
        "name": "Newton's second law",
        "sympy": "F = m * a",
        "latex": "F = ma",
        "subject": {
            "id": 2,
            "name": "Dynamics",
            "sort_order": 0
        },
        "system": {
            "id": 1,
            "name": "Single particle",
            "sort_order": 0
        },
        "variables": [
            {
                "id": 6,
                "unit": {
                    "id": 5,
                    "symbol": "N",
                    "name": "newton",
                    "quantity": "force",
                    "equivalent": "kg-m/s2"
                },
                "symbol": "F",
                "name": "force"
            },
            {
                "id": 4,
                "unit": {
                    "id": 2,
                    "symbol": "m/s2",
                    "name": "meters per second squared",
                    "quantity": "acceleration",
                    "equivalent": ""
                },
                "symbol": "a",
                "name": "Acceleration"
            },
            {
                "id": 7,
                "unit": {
                    "id": 6,
                    "symbol": "kg",
                    "name": "kilogram",
                    "quantity": "mass",
                    "equivalent": ""
                },
                "symbol": "m",
                "name": "mass"
            }
        ],
        "constants": [],
        "limitations": []
    }    

Pretty verbose, I know. But it's stanard JSON, so use it how you wish. An
simple example is included as the "home page", `/eqns/`.

## How to install?

Standard stuff. Copy or clone this whole thing into your Django project as an
app. Add the folder to your INSTALLED_APPS in settings.py. Run `syncdb` to
set up your database, etc.

## What next?

1. Adding some sort of POST functionality.
2. Use the power of `sympy` to to do some problem solving.
3. Fix the gazillion bugs that are certainly left to be fixed.