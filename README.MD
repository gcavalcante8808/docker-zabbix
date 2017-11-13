Docker-zabbix
-------------

This repository contain all information about gcavalcante8808 zabbix docker images.

You can check details of each image at the respective folder.

All images are founded on a Debian image with all modules support (except for mysql on server at this time) and support all versions through 3.0 to 3.4.

Supported Versions
------------------

In general, all stable versions of all daemons are supported. The Server is compilled with PostGreSQL support and an DB Image is provided as Well.

For proxy, the sqlite3 backend is used.

Check the Supported Versions file at  ([Supported Versions](https://github.com/gcavalcante8808/docker-zabbix/blob/master/supported_versions))

Simple Usage
------------

Clone this repository (or copy the docker-compose.yml file) to your computer, and use the ** docker-compose ** to start the services:

``` docker-compose up -d ```

After 15 seconds, check the port 80; the user and password are the default (User: "Admin", Password: "zabbix").

The docker-compose file uses the latest version of all images by default.
