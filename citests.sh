#!/usr/bin/env bash

# Exit when any command fails
set -e

export PYTHONPATH=`pwd`

echo '============================='
echo '=     RUNNING NOSETESTS     ='
echo '============================='
echo ''
nosetests

echo ''
echo '============================'
echo '=     RUNNING DOCTESTS     ='
echo '============================'
echo ''
cd docs && make doctest
