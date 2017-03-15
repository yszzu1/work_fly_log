***静态方法拦截***
PowerMockito.mockStatic(KeystoneClientImpl.class);



*** new对象前拦截  ***
PowerMockito.whenNew(FileWriter.class).withArguments(anyString()).thenReturn(fileWrite);
   
      

***跳过某个方法***
PowerMockito.doNothing().when(KeystoneClientImpl.class, "writeCert", any(CertType.class), any(String.class));


***调用mock对象的真实方法***
doRealMethod()
