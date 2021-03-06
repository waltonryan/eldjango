# El Django | A Python/Django Starter App. #
Get your project up and running. Quickly. Supports <a href="http://compass-style.org">Compass</a>, <a href="http://sass-lang.com">Sass</a> and <a href="http://lesscss.org">Less</a>. Uses <a href="http://twitter.github.io/bootstrap/">Bootstrap</a>, <a href="http://mandrill.com/">Mandrill</a>, <a href="http://www.django-userena.org/">django-userena</a> and <a href="https://github.com/brack3t/Djrill">djrill</a>. Designed for use with <a href="https://devcenter.heroku.com/articles/django">Heroku</a>.

See the app in <a href="http://www.eldjango.com">Action</a>. It'll take a few seconds to load due to its development settings.

## Why is El Django so Great ##

* Get your app running in about 30 minutes
* Full login/signup and edit profile settings support via django-userena, which includes email confirmations via Mandrill SMTP
* Fully functional SMTP functionality via Mandrill
* Twitter Bootstrap ready (as Less and compiled files)
* Sass ready
* Less ready
* Compass ready (config.rb file included)
* Working DB submission form (to log data into your db)
* Working Contact Us form submitted via Mandrill

## Before You Get Started ##

Depending on your needs, you might want to make sure you've properly installed a few things: 

* <a href="http://python.org/">Python</a>. <a href="http://docs.python-guide.org/en/latest/starting/install/osx/">Python for Mac</a>.
* <a href="https://toolbelt.heroku.com/">Heroku Toolbelt</a>
* <a href="https://pypi.python.org/pypi/virtualenv">Virtualenv</a>

A lot of the setup instructions come from <a href="https://devcenter.heroku.com/articles/django">Django on Heroku</a>. It's a really great resource.

Here are the requirements, the installation of which are described more fully below:

	Django==1.5.1
	distribute==0.6.34
	dj-database-url==0.2.1
	gunicorn==0.17.2
	psycopg2==2.5
	wsgiref==0.1.2
	mandrill>=1.0.6
	djrill==0.4.0
	django-userena==1.2.0
	django-guardian==1.1.0.beta
	PIL>=1.1.7

## Installation ##

Clone the source code, typically in a projects directory (e.g., /Users/your/path/Projects):
	
	$ git clone https://github.com/waltonryan/eldjango.git

Get into the cloned project:

	$ cd eldjango
	
Distribute your virtual environment (see <a href="https://devcenter.heroku.com/articles/django">here</a> for additional details):

	$ virtualenv venv --distribute
	New python executable in venv/bin/python
	Installing distribute...............done.
	Installing pip...............done.
	
	$ source venv/bin/activate
	
Install Flask gunicorn:
	
	$ pip install Flask gunicorn
	
Install the other necessary dependencies (may be altered depending on your preferences. For instance, you can choose which db you want to use):

	$ pip install Django psycopg2 gunicorn dj-database-url

Install django-userena (see <a href="http://docs.django-userena.org/en/latest/installation.html#installing-django-userena">here</a> for details):

	$ pip install django-userena
	
Install djrill (see <a href="https://github.com/brack3t/Djrill">here</a> for details):

	$ pip install djrill
	
Create your app on Heroku:

	$ heroku create
	Creating simple-spring-9999... done, stack is cedar
	http://simple-spring-9999.herokuapp.com/ | git@heroku.com:simple-spring-9999.git
	Git remote heroku added
	
This creates a git remote for heroku called 'heroku'.

Add your database to Heroku:

	$ heroku addons:add heroku-postgresql:dev

Get your new db credentials by logging into Heroku, going to your <a href="https://dashboard.heroku.com/apps">App</a> (e.g., afternoon-plains-1234) and clicking on "Heroku Postgres Dev". Once there, go to "Connection Settings:Django". Open your /eldjango/mysite/settings.py file and paste in your database credentials. You can alternatively locate your credentials following <a href="https://devcenter.heroku.com/articles/heroku-postgresql">these steps</a>:

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
		'/Users/to/your/path/eldjango/css',
		'/Users/to/your/path/eldjango/js',
		'/Users/to/your/path/eldjango/img',
		'/Users/to/your/path/eldjango/static',
	    # Put strings here, like "/home/html/static" or "C:/www/django/static".
	    # Always use forward slashes, even on Windows.
	    # Don't forget to use absolute paths, not relative paths.
	)

Add Mandrill to your Heroku app:

	$ heroku addons:add mandrill:starter
	
Get your Mandrill API Key and paste it into your /eldjango/mysite/settings.py file:

	$ heroku config:get MANDRILL_APIKEY
	af5xxxxx-xxxx-xxxx-xxxx-dexxxxxxxxxx

Like so:

	MANDRILL_API_KEY = 'af5xxxxx-xxxx-xxxx-xxxx-dexxxxxxxxxx'
	
Add the email address you'd like to use for Mandrill. Heroku provides you with an email address that you may use if you like. Add the email address to the /eldjango/mysite/settings.py file:

	DEFAULT_FROM_EMAIL = 'your email address here' (example@address.com)
	
If you'd like, get a <a href="http://www.google.com/analytics/">Google Analytics</a> key and paste it into your /eldjango/mysite/settings.py file:

	GOOGLE_TRACKING_ID = 'UA-XXXXXXXX-X'
	
Make sure you install python-PIL. For <a hrf="http://pythonmac.org/packages/py25-fat/index.html">Mac</a>. This can cause the error "No module named Image". <a href="http://stackoverflow.com/questions/2485295/the-problem-with-installing-pil-using-virtualenv-or-buildout">This</a> could work for you:

	$ pip install --no-index -f http://dist.plone.org/thirdparty/ -U PIL

Make sure that you <code>check permissions</code> as instructed by the <a href="http://docs.django-userena.org/en/latest/commands.html#commands">django-userena documentation</a>. This is because we are not starting eldjango from scratch. This will usually do the trick:

	$ heroku run python manage.py check_permissions
	
Sync your database models to the heroku db you created earlier:

	$ heroku run python manage.py syncdb
	
If prompted, create your superuser account and write down the credentials in a handy place.
	
Commit your changes to git and push your new app to Heroku:

	$ git add .
	$ git commit -m "add app specific settings in settings.py"
	$ git push heroku master
	
Alright, check out your new site! You now should now have a fully functioning app on both your local environment and on Heroku:

	$ heroku open
	*Opening simple-spring-9999.herokuapp.com... done*
	
Let me know if you have any questions at ryang24@gmail.com. Happy app making!

	
	

	


	

	

	

	

