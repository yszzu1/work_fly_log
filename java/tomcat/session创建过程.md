



HttpSession是在HttpRequest.getSession()时首次创建，如果浏览器没有关闭，这个sessionId会一直存在。  
使用这个sessionId可以向其他IP端口的应用发起请求，如果这个应用和首次创建session时的应用共用一个session存储的话。  

```

    public HttpSession getSession() {
        Session session = doGetSession(true);
        if (session == null) {
            return null;
        }

        return session.getSession();
    }
``` 
    doGetSession方法默认会创建新的session (如果request中没有sessionId)
    
