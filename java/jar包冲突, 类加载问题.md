解决jar包冲突，在任意位置打印类所在的jar包
````
getClass().getClassLoader().getResource(XXX.class.getName().replace('.', '/') + ".class"));
````




现象:
Caused by: java.lang.NoClassDefFoundError: Could not initialize class org.hibernate.validator.internal.engine.ConfigurationImpl
	at org.hibernate.validator.HibernateValidator.createGenericConfiguration(HibernateValidator.java:33)
  
查看多次这个类在hibernate-validator中，在war包中是存在的，但就是加载不了

和上次的war对比，发现少了jboss-logging.jar, 加上之后就正常了

原因: ConfigurationImpl依赖jboss-logging, ***不是ConfigurationImpl找不到，而是它依赖的类找不到导致ConfigurationImpl加载不了***

