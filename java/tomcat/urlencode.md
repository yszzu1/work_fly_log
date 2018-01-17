
请求体使用x-www-form-ulrencoded,
request.getParameter("XXX") 时取出的参数已经URLDecode
spring mvc中的@RequestParam实际是使用request.getParameter

servlet中使用request.getReader getInputStream来获得body byte[], 规范中是没有getBody()方法的

