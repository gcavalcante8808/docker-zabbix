#!/bin/bash

set -e

CONF="/usr/local/etc/zabbix_proxy.conf.d"

if [ -z "${ZBX_SERVER}" ]; then
    echo "No default Zabbix Server provided. Exiting ..."
    exit 1
fi

if [ -z "${ZBX_SERVER_PORT}" ]; then
    echo "No Zabbix Server Provided. Using 10051"
    ZBX_SERVER_PORT=10051
fi


if [ -z "${ZBX_PROXY_NAME}" ]; then
    echo "No ZBX proxy Name provided. Exiting..."
    exit 1
fi


echo "Include=/usr/local/etc/zabbix_proxy.conf.d/" > /usr/local/etc/zabbix_proxy.conf

cat <<EOT > $CONF/automatic.conf
ListenPort=10051
DBName=/tmp/zabbix_proxy.db
Server=${ZBX_SERVER}
ServerPort=${ZBX_SERVER_PORT}
Hostname=${ZBX_PROXY_NAME}
LogFile=/tmp/zabbix_proxy.log 
LogFileSize=1024
LogType=console
EOT

exec /usr/local/sbin/zabbix_proxy -f -c "/usr/local/etc/zabbix_proxy.conf"
