## How to deploy the project to web server?

Before deployment, make sure both Git and the Heroku CLI are installed. </br>
Create 2 app on Heroku, which prepares Heroku to receive your source code. One for website, another for telegram bot. For example: pkobsystemhelloworld and pkobhelloworldbot. </br>
Make a Procfile, a text file in the root directory of your application, to explicitly declare what command should be executed to start your app. Write this in Procfile.
````
bot: python telegrambot.py
web: gunicorn PKOB.wsgi
````
Make a requirements.txt through which heroku will install the dependencies to make our bot work. Then install these.
````
pip install python-telegram-bot
pip install psycopg2
pip install gunicorn
````
Update the requirements.txt
````
pip freeze > requirements.txt
````
Use the heroku login command to log in to the Heroku CLI. A new window will be opened in your browser prompting you to login, so just click on the button.
````
heroku login
heroku git:remote -a YourAppName
git remote
````
update the PKOB/setting.py
````
ALLOWED_HOSTS = ['127.0.0.1','YourAppName.herokuapp.com']
````
Push to Heroku. First, add the modified files to the local git repository. Then, commit the changes to the repository. Lastly, pushes everything to the server.
````
git add .
git commit -m "update setting.py"
git push heroku main
````
The application is now deployed. Run this if the static folder is not configured. After that run again the ```git push heroku main```.
````
heroku config:set DISABLE_COLLECTSTATIC=1
````
Now, set the Heroku Postgres. Get the Host, Database, User, Port, Password from heroku->YourAppName->Resources->Add-ons->Heroku Postgres->Settings->View Credentials->copy the all the information. After that, go to PKOB/settings.py and update. Below are the example.
````
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'e3mgfdgqkkflfo',
        'USER': 'fwwzdfdufrdlqf',
        'PASSWORD': 'jc7c53ddfghj3a7f4e97e5be6102ertyu8c1d2d76694f99dsaqw3ce0f35eb63a',

        'HOST': 'ec2-72-21-200.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
````
After updated, run again the commands of Database Migration.
````
python manage.py makemigrations App_Soc
python manage.py migrate
````
Then, run again the commands of Push to Heroku. Website push to master while Telegram Bot push to main.
````
git add .
git commit -m "update setting.py"
git push heroku master
git push heroku main
````
To use the free Dynos, go to heroku->YourAppName->Resources->Free Dynos->Edit Dynos Formation->open->confirm.</br>
To connect the database, get the postgres link from heroku->YourAppName->Resources->Add-ons->Heroku Postgres->Settings->View Credentials->copy the postgresql URI link. And then paste in bot.py file </br>
Run the standard Django manage.py migrate to create the tables.
````
heroku run python manage.py migrate
````
## YouTube Presentation
Code Band. (2020, April 15). How to Deploy Django Project on Heroku for Free | Step by Step Tutorial by Code Band [Video]. YouTube.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.youtube.com/watch?v=V2rWvStauak  

Code Yogi. (2021, June 4). Create and Deploy telegram bot using python | telegram bot development | mini projects python | [Video]. YouTube.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.youtube.com/watch?v=d-5rufLCdFM  
