#!/bin/sh -e
set -x

flake8 cli.py
flake8 app/

black cli.py --check
black app/ --check