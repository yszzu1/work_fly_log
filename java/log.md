## TOOLS
### 性能分析  
  btrace    
  火焰图  
  socket backlog 等待队列的长度  
  
  
  
### logback MDC  
用来在日志中增加自定义字段  
![xml解析过程](https://github.com/yszzu1/work_fly_log/blob/master/images/logback%20xml%E9%85%8D%E7%BD%AE%E8%A7%A3%E6%9E%90%E8%BF%87%E7%A8%8B.png)

#### 显示异常日志中的jar目录
https://logback.qos.ch/manual/configuration.html#packagingData



## slf4j logback log4j都存在时，为什么不冲突? 为什么有冲突?

* 不冲突是因为代码里面使用的是slf4j的api, 不是logback/log4j的api  
* 冲突是因为slf4j api对应有两个实现, logback-classic是对slf4j的原生实现;   slf4j-log4j是log4j对slf4j api的实现，属于中间层。  
### 如何确保只有一个日志实现 
>>>> lib中只存在logback-classic或者slf4j-log4j中的一个, 不要都存在。  commons-logging类似
