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
