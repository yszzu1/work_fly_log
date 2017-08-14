一些前端组件  
sea.js  seajs.use(xxx.js), 直接用script引入不会自动调用里面的方法
Handlebars.js 可以访问WINDOW中定义的全局变量


jquery  deferred.done ajax请求返回一个deferred对象 

如果是在ajax.done之后 才调用window.open会被浏览器拦截，方法是先打开一个窗口并持有它的引用，在done之后修改成需要的URL



富文本编辑
https://www.tinymce.com/


jquery .ajax() 参数URL为空时，默认向当前地址发送请求。 增加判断 如果为空直接返回，避免重复请求。
