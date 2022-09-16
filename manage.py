import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SubterSite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment? Did you suck a little bit?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()