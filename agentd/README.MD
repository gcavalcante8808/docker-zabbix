Zabbix Agent
------------

This is a gcavalcante8808/zabbix-agent image with Zabbix Agent, based on debian docker official image THAT HAVE THE CAPABILITY TO MONITOR THE HOST PROCESSES AND FILESYSTEMS!


Simple Usage
------------

Clone this repository into your computer:

```
   git clone https://github.com/gcavalcante8808/docker-zabbix-agent.git
   cd docker-zabbix-agent
```

Update the docker-compose.yml with your Zabbix Server Address and use the docker-compose to run it:

```
    docker-compose up -d
```

This image contains a vanilla zabbix-agentd compilled again the version defined in the Dockerfile and have the capability to monitor the host processes and other related
informations.

To work properly with docker, the Zabbix Agentd container should be run in "privileged" mode. In the previous version, the zabbix agentd just used proot to mount the files into the host archives, but was showing annoing problems related with lib versions on different Unix OSes; with this in mind, the proot mode was dropped and the privileged mode should be used from now on.
Other infos
-----------

This image support the following parameters (through env variables):

 * ZBX_SERVER: Zabbix Server IP or FQDN (Required):
 * ZBX_SERVER_PORT: Zabbix Server Port (10051 assumed if missing);
 * REMOTE_COMMAND: Enable or Disable support for remote commands (disabled by default);

You need to mirror your root into the "/rootfs" of the container, because it uses proot to run the zabbix_agentd as an native binary.

All configurations are written into /usr/local/etc/zabbix.conf.d/ by default (which make it a good endpoint for a named volume).


Author
------

Author: Gabriel Abdalla Cavalcante Silva (gabriel.cavalcante88@gmail.com)

