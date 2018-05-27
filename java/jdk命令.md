## 运行jar包中的一个类  
java -cp xxx.jar:yyy.jar a.b.c.AB arg1 agr2

## classPath引入多个jar  
linux中示例: `java -cp '.:./lib/*'   XxxClass`  
注意下面这样是不行的, `java -cp '.:./lib/junit*.jar'  XxxClass`


## jmap生成堆内存dump
## jstack生成Tread dump

