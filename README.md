# Eqns

A Django-based Physics equations API.

## How to install

Standard stuff. Copy or clone this whole thing into your Django project as an
app and add the folder to your INSTALLED_APPS in settings.py.

## What is it?

It works using [Django REST Framework](http://www.django-rest-framework.org/)
which can be accessed via `http://<your-domain>/eqns/api/`. It only supports 
`GET` requests now. The only way to add equations is through the Django admin.

To pull the data for a specific equation, use `/eqns/api/equations/1/`. You'll 
get something like:

    {
        "name": "Displacement from constant acceleration (1D)",
        "sympy": "d = v0 * t + Rational(1,2) * a * t**2",
        "latex": "d = v_0 t + \\tfrac{1}{2} at^2",
        "subject": {
            "id": 1,
            "name": "Kinematics",
            "sort_order": 0
        },
        "system": {
            "id": 1,
            "name": "Single particle",
            "sort_order": 0
        },
        "variables": [
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
                "id": 1,
                "unit": {
                    "id": 4,
                    "symbol": "m",
                    "name": "meter",
                    "quantity": "length",
                    "equivalent": ""
                },
                "symbol": "d",
                "name": "Displacement"
            },
            {
                "id": 5,
                "unit": {
                    "id": 3,
                    "symbol": "s",
                    "name": "second",
                    "quantity": "duration",
                    "equivalent": ""
                },
                "symbol": "t",
                "name": "Time"
            },
            {
                "id": 2,
                "unit": {
                    "id": 1,
                    "symbol": "m/s",
                    "name": "meters per second",
                    "quantity": "speed",
                    "equivalent": ""
                },
                "symbol": "v",
                "name": "Velocity"
            },
            {
                "id": 3,
                "unit": {
                    "id": 1,
                    "symbol": "m/s",
                    "name": "meters per second",
                    "quantity": "speed",
                    "equivalent": ""
                },
                "symbol": "v0",
                "name": "Initial velocity"
            }
        ],
        "constants": [],
        "limitations": [
            {
                "id": 1,
                "name": "Constant acceleration",
                "sort_order": 0
            },
            {
                "id": 2,
                "name": "Single dimension",
                "sort_order": 0
            }
        ]
    }
    
Pretty verbose, I know. But it's stanard JSON, so use it how you wish. An
simple example is included as the "home page", `/eqns/`.

## What next?

1. Adding some sort of POST functionality.
2. Use the power of `sympy` to to do some problem solving.
3. Fix the gazillion bugs that are certainly left to be fixed.