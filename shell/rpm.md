
rpm -qa | grep mysql
不要用rpm -ql mysql, 查找不全


rpm解压
rpm2cpio kchmviewer-3.1-1.el5.5.x86_64.rpm | cpio -div



查询文件在哪个rpm包中
rpm -qf xxx.cfg

查询rpm中有哪些文件
rpm -ql xxx.rpm

查询所有已安装的rpm包
rpm -qa
