# Demo Project Django

## Project structure

```bash
|----demo [Main app]
|----drf [App with demo work]
|----static [js, css files]
|--readme.md
|--requirements.txt
|--manage.py

```

## Setup

1. Create a virtual environment  `python -m venv .venv`
2. Activate virtual environment `.venv\Scripts\activate` (Windows) | `source .venv/bin/activate` (Linux, Mac)
3. Create migrations `python manage.py makemigrations ` 
4. Migrate to database  `python manage.py migrate`
5. Run server `python manage.py runserver`

## URLs

### HTML Pages

- ` /` home page
- `/logs`  logs page
- `/admin` admin panel

### DRF API

- `GET     /api/` Get All user objects
- `POST    /api/` Create a new user object
- `GET     /api/{pk}/` Get  single user object
- `PUT     /api/{pk}/` Update single user object
- `DELETE  /api/{pk}/` Delete user object

## Dependencies

- Django + DRF
- HTML + CSS + JS
- jQuery
- Bootstrap