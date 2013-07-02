=====
django-mymigrate
=====

django-mymigrate is a wrapper on south that allows to quickly migrate all project apps with one command.


Quick start
-----------
./manage.py syncdb --all

./manage.py mymigrate -i
Creates initial migrations for all apps in project directory.
It is equivalent to run "./manage.py schemamigration app_name --initial" thought all apps in project directory.

./manage.py migrate --fake
Apply fake migrations.

Change something in models.

./manage.py mymigrate -a
Create auto migrations for all apps in project directory.
It is equivalent to run "./manage.py schemamigration app_name --auto" thought all apps in project directory.
Than run "./manage.py migrate" to apply migrations.

./manage.py mymigrate -d
Deletes all migrations on disk and database

Notes:
-----------

When you created initial migrations using "./manage.py mymigrate -i" and then created new app - you should manually run  
"./manage.py schemamigration new_app_name --initial" & "./manage.py migrate new_app_name" to create and apply initial migrations.
Than you can use "./manage.py mymigrate -a" in future development.


