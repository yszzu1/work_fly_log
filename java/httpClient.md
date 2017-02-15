##超时时间

httpclient.getParams().setParameter("http.socket.timeout",1000);

httpclient.getParams().setParameter("http.connection.timeout",1000);

httpclient.getParams().setParameter("http.connection-manager.timeout",60*60L);

// httpclient.setConnectionTimeout(1000);

// httpclient.setTimeout(1000);

// httpclient.setHttpConnectionFactoryTimeout(1000);


##是否保持连接
request.addHeader("Connection", "close");
