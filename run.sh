#!/bin/sh

set -a
. ./.env
set +a

# pip3 install -r requirements.txt -q

exec uvicorn --reload --host 0.0.0.0 --port $PORT "$APP_MODULE"
