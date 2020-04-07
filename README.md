### Getting Started

Create and activate a virtual environment, and then install the requirements.

### Set Environment Variables

Update config.py


You can alter the `APP_SETTINGS` environment variable for shifting prod and dev settings in .env file.


### DB Commands

```sh
$ python manage.py create-db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python manage.py create-admin
$ python manage.py create-data
```

### Run the Application

```sh
$ python manage.py run
```

Access the application at the address [http://localhost:5000/](http://localhost:5000/)

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```

Run flake8 on the app:

```sh
$ python manage.py flake
```

or

```sh
$ flake8 project
```

### Running Celery Worker

```sh
$ celery worker -A celery_app
```
