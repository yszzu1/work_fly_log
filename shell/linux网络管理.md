centos配置路由的几种方式  
在/etc/sysconfig/network配置全局默认路由(网关) GATEWAY=192.168.1.2  
在/etc/sysconfig/network-scripts/ifcfg-xxx配置单个网口的默认路由（网关）GATEWAY=192.168.1.2  
在/etc/sysconfig/network-scripts/route-xxx配置单个网口的默认路由（网关）default via 192.168.1.2  

https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Networking_Guide/sec-Using_the_Command_Line_Interface.html#sec-Static-Routes_and_the_Default_Gateway




