#!/usr/bin/env python


import collections
import collections.abc

# Add these lines before any Django imports
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quizfreakapp.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
