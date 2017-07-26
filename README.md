# Django REST Kickstart

A *slightly* opinionated starting point for creating JSON API using Django, Django Rest Framework, PostgreSQL.

**Note: Python 1 is not supported.**


## What's inside

### JWT Auth
- `/api/token/`
- `/api/token/verify/`
- `/api/token/refresh/`

### users app with
- `/api/users/`
- `/api/users/{id}/`

### things app with
- `/api/things/`
- `/api/things/{id}/`

### Scalable primary keys

All primary keys are 64 bit integers generated by [simpleflake][simpleflake]. API serves primary keys as strings to work around possible client constraints, for instance, [JavaScript's Number.MAX_SAFE_INTEGER][MAX_SAFE_INTEGER]

Checkout the source code for,
- `helpers.models.BaseModel` implements simpleflake primary keys for models, in addition to providing some common fields.
- `helpers.serializers.BaseModelSerializer` implements conversion of simpleflake primary keys to strings.

### Filtering

[django-filter][djfilter] filter backend is integerated.

### [12 factor][12factor] settings, read from environment variables

See [django12factor][d12f] for more details.

Making settings available as environment variables is not, and should not be, a part of the API application itself. I use [direnv][direnv] during local development, you may use a differnt way to supply configuration.


## Usage

I am using [pipenv][pipenv] to create/manage virtualenvs. Install it, read the docs before proceeding.

Once pipenv is installed, 

```
git clone https://github.com/mnazim/django-rest-kickstart.git myproject
cd myproject
rm -rf .git
pipenv --three
pipenv install -d
pipenv shell
```


Provide following settings via environment variables.

- `DEBUG`
- `SECRET_KEY`
- `ALLOWED_HOSTS`
- `DATABASE_URL` as expected by [dj-database-url][djdburl]

and the rest is just Django,
```
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

*Happy hacking!*

[pipenv]:https://github.com/kennethreitz/pipenv
[simpleflake]:https://pypi.python.org/pypi/simpleflake
[MAX_SAFE_INTEGER]:https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER
[djfilter]:http://django-filter.readthedocs.io
[12factor]:https://12factor.net
[d12f]:https://django12factor.readthedocs.io
[direnv]:https://direnv.net/
[djdburl]:https://github.com/kennethreitz/dj-database-url
