Website
=============
Website of CulturePlex Lab. It is a Django based-web with Fiber CMS.

Installation:

Just in case, first thing you need is to have installed pip_ and virtualenv_ in your machine::

  $ sudo apt-get install python-pip python-dev build-essential 
  $ sudo pip install --upgrade pip 
  $ sudo pip install --upgrade virtualenv 

Then, it's a good option to use virtualenvwrapper_::

  $ sudo pip install virtualenvwrapper

In the instructions given on virtualenvwrapper_, you should to set the working
directory for your virtual environments. So, you could add it in the end of
your .bashrc file::

  $ mkdir -p ~/.venvs
  export WORKON_HOME=~/.venvs
  source /usr/local/bin/virtualenvwrapper.sh

And finally, create a virtualenv for the project::

  $ mkvirtualenv website --no-site-packages

After you setup your virtual environment, you should be able to enable and
disable it. The system propmt must change where you have it enable::

  $ workon website
  $ deactivate

Now, if you didn't get the project yet, clone it in your desired location::

  $ git clone git@github.com:CulturePlex/website.git


Enter in the new location and update the virtual environment previously created::

  $ cd git/website/cultureplex
  $ workon website
  $ pip install -U -r requirements.txt

Now you have installed the Django project and almost ready to run it. Before that, you must create a database. In developing stage, we use SQLite:

$ python manage.py syncdb

Now, we recommend to install fixture file in fixtures/pagesandsampledata.json , it contains fiber pages and some sample data for database:

$ python manage.py loaddata fixtures/pagesandsampledata.json

And that is. If you run the project using the standalone development server of Django, you could be able to access to the URL http://localhost:8000/:

$ python manage.py runserver localhost:8000
$ xdg-open http://localhost:8000/
