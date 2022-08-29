#!/bin/bash
set -a
. ./.env
set +a

ENV_FILE=./.env
if [ ! -f "$ENV_FILE" ]; then
    echo "$ENV_FILE does not exists. Please cp from source root"
    exit 1;
fi

if [ -z "$1" ]
  then
    echo "Please input downgrade version and try again"
    exit 1;
fi

echo --------------------
echo "Downgrade database"
echo --------------------

# Check if the database is already migrated and if not, migrate it
echo "Downgrade to version $1"
alembic downgrade $1

# Save the database's current migration state in a file
# `grep -v` for ignore `Binding` log
# `sed` to trim trailing whitespace
alembic history | grep -v -E '^(Binding).*' | sed 's/ *$//g' > ./alembic/versions/.history

echo "Update History Done"
