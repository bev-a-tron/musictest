#MusicTest
[![Build Status](https://travis-ci.org/asifrc/musictest.svg?branch=master)](https://travis-ci.org/asifrc/musictest)

This is a README file for musictest.

Five audio clips, played at random.
The user is instructed to listen to the clips
and indicate:
1. whether he/she recongizes the piece
2. the name of the composer (+confidence)
3. the name of the piece (+confidence)

The data will be saved to a text file,
using the user's name and age for the file name.

##Local Configuration
1. Install postgresql and make sure it is running
2. Install [virtualenv](https://virtualenv.pypa.io/en/latest/virtualenv.html)
3. Start the virtual environment
```
virtualenv venv  
$ source venv/bin/activate
```
4. Install dependencies
```
(venv) $ pip install -r requirements.txt
```

###Run the Tests
```
(venv) $ nosetests
```

###Run the Application
There are three ways you can run the application. Heroku uses Foreman, which
is configured by the Procfile. Gunicorn is the server used by the Procfile. And
python is.. python.
####Foreman (requires Ruby)
1. Install [foreman](https://github.com/ddollar/foreman)
```
(venv) $ gem install foreman
```
2. Start application with foreman (the same command heroku runs)
```
(venv) $ foreman start
```

####Gunicorn
```
(venv) $ gunicorn application:app
```

####Python
```
(venv) $ python application.py
```

##Continuous Integration & Continuous Deployment
The repository is currently configured to use Travis-CI as the Continuous
Integration server and then uses Travis to deploy successful builds of the master
branch to Heroku.

###Heroku Configuration
####Add the Heroku Postgres Add-on
Log in to your account and go [here](https://addons.heroku.com/heroku-postgresql).
Then scroll to the bottom, select your app from the dropdown (or click login),
and then click 'Add Hobby Dev for Free'.
####Add your api_key to .travis.yml
Get your api_key by going to your [account settings](https://dashboard.heroku.com/account)
Click on the 'Show API Key' button, enter your password, and then paste this key
into the .travis.yml file (and add your app name) so that it looks something like
this:
```
deploy:
  provider: heroku
  api_key: 8a8a8a8a-1212-7b7b-2121-a8a8a8a8
  app: musictest
```
Save the travis file and commit it.

Now whenever a travis build on master passes (after you set up travis), it will
automatically deploy to heroku.

###Travis Configuration
Sign up/in to [travis-ci](http://travis-ci.org) with your github account, then
select 'Accounts' after hovering over your username at the top right. Find this
repository in there and switch it from off to on, and then you're good to go!

Additionally, you can change line 2 of this readme to have the build badge
reflect the status of your build instead of this one.
