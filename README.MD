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

To add a new supported version, you use the script *generate_version.py* after install the libraries present in requirements.txt. The command has the following syntax (eg):

```
   python generate_releases.py --version 4.0.0
```

Where version is the new version to be supported. To allow the things works as expected, its nice to update the supported_versions file as well.


Simple Usage
------------

Clone this repository (or copy the docker-compose.yml file) to your computer, and use the ** docker-compose ** to start the services:

``` docker-compose up -d ```

After 15 seconds, check the port 80; the user and password are the default (User: "Admin", Password: "zabbix").

The docker-compose file uses the latest version of all images by default.

Triggering Real Time event support (Zabbix 4.0.0+)
--------------------------------------------------

If you want to export events in real time as stated in https://www.zabbix.com/documentation/4.0/manual/appendix/protocols/real_time_export, you can do it through the following environment variables:

 * EVENT_EXPORT_DIR: The directory that will receive the files;
 * EVENT_EXPORT_FILESIZE: Optional, the size of each file. By default, zabbixes uses 1G as a value.

**You going to need a volume inside the container to receive the logs and the user zabbix (id 1000) should have the ownership of the volume.**

Author
------

Author: Gabriel Abdalla Cavalcante Silva (gabriel.cavalcante88@gmail.com)