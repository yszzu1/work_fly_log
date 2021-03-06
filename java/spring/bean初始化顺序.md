

### 1. 时序图  
默认情况下是启动时初始化，可以通过``<beans default-lazy-init="true"/>``来修改默认行为。
如果一个非延时初始化的bean引用了一个lazy-initialize的bean， 那么这个lazy-initialize bean会在启动时被初始化，以正常完成依赖注入。
http://docs.spring.io/spring/docs/current/spring-framework-reference/htmlsingle/#beans-factory-lazy-init

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
  
！！如果prototype实体使用cglib代理，那么get set方法不能是final类型的，final会造成值直接set到proxy对象上，而不是动态生成的对象上  

参考： https://prasanthnath.wordpress.com/2013/03/21/injecting-a-prototype-bean-into-a-singleton-bean/
http://docs.spring.io/spring/docs/2.5.x/reference/beans.html#beans-factory-scopes-sing-prot-interaction
http://docs.spring.io/spring/docs/current/spring-framework-reference/htmlsingle/#beans-factory-scopes-sing-prot-interaction

### 3. 依赖注入
spring依赖注入有一个限制：小作用域的对象不能被注入到大作用域的对象。你不能够把request和session作用域的对象注入到singleton对象中。前者在每次WEB请求时，均会创建新的实例，每个线程独享这个request/session作用域的对象；后者是在Spring初始化或第一次使用时被创建，然后被所有的线程共享。假如你把某个request/session作用域的对象意外注入到singleton对象中，将可能产生致命的应用错误，甚至导致数据库的错乱。
因此structs中action都需要设置成prototype  
参考：http://openwebx.org/docs/filter.html
webx中使用 <aop:scoped-proxy/>来实现小对象注入到大对象中
