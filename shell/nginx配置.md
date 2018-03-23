
一个反向代理的示例
```
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    upstream  favtomcat
    {
        #server   localhost:8887 weight=1;
        server   localhost:8888 weight=90;
    }
    server
    {
        listen  80;
        server_name  favtomcat;
 
        location / {
            proxy_pass         http://favtomcat;
            proxy_set_header   Host             $host;
            proxy_set_header   X-Real-IP        $remote_addr;
        }
    } 
}
```


upstream模块必须在http{}模块里面  
客户端request先经过server的proxy_pass模块转发到upstream模块, 再到后端真实服务器地址.  
在proxy_pass中可以加入自定义请求头, $remote_addr是nginx内置变量  
proxy_pass后面必须是http://+upsteam名字  

http://favtomcat host配置在nginx所在机器  
服务下线: 在upstream server前面注释掉, 然后执行nginx -s reload

