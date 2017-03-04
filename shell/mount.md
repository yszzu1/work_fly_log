移动硬盘挂载，需要先配置NFS客户端

mount -t ntfs -o iocharset=cp936 /dev/sdc1 /mnt/usbhd1     #  文件名为汉字可以用这个命令

U盘挂载

mount -t vfat /dev/sdd1 /mnt/usb

其他网络上的window共享目录挂载，需要安装samba

mount -o username=admin,password=123,iocharset=utf8//10.140.133.23/c$ /mnt/samba

mount

-o 可指定多个参数, 比如字符集

-t  挂载的文件类型ntfts iso fat32等，
