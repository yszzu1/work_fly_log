


java进程异常结束, 也没有生成dump, 可能是被操作系统直接kill了

/var/log/message中oom killer生成的日志示例
![oom killer](https://github.com/yszzu1/work_fly_log/blob/master/images/linuxOOMkiller.png)

最简单直接的方法是增加内存

参考:https://yq.aliyun.com/articles/78307?spm=5176.10695662.1996646101.searchclickresult.175368d5LqF8Rq
