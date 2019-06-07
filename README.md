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

Create user: `sudo -u postgres createuser chamaleon_admin `
Create database: `sudo -u postgres createdb -O chamaleon_admin chamaleon-db`


* Create environment variables:
```
cp contrib/env-sample .env
```
