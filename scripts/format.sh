#!/bin/sh -e
set -x

isort app/
isort tests/

black app/
black tests/