Zabbix Frontend
---------------

This is a gcavalcante8808/zabbix-frontend image with Zabbix Frontend installed.

Build the Image
---------------
    docker build -t gcavalcante8808/zabbix-frontend .

If you want to build the image with a specific version of the Zabbix Frtoned (3.2.0 in the sample), you can do the following:

    docker build --build-arg ZBX_VERSION=3.2.0 -t gcavalcante8808/zabbix-server .

Simple Usage
------------

If you just want to create a Zabbix Service from scratch, check for the compose files and instructions at the following project:

https://github.com/gcavalcante8808/docker-zabbix-server


Usage
-----

You need to have a Zabbix Database and Server configured properly. If you don't have them yet, check my images at:


Then, you need to supply the following environment variables:

 * DB_HOST: Zabbix Database;
 * DB_TYPE: Zabbix Database Type (POSTGRESQL, MYSQL);
 * DB_PORT: Zabbix Database Port (5432 for Postgres, 3306 for MySQL);
 * DB_USER: Database User;
 * DB_PASS: Database User Password;
 * DB_NAME: Database Name;

 * ZBX_SERVER: Zabbix Server Address;
 * ZBX_SERVER_PORT: Zabbix Server listenPOrt (10051 Usually);
 * ZBX_SERVER_NAME: a Custom name for the installation.

With all this information, you can now run the container:

    docker run -d --name zabbix-frontend -e DB_HOST=192.168.1.100 -e DB_PORT=5432 -e ZBX_SERVER=192.168.1.101 -e DB_NAME=zabbix -e DB_PASS=zabbix gcavalcante8808/zabbix-frontend


Author
------

Author: Gabriel Abdalla Cavalcante Silva (gabriel.cavalcante88@gmail.com)
