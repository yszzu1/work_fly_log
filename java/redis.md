
###  redis集群  

先以集群模式启动各个节点（需要修改各节点下的redis.conf），然后使用脚本配置集群进行选主，确定master slaver关系
```
cluster-enabled yes
cluster-config-file nodes-6379.conf
cluster-node-timeout 15000
```
***多个master组成一个集群，一个集群中不止一个master  
集群数据不是使用一致性hash, 而是使用slot管理的***  
每个master只管理部分slot, 如果一个master挂了(下面没有备节点)，这个集群也就废了（此部分的slot数据永远不能访问）， 因此需要给master加至少一个slaver

16个database与slot是什么关系?

数据的key不能为null， value也不能为null?   


如果Spring-data-redis使用集群方式配置connectionPool, 则redis也必须以集群方式启动  

### 项目中使用

spring boot项目中可以使用spring-data-autoconfig.jar中的RedisProperties 来简化配置, 支持集群配置

redisTemplate注册的成ListOperation的原理 http://www.cnblogs.com/chanedi/p/4135303.html  

