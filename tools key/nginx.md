

* 配置示例
```
    server {
        listen       80;
        server_name  localhost;

        location / {
        #指定网站的根目录,默认是nginx下的html目录
            root   C:/Users/wb-ys274743/Desktop/;
            index  index.html index.htm;
        }
 
		error_page  404              /404.html;
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
        
    }
    
```
