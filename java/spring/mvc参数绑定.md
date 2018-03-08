
[原码分析](http://www.cnblogs.com/fangjian0423/p/springMVC-request-param-analysis.html)


@ModelAttribute  对应的参数解析器ServletModelAttributeMethodProcessor, 使用request.getParamter
@RequestBody 对应的参数解析器RequestResponseBodyMethodProcessor, 参数(序列化)转换器MappingJackson2HttpMessageConverter, 使用request.getInputStream


同时支持两种content-type, Jquery.ajax默认的content-type是x-www-form-urlencoded  
示例:

```
    @PostMapping(value = "/testContentType", consumes = "application/x-www-form-urlencoded")
    public String testB(@ModelAttribute Dto invokeDTO) {
        return "1";
    }

    @PostMapping(value = "/testContentType", consumes = "application/json")
    public Result testC(@RequestBody Dto invokeDTO) {
        return "2";
    }
    
```
