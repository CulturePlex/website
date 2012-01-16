Website
=============
Website of CulturePlex Lab. It is a Django based-web with Fiber CMS.

Installation:

$ git clone git@github.com:CulturePlex/website.git

$ cd website/cultureplex

Now you have installed the Django project and almost ready to run it. Before that, you must create a database. In developing stage, we use SQLite:

$ python manage.py syncdb

And that is. If you run the project using the standalone development server of Django, you could be able to access to the URL http://localhost:8000/:

$ python manage.py runserver localhost:8000
$ xdg-open http://localhost:8000/
