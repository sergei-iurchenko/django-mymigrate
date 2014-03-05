=====
django-mymigrate
=====

django-mymigrate is a wrapper on south that allows to quickly migrate all project apps with one command.

- version 0.2

- https://github.com/hellpain/django-mymigrate

Installation
-----------

pip install south

pip install django-mymigrate

In your settings.py define PROJECT_ROOT as a folder containing all your apps.

from os.path import join, normpath, dirname

PROJECT_ROOT = join(normpath(dirname(__file__)), '..')

in django 1.6 better use BASE_DIR which django creates

Commands
-----------

- ./manage.py mymigrate -i

Creates initial migrations for all apps in project directory.
It is equivalent to run "./manage.py schemamigration app_name --initial" through all apps in project directory.

- ./manage.py mymigrate -a

Create auto migrations for all apps in project directory.
It is equivalent to run "./manage.py schemamigration app_name --auto" through all apps in project directory.

- ./manage.py mymigrate -d

Deletes all migrations on disk and database.

Typical use
-----------

1) ./manage.py syncdb --all

Create all tables

2) ./manage.py mymigrate -i

Creates initial migrations for all apps in project directory.

3) ./manage.py migrate --fake

Apply fake migrations.

4) Change something in models...

5) ./manage.py mymigrate -a

Create auto migrations for all apps in project directory.

6) ./manage.py migrate

Apply migrations.

7) ./manage.py mymigrate -d

(optional) Delete all migrations on disk and database.

Notes:
-----------

When you created initial migrations using "./manage.py mymigrate -i" and then created new app, you should manually run
"./manage.py schemamigration new_app_name --initial" & "./manage.py migrate new_app_name" to create and apply initial migrations.
Only after that you can use "./manage.py mymigrate -a" in future development.

Release Notes:
-----------
- 0.2  Better support for django 1.6