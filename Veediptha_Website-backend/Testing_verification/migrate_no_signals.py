import os
import django
from django.core.management import execute_from_command_line

# Monkey patch to disable create_permissions during migrate
def dummy_create_permissions(*args, **kwargs):
    pass

import django.contrib.auth.management
django.contrib.auth.management.create_permissions = dummy_create_permissions

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    django.setup()
    execute_from_command_line(["manage.py", "migrate"])
