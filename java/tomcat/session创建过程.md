



HttpSession是在HttpRequest.getSession()时首次创建，如果浏览器没有关闭，这个sessionId会一直存在。  
如果其他应用和当前应用共用一个session存储的话， 使用这个sessionId就可以向其他应用发起请求。  

````

    public HttpSession org.apache.catalina.connector.Request.getSession()() {
        Session session = doGetSession(true);
        if (session == null) {
            return null;
        }

        return session.getSession();
    }
````
    doGetSession方法传参为true,默认会创建新的session (如果request中没有sessionId),
    
````
    protected Session doGetSession(boolean create) {

        // There cannot be a session if no context has been assigned yet
        Context context = getContext();
        if (context == null) {
            return (null);
        }

        // Return the current session if it exists and is valid
        if ((session != null) && !session.isValid()) {
            session = null;
        }
        if (session != null) {
            return (session);
        }

        // Return the requested session if it exists and is valid
        Manager manager = context.getManager();
        if (manager == null) {
            return (null);      // Sessions are not supported
        }
        if (requestedSessionId != null) {
            try {
                session = manager.findSession(requestedSessionId);
            } catch (IOException e) {
                session = null;
            }
            if ((session != null) && !session.isValid()) {
                session = null;
            }
            if (session != null) {
                session.access();
                return (session);
            }
        }

        // Create a new session if requested and the response is not committed
        if (!create) {
            return (null);
        }
...
        // Re-use session IDs provided by the client in very limited
        // circumstances.
        String sessionId = getRequestedSessionId();
        if (requestedSessionSSL) {
            // If the session ID has been obtained from the SSL handshake then
            // use it.
        } else if (("/".equals(context.getSessionCookiePath())
                && isRequestedSessionIdFromCookie())) {
         
            if (context.getValidateClientProvidedNewSessionId()) {
                boolean found = false;
                for (Container container : getHost().findChildren()) {
                    Manager m = ((Context) container).getManager();
                    if (m != null) {
                        try {
                            if (m.findSession(sessionId) != null) {
                                found = true;
                                break;
                            }
                        } catch (IOException e) {
                            // Ignore. Problems with this manager will be
                            // handled elsewhere.
                        }
                    }
                }
                if (!found) {
                    sessionId = null;
                }
            }
        } else {
            sessionId = null;
        }
        session = manager.createSession(sessionId);//创建session的位置
...
        session.access();
        return session;
    }
 ````
         注意其中的Manager manager = context.getManager(); session实际是由manager创建并管理，而Manager默认会用的是org.apache.catalina.session.StandardManager,  我们可以在TOMCAT配置文件中指定自己实现的manager, Redis或者memcached的session共享插件也是这个原理。
 
 
    
