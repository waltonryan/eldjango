# El Django | A Python/Django Starter App. #
Get your project up and running. Quickly. Supports Compass, Sass and Less. Uses Bootstrap, Mandrill, django-userena and djrill. Designed for use with Heroku.

## Before you get started, depending on your needs, you might want to look make sure you've properly installed a few things: ##

* <a href="http://python.org/">Python</a>. <a href="http://docs.python-guide.org/en/latest/starting/install/osx/">Python for Mac</a>.
* <a href="https://toolbelt.heroku.com/">Heroku Toolbelt</a>
* <a href="https://pypi.python.org/pypi/virtualenv">Virtualenv</a>

See requirements.txt for list of requirements. A lot of the setup instructions come from <a href="https://devcenter.heroku.com/articles/django">Django on Heroku</a>. It's a great resource.

## Installation ##

Clone the source code, typically in a projects directory (e.g., /Users/your/path/Projects):
	
	$ git clone https://github.com/waltonryan/eldjango.git
	$ cd eldjango
	
Distribute your virtual environment (see <a href="https://devcenter.heroku.com/articles/django">here</a> for details):

	$ virtualenv venv --distribute
	*New python executable in venv/bin/python*
	*Installing distribute...............done.*
	*Installing pip...............done.*
	
	$ source venv/bin/activate
	
Install flask gunicorn:
	
	$ pip install Flask gunicorn
	
Install the necessary dependencies (may be altered depending on your preferences - like what db you want to use):

	$ pip install Django psycopg2 gunicorn dj-database-url

Install django-userena (see <a href="http://docs.django-userena.org/en/latest/installation.html#installing-django-userena">here</a> for details):

	$ pip install django-userena
	
Install djrill (see <a href="https://github.com/brack3t/Djrill">here</a> for details):

		$ pip install djrill
	
Create your app on Heroku:

	$ heroku create
	*Creating simple-spring-9999... done, stack is cedar*
	*http://simple-spring-9999.herokuapp.com/ | git@heroku.com:simple-spring-9999.git*
	*Git remote heroku added*
	
This create a git remote for heroku called 'heroku'.

Add your database to Heroku:

	$ heroku addons:add heroku-postgresql:dev

Get your new database credentials by logging into Heroku, going to your new app (e.g., afternoon-plains-1234) and clicking on "Heroku Postgres Dev". Once there, go to "Connection Settings:Django". Open your /eldjango/mysite/settings.py file and paste in your database credentials:

	DATABASES = {
	  'default': {
	    'ENGINE': 'django.db.backends.postgresql_psycopg2',
	    'NAME': 'XXXXXXXXXXXXX',
	    'HOST': 'XXXXXXXXXXXXX.compute-1.amazonaws.com',
	    'PORT': 5432,
	    'USER': 'XXXXXXXXXXXX',
	    'PASSWORD': 'XXXXXXXXXXXXX'
	  }
	}
	
In your /eldjango/mysite/settings.py file, update your STATICFILES_DIRS to your path structure: 

	STATICFILES_DIRS = (
		'/Users/*to/your/path*/eldjango/css',
		'/Users/*to/your/path*/eldjango/js',
		'/Users/*to/your/path*/eldjango/img',
		'/Users/*to/your/path*/eldjango/static',
	    # Put strings here, like "/home/html/static" or "C:/www/django/static".
	    # Always use forward slashes, even on Windows.
	    # Don't forget to use absolute paths, not relative paths.
	)

Add Mandrill to your Heroku app:

	$ heroku addons:add mandrill:starter
	
Get your Mandrill API Key and paste it into your /eldjango/mysite/settings.py file:

	$ heroku config:get MANDRILL_APIKEY
	*af5xxxxx-xxxx-xxxx-xxxx-dexxxxxxxxxx*
	
	MANDRILL_API_KEY = '*mandrill api key here*'
	
Add the email address you'd like to use for Mandrill. Heroku give you an email address to use if you like:

	DEFAULT_FROM_EMAIL = 'your email address here' (example@address.com)
	
If you'd like, get a Google Analytics key and paste it into your /eldjango/mysite/settings.py file:

	GOOGLE_TRACKING_ID = 'UA-XXXXXXXX-X'
	
Make sure you install python-PIL. For <a hrf="http://pythonmac.org/packages/py25-fat/index.html">Mac</a>

You'll need to make sure that you check permissions, as described by the <a href="http://docs.django-userena.org/en/latest/commands.html#commands">django-userena documentation</a>. This is because we are not starting django-userena from scratch:

	$ heroku run python manage.py check_permissions
	
Sync your database models to the heroku db you created:

	$ heroku run python manage.py syncdb
	
If prompted, create your superuser account and write down the credentials in a handy place.
	
Commit your changes to git. Push your new app to Heroku:

	$ git add .
	$ git commit -m "add app specific settings in settings.py"
	$ git push heroku master
	
Alright, check out your new site! You now should have a fully functioning app:

	$ heroku open
	*Opening simple-spring-9999.herokuapp.com... done*
	
You should be ready to go. Let me know if you have any questions at ryang24@gmail.com.

	
	

	


	

	

	

	

