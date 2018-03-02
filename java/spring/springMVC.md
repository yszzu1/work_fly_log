

@RequestMapping(value = "/baseType",method = RequestMethod.GET)  
@RequestMapping("/home")  

name属性没有用处，映射url的是value属性，注意url中的斜线不能少, 其他属性都不写时就是指value属性


异常处理器HandlerExceptionResolver的实现方法resolveException最好有返回值ModelAndView，参考此方法的java doc
![](https://raw.githubusercontent.com/yszzu1/work_fly_log/94e32793905fc31ad396c562e0f0b61d4c39ba14/exception%20interceptor.png)

在没有返回值时异常会重新抛出，然后转发到/error请求，再次进入dispatchServlet,出现两次请求, 返回给客户端的结果可能不固定
![](https://github.com/yszzu1/work_fly_log/blob/master/images/springMVC%E5%BC%82%E5%B8%B8%E6%8B%A6%E6%88%AA.png)




### @EnableWebMvc
与<mvc:annotation> xml配置不要混合使用， 配置可能会被覆盖. 此注解最好不要使用.
参考https://stackoverflow.com/questions/31082981/spring-boot-adding-http-request-interceptors
https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#boot-features-spring-mvc-auto-configuration
