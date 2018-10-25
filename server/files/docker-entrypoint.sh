#!/bin/bash

set -e

CONF="/usr/local/etc/zabbix_server.conf.d"

if [ -z ${DB_HOST} ]; then
    echo "No Default DB Host Provided. Assuming 'db'"
    DB_HOST="db"
fi

if [ -z ${DB_PORT} ]; then
    echo "No Default port for Db Provided. Assuming 5432."
    DB_PORT=5432
fi

if [ -z ${DB_USER} ]; then
    echo "No Default User provided for Db. Assuming zabbix"
    DB_USER="zabbix"
fi

if [ -z ${DB_PASS} ]; then
    echo "No Default DB Password provided. Assuming zabbix"
    DB_PASS="zabbix"
fi

if [ -z ${DB_NAME} ]; then
    echo "No default db name provided. Assuming zabbix"
    DB_NAME="zabbix"
fi

cat <<EOT > $CONF/automatic.conf
DBHost=${DB_HOST}
DBPort=${DB_PORT}
DBUser=${DB_USER}
DBName=${DB_NAME}
DBPassword=${DB_PASS}
LogFile=/tmp/zabbix_server.log
LogFileSize=1024
LogType=console
ListenPort=10051
EOT

if [ ! -z ${EVENT_EXPORT_DIR} ]; then
    echo "Export event flag reconized. Creating dir and set permissions if needed and configuring zabbix_server."
    if [[ ! -d ${EVENT_EXPORT_DIR} ]]; then
        mkdir -p ${EVENT_EXPORT_DIR}
    fi
    echo "ExportDir=${EVENT_EXPORT_DIR}" >> $CONF/automatic.conf
fi

if [[ ! -z ${EVENT_EXPORT_FILESIZE} ]]; then
    echo "Defining the filezie as ${EVENT_EXPORT_FILESIZE}"
    echo "ExportFileSize=${EVENT_EXPORT_FILESIZE} >> $CONF/autmoatic.conf"
fi

exec /usr/local/sbin/zabbix_server -f -c "/usr/local/etc/zabbix_server.conf"
