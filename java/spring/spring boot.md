

Spring boot 中一些自带的管理beans


 
/heath 可以查看应用是否启动成功，

/beans可以查看当前加载的bean

/env 可以查看当前应用的jar

/autoconfig 可以查看已经生效的@Configuretion bean

/metircs 查看应用占用的内存大小，访问http状态码记数

除/heath外, 其他的访问需要在application.properties中加入以下配置，以禁用安全校验 （代码见MvcEndpointSecurityInterceptor）

***management.security.enabled=false***

参考:  
https://docs.spring.io/spring-boot/docs/current/reference/html/production-ready-endpoints.html  
http://www.blogs8.cn/posts/A5qja11  
https://docs.spring.io/spring-boot/docs/current/reference/html/production-ready-monitoring.html  

