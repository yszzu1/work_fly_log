

### 1. 时序图  

### 2. singletone与prototype
***如果一个singletone的beanA，autowire引用了另外一个prototype的beanB, 那么在beanA中始终引用的是同一个beanB***

*  如果想重新注入一个新的beanB可以在A中加一个方法调用getBean(), 但是这样需要手动调用这个方法，能否自动调用呢？  
