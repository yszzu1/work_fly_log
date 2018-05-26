
## 两种定时任务:  
`ScheduledExecutorService.scheduleAtFixedRate(Runnable command,long initialDelay,long period,TimeUnit unit)`  
以固定的period周期启动任务,  如果任务消耗的时间大于period周期,那么下次启动是在任务消耗的时间之后。

如果这个任务报出异常，那么后面的任务都不会再执行了.

`ScheduledExecutorService.scheduleWithFixedDelay(Runnable command,long initialDelay,long delay,TimeUnit unit);`  
以固定的delay启动任务,  本次任务结束后有个delay的延时，然后才启动下次任务.
