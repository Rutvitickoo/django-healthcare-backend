#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare_backend.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if _name_ == '_main_':
    main()
