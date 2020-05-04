#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
from os.path import join, pardir, abspath, dirname, split
import sys


def main():
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # fix PYTHONPATH and DJANGO_SETTINGS for us
    # django settings module
    DJANGO_SETTINGS_MODULE = '%s.%s' % (split(abspath(dirname(__file__)))[1], 'settings')
    # pythonpath dirs
    PYTHONPATH = [
        abspath(join( dirname(__file__), pardir, pardir)),
        abspath(join( dirname(__file__), pardir)),
    ]

    # inject few paths to pythonpath
    for p in PYTHONPATH:
        if p not in sys.path:
            sys.path.insert(0, p)

    # django needs this env variable
    print('DEBUG: DJANGO_SETTINGS_MODULE={0}'.format(DJANGO_SETTINGS_MODULE))
    os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
