SECRETS = {}

# Based on Django's SECRET_KEY hash generator
# https://github.com/django/django/blob/9893fa12b735f3f47b35d4063d86dddf3145cb25/django/core/management/commands/startproject.py

from django.utils.crypto import get_random_string
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRETS['secret_key'] = get_random_string(50, chars)

import json
print(json.dumps(SECRETS))
