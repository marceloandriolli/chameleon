# Chameleon
Create custom data models for business easily


### Dependences ###

* Python 3.7+

Install Pyenv:
https://github.com/pyenv/pyenv#installation

Intall virtualenv for Pyenv:
https://github.com/pyenv/pyenv-virtualenv


Create and active a virtual environment.

```
pyenv install 3.7.0a3
pyenv virtualenv 3.7.0a3 venv
pyenv activate venv
```

### Setup database

* You need to create a databaes and user in PostgreSQL:

Create database: `createdb back-to-feature-db`
Create user: `createuser -P -s deLorean_admin`

* Create environment variables:
```
cp contrib/env-sample .env
```