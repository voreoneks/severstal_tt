#!/bin/sh -e
set -x

flake8 app/
flake8 tests/

black app/ --check
black tests/ --check