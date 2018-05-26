


**现象:** 
请求并发不高，但是响应很慢， 调用别人的接口返回数据很快，但是自己的线程感觉响应时间慢

====> CPU压力太大， 线程数太多，死循环？


使用TOP查看 cpu load， 一会高一会低，双核cpu load有时达到8, *实际上达到cpu核心数就需要定位问题了*

**查看java进程有多少线程**  
1. top -Hp pid   在上面中有Thread的统计
2. ps -mp pid | wc -l 
3. cat /proc/xxx/

输出结果竟然有15000多个线程，对于双核cpu压力实在太大了，会引起系统不稳定


**jstack导出线程栈**  
内存操作，这个操作应该响应很快  
jstack pid >> xxx.log  
jstack pid | grep tid的十六进制数

*如果有死锁，会在最下面几行输出*

输出结果中并没有看到死锁，但是有很多（grep wc统计也正好15000多）

```
"Thread-507" #4327 daemon prio=5 os_prio=0 tid=0x00002b30cc10d000 nid=0x72fb in Object.wait() [0x00002b30f1759000]
   java.lang.Thread.State: TIMED_WAITING (on object monitor)
	at java.lang.Object.wait(Native Method)
	at com.mashape.unirest.http.utils.SyncIdleConnectionMonitorThread.run(SyncIdleConnectionMonitorThread.java:22)
	- locked <0x000000008b19e320> (a com.mashape.unirest.http.utils.SyncIdleConnectionMonitorThread)
 ```
 怀疑unirest没有释放http连接，官方文档看不出问题，怎么办？？？？
 
 进一步查看<u>SyncIdleConnectionMonitorThread.java:22</u>原码，发现这个线程**内部是个死循环,启动后线程不会退出**，每5秒自动释放idle的socket连接。而每次调用Unirest.setTimeouts()方法后，都会启动这样一个SyncIdleConnectionMonitorThread, 最终造成线程爆炸
 ```
 	public void run() {
		try {
			while (!Thread.currentThread().isInterrupted()) {
				synchronized (this) {
					wait(5000); // ***注意这行，==============>
					// Close expired connections
					connMgr.closeExpiredConnections();
					// Optionally, close connections
					// that have been idle longer than 30 sec
					connMgr.closeIdleConnections(30, TimeUnit.SECONDS);
				}
			}
		} catch (InterruptedException ex) {
			// terminate
		}
	}
 ```
 
 
 
 引入的问题: **线程为什么一直存在,为什么不释放?**  
 原因1: run方法中有类似while的死循环。 比如上面的情景, 多线程时HashMap的Entry<>引起的死循环, NIO的epoll bug。 线程一直处于running状态  
 原因2: run方法中有对象发生死锁。 造成线程一直处于wait状态  
 原因3: 线程池中core线程不会释放。 Worker对象持有一个final Thread， 线程池中管理Worker。  
  即使线程中引用的对象是Future之类的，只要不是死循环，线程在几秒内应该都会运行完成。 
  JVM退出的条件之一是没有运行中的非daemon线程,  一般用户自己启动的都是非daemon线程, 只要用户启动的线程运行完成，JVM都可以正常退出。 
  上面的线程数量过多并不影响jvm的退出。
 
 
 
 
 
