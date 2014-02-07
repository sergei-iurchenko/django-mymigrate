#coding: utf-8
import os
import shutil
from django.core.exceptions import ImproperlyConfigured

from django.core.management.base import BaseCommand
from optparse import make_option
from django.conf import settings
# in your settings.py
# from os.path import join, normpath, dirname
# PROJECT_ROOT = join(normpath(dirname(__file__)), '..')
# in django 1.6 use BASE_DIR
if hasattr(settings, 'PROJECT_ROOT'):
    #old django <1.6, must be created
    ROOT = settings.PROJECT_ROOT
elif hasattr(settings, 'BASE_DIR'):
    #django >=1.6, created automatically
    ROOT = settings.BASE_DIR
else:
    raise ImproperlyConfigured('Set django project dir in "PROJECT_ROOT" or "BASE_DIR"')


from south.models import MigrationHistory


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            '-i',
            '--initial',
            action='store_true',
            default=False,
            help='South initial of all apps'),
        make_option(
            '-a',
            '--auto',
            action='store_true',
            default=False,
            help='South auto for all apps'),
        make_option(
            '-d',
            '--delete',
            action='store_true',
            default=False,
            help='Deletes all south migration folders for all apps and clears db'),)
    manage_py = os.path.join(ROOT, 'manage.py')

    def make_initial(self, app):
        os.system('%s schemamigration %s --initial' % (self.manage_py, app))

    def make_auto(self, app):
        print(app)
        os.system('%s schemamigration %s --auto' % (self.manage_py, app))

    def delete(self, app):
        migration_dir = os.path.join(ROOT, app, 'migrations')
        print(migration_dir)
        shutil.rmtree(migration_dir, ignore_errors=True, onerror=None)

    def handle(self, *args, **options):
        myapps = []
        for app in os.listdir(ROOT):
            if os.path.isdir(app):
                if any(installed_app == app for installed_app in settings.INSTALLED_APPS):
                    myapps.append(app)
        if options['initial']:
            for app in myapps:
                self.make_initial(app)
        elif options['auto']:
            for app in myapps:
                self.make_auto(app)
        elif options['delete']:
            print('Deleting folders with migrations...')
            for app in myapps:
                self.delete(app)
            print('Deleting migrations from database...')
            MigrationHistory.objects.all().delete()
            print('Now you may create initial migrations!')

