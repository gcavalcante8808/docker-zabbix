Zabbix Db Postgres
------------------

This is a gcavalcante8808/zabbix-db-postgres image with with Zabbix Database Creation Scripts (schema, image and data) imported, based on postgres docker official image.

Build the Image
---------------

```docker build -t gcavalcante8808/zabbix-db-postgres . ```

If you want to build the image with a specific version of Zabbix (3.2.0 in the sample), you can do the following:

``` docker bulid --build-arg ZBX_VERSIOn=3.2.0 -t gcavalcante8808/zabbix-db-postgres . ```


Simple Usage
------------

If you just want to create a Zabbix Service from scratch, check for the compose files and instructions at the following project:

https://github.com/gcavalcante8808/docker-zabbix-server


Other Infos
-----------

If you dont want to use docker-compose, you will need to repeat the 'run' syntax defined on the postgres official image, like:

``` docker run --name zabbix-db -v /datafolder:/var/lib/postgres/data -e POSTGRES_DB=zabbix -e POSTGRES_USER=zabbix -e POSTGRES_PASSWORD=zabbix gcavalcante8808/zabbix-db-postgres ```

Change the "POSTGRES_DB", "POSTGRES_USER" and "POSTGRES_PASSWORD" environment variables to your preference.

After this, proceed with Zabbix Server and Frontend creation. If you want to use a docker image for it, you can see instructions of how to get the images working at:

https://github.com/gcavalcante8808/docker-zabbix-frontend.git
https://github.com/gcavalcante8808/docker-zabbix-server.git


Other Options about the Postgres Image
--------------------------------------

If you want to see a complete set of options, take a loot at:

https://hub.docker.com/_/postgres/

Author
------

Author: Gabriel Abdalla Cavalcante Silva (gabriel.cavalcante88@gmail.com)
