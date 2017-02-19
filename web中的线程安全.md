##servlet的线程模型

Tomcat启动时会创建线程池，当接收到一个请求时先创建一个servlet对象，分配一个独立的线程来调用doService方法
**线程是由tomcat来管理和调用的**  
从Java 内存模型也可以知道，**方法中的临时变量是在栈上分配空间，而且每个线程都有自己私有的栈空间，所以它们不会影响线程的安全**  
这样每个线程就会有一个栈空间上的request和response对象  
<a>DispatcherServlet在每个栈空间上设置了一个新的Controller(如果配置成protoscope)对象，但是使用同一个service对象，因此Spring使用ThreadLocal来处理多线程的问题</a>  
**多线程问题是由Servlet中的实例变量引起，尽量在doService方法中使用局部变量**
