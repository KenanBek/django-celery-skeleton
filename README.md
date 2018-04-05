# django-celery-skeleton

Django and Celery skeleton project.

## Versions

App | Version
--- | ---
Python | 2.7.12
Django | 1.11.11
Celery | 4.1.0

# Project structure

    django-celery-skeleton/
    |---src                                     # django project folder
    |   |---dcs                                 # django root configuration
    |   |   |---settings.py
    |   |   |---urls.py
    |   |   |---wsgi.py
    |   |   |---celeryconf.py
    |   |---files
    |   |   |---tempaltes                       # view templates
    |   |   |   |---index.html
    |   |   |---media                           # images, sized cache and placeholder
    |   |   |   |---.gitignore
    |   |   |   |---placeholder.png
    |   |   |   |---README.md
    |   |   |---static
    |   |   |   |---placeholder.png
    |   |   |---README.md
    |   |---manage.py
    |---.gitignore
    |---.dockerignore
    |---Vagrantfile
    |---Dockerfile
    |---docker-compose.yml
    |---requirements.txt
    |---README.md

# Run from local machine

    python manage.py runserver
    celery -A core worker -l info
