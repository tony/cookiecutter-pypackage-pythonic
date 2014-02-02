#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

{{ cookiecutter.project_name }}
{{ '-' * cookiecutter.project_name|count }}

{{ cookiecutter.project_short_description }}

"""

from __future__ import absolute_import, division, print_function, \
    with_statement, unicode_literals

__title__ = '{{ cookiecutter.project_name }}'
__package_name__ = '{{ cookiecutter.repo_name }}'
__author__ = '{{ cookiecutter.full_name }}'
__description__ = '{{ cookiecutter.project_short_description }}'
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'
__license__ = '{{ cookiecutter.license }}'
__copyright__ = 'Copyright {{ cookiecutter.year }} {{ cookiecutter.full_name }}'

from .{{ cookiecutter.repo_name }} import {{ cookiecutter.repo_name | capitalize }}
