#!/bin/bash

set -e 

if [ ! -d "/tmp/firstrun" ]; then
    echo "Importing Schema.sql"
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" ${POSTGRES_DB} < /tmp/postgresql/schema.sql 1> /dev/null
    echo "Importing Images.Sql"
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" ${POSTGRES_DB} < /tmp/postgresql/images.sql 1> /dev/null
    echo "Importing Data.Sql"
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" ${POSTGRES_DB} < /tmp/postgresql/data.sql 1> /dev/null
    touch /tmp/firstrun
fi
