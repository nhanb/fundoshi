#!/usr/bin/env python

###########################################################
# Distribute on PyPI if this is a tagged commit by owner #
# NOTE: This script is to be executed on travis CI only.  #
###########################################################

import sys
from os import environ as env
from os.path import expanduser
from subprocess import call


# Gatekeeping: Abort if not a tagged commit by owner
if not (
    env.get('TRAVIS_PULL_REQUEST') == 'false' and
    env.get('TRAVIS_TAG')
):
    print('Not a tagged commit by owner => Not publishing.')
    print('TRAVIS_TAG=' + env.get('TRAVIS_TAG'))
    print('TRAVIS_PULL_REQUEST=' + env.get('TRAVIS_PULL_REQUEST'))
    sys.exit()


# Write ~/.pypirc file so we can publish our package on PyPI:

pypirc = """
[distutils]
index-servers=
    pypi

[pypi]
repository = https://pypi.python.org/pypi
username = nhanb
password = %s
"""

with open(expanduser('~/.pypirc'), 'w') as f:
    f.write(pypirc % env.get('PYPI_PASSWORD'))


# Install build tools, build, publish, profit.
call('pip install setuptools wheel', shell=True)
call('python setup.py sdist', shell=True)
call('python setup.py bdist_wheel', shell=True)
call('python setup.py sdist upload -r pypi', shell=True)
call('python setup.py bdist_wheel upload -r pypi', shell=True)
