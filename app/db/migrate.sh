#!/bin/bash
set -a
. ./.env
set +a

echo --------------------
echo "Migrate database"
echo --------------------

# Check if the database is already migrated and if not, migrate it
alembic revision --autogenerate

# Save the database's current migration state in a file
# `grep -v` for ignore `Binding` log
# `sed` to trim trailing whitespace
alembic history | grep -v -E '^(Binding).*' | sed 's/ *$//g' > ./alembic/versions/.history

echo "Update History Done"
