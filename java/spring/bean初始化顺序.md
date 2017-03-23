

### 1. 时序图  

### 2. singletone与prototype
***如果一个singletone的beanA，autowire引用了另外一个prototype的beanB, 那么在beanA中始终引用的是同一个beanB***

*  如果想重新注入一个新的beanB可以在A中加一个方法调用getBean(), 但是这样需要手动调用这个方法，能否自动调用呢？  
*  在beanA的默认构造方法中增加getBean("beanB")， 或者使用lookup-method来配置beanA 
``` 
  <bean id="beanA" class="com.pramati.spring.RequestProcessor">
    <lookup-method name="getBeanB" bean="beanB"/> 
</bean>
```
*  使用aop切入
```
  <bean id="beanA" class="com.pramati.spring.RequestProcessor">
    <property name="validator" ref="validator"/>
</bean>
 
<bean id="beanB" scope="prototype" class="com.pramati.spring.RequestValidator">
    <!-- This instructs the container to proxy the current bean-->
    <aop:scoped-proxy/>
</bean>
```

参考： https://prasanthnath.wordpress.com/2013/03/21/injecting-a-prototype-bean-into-a-singleton-bean/
