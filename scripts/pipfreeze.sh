#!/bin/sh -e
set -x

pip freeze | grep -vFxf requirements.txt