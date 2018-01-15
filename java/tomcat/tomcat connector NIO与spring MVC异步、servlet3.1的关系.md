

tomcat connector的NIO   http://www.importnew.com/27309.html

servlet3.0的异步  
spring mvc的异步  http://www.bijishequ.com/detail/538890?p= ,是servlet3.0异步的另一种实现, 对比@WebServlet(async=true)


**NIO与异步是两个概念**  没有异步io的说法，只有非阻塞io的说法!!!

1. NIO是socket层面的, 可以增加连接数,比如几万个连接,非NIO时一般机器上只能支撑到3000个连接  
原因是大部分的keep-alive连接有很多是不活动的，并不需要占用tomcat的work线程。NIO即能保持socket的keep-alive, 也能释放work线程。  
使用少量(几百个)的work线程即可接收几万个连接的请求

2. 异步是servlet业务处理的, 新开业务线程(和tomcat的work线程也分开, 他们两个的联系是AsyncContext对象). 没有NIO时也能异步处理. servlet3.1的异步在socket的操作上使用的是JDK事件机制，不是用的jdk NIO

**对象和线程是两个概念**

线程可以处理很多个对象  
一个对象通常只在一个线程中, 多线程编程时也不会超过几十个线程。


