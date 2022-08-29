#!/bin/bash
set -a
. ./.env
set +a

echo --------------------
echo "Upgrade database"
echo --------------------

# Run migrations
alembic upgrade head

# Save the database's current migration state in a file
# `grep -v` for ignore `Binding` log
# `sed` to trim trailing whitespace
alembic history | grep -v -E '^(Binding).*' | sed 's/ *$//g' > ./alembic/versions/.history

echo "Update History Done"
