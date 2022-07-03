
## How to install requirements.txt
```
$ pip3 install -r requirements.txt
```

## How to update requirements.txt
````
$ pip3 freeze > requirements.txt
````

## How to create new App
````
$ python3 manage.py startapp App_Soc
````

## How to migrate database
````
$ python3 manage.py showmigrations
$ python3 manage.py makemigrations
$ python3 manage.py makemigrations App_Soc
$ python3 manage.py migrate
````

## How to create Super User
````
$ python3 manage.py createsuperuser
````

## How to reverse migration
````
$ python3 manage.py migrate App_Books 0002 (reverse)
$ python3 manage.py migrate App_Books zero (reverse all)
````

## How to reset migration
````
$ pip3 install django-reset-migrations
$ python3 manage.py migrate --fake-initial
$ python3 manage.py migrate --fake
$ python3 manage.py migrate --fake App_Books zero
````

## How to install gunicorn
````
$ pip3 install gunicorn
````

## How to install Heroku CLI (for MacOS only)
````
$ brew install heroku/brew/heroku
````

## How to login and create git remote
````
$ heroku login
$ heroku git:remote -a pkob
$ git remote
````

## How to push to Heroku
````
$ git add .
$ git commit -m "update setting.py"
$ git push heroku master
````

## How to configure the static folder
````
$ heroku logs --tail
$ heroku config:set DISABLE_COLLECTSTATIC=1
````

## How to install python telegram bot
````
$ pip3 install python-telegram-bot
````

## How to install psycopg2
````
$ pip3 install psycopg2
````

## How do switch branches from master to main
To switch the default branch used to deploy apps from master to main, first create a new branch locally:
````
$ git checkout -b main
````
Next, delete the old default branch locally:
````
$ git branch -D master
````

## How to push to Heroku main
````
$ git push heroku main
````

## How to run the standard Django manage.py migrate to create the tables
````
$ heroku run python manage.py migrate
````
