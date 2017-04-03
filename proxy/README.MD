Zabbix Proxy
-------------

This is a gcavalcante8808/zabbix-proxy image with Zabbix Proxy compilled with SQLITE3 support, based on debian docker official image.


Simple Usage
------------

Clone this repository (or copy the docker-compose.yml file) to your computer, and use the ** docker-compose ** to start the services:

``` 
    cd /tmp
    git clone https://github.com/gcavalcante8808/docker-zabbix-proxy
    cd docker-zabbix-proxy
    docker-compose up -d 
```

After some seconds the service will be available. Note that you need to have a zabbix-server working. Check at the docker-compose.yml file to define the zabbix-server address and port.

About SNMP MIBS
---------------

The Debian Team doesn't ship the snmp mibs by default. Instead, you need to install the 'snmp-mibs-downloader' and then install all mibs. To do this, you going to need a new image based in this one, that have the following Dockerfile:


```
    FROM gcavalcante8808/zabbix-server
    USER root
    RUN apt-get updat e&& apt-get install -y snmp-mibs-downloader && \
        downloads-mibs && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    USER zabbix
```

Built-in Agentd is no more
--------------------------

There is no support for an agentd image inside this image anymore. For now, you going to need to use an native version or a container version of the agent.

The docker-compose.yml file was updated to use the 'gcavalcante8808/zabbix-agentd' image, which is built in the same way than this one (compilled against the latest version).

Other infos
-----------

If you don't want to use 'docker-compose', you will need to have a previous Zabbix Server installed and configured. If you need an new Zabbix Server Image configured, you can use my Zabbix Images, available at:

https://github.com/gcavalcante8808/docker-zabbix-server

After the Server Configuration, to use this image, you would set the following variables:

 * ZBX_SERVER: Zabbix Server Address (if not provided, the container will exit automatically);
 * ZBX_SERVER_PORT: Zabbix Server Port (10051 is assumed if not provided);

Three volumes are available:
 
 * /usr/local/etc/zabbix_agentd.conf.d: which has all zabbix AGENTD configuration and allow you to tune your zabbix_agentd;
 * /usr/local/etc/zabbix_proxy.conf.d: which has all zabbix proxy configuration and allow you to tune your zabbix_proxy;
 * /usr/local/share/zabbix: which need to have the alertscripts and externalscripts folders and will be used to receive your scripts.

Use the following statement create a new Zabbix Proxy:

    docker run -d --name zabbix-proxy -v /conf:/usr/local/etc/zabbix_proxy.conf.d -e ZBX_SERVER=192.168.1.100 gcavalcante8808/zabbix-proxy

You can make some server adjustements by create or edit the files inside the "/conf" dir (or the dir what you defined during the run phase).

If you need a frontend to manage your zabbix, you can use my Zabbix FrontEnd Image, available at:

    https://github.com/gcavalcante8808/docker-zabbix-frontend


Author
------

Author: Gabriel Abdalla Cavalcante Silva (gabriel.cavalcante88@gmail.com)
