#!/bin/bash
cd -- "$(dirname "$0")"

if ! [[ -x "$(command -v python3)" ]]
then
  echo 'You must install Python 3.10.1 first: https://www.python.org/downloads/release/python-3101/'
  exit 1
else
  pip install -r requirements.txt
  python3 todo.py $1
fi

