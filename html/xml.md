

### xsd 与 namespace的关系

#### xsd == Xml Schema Definition 
targetNameSpace是定义在xsd中的, 并在xml文件头中使用，也可以在某个element中使用

```
 <h:table xmlns:h="http://www.w3.org/TR/html4/">
   <h:tr>
   <h:td>Apples</h:td>
   <h:td>Bananas</h:td>
   </h:tr>
</h:table>
```


  如果在xsd中指定elementFormDefault="qualified"， 那么在xml中使用时（此xsd不是默认空间），子元素element也需要加上namespace前缀  
  如果在xsd中指定elementFormDefault="unqualified", 子元素element不需要加上namespace前缀
 ```
<h:table xmlns:h="http://www.w3.org/TR/html4/">
   <tr>
   <td>Apples<td>
   <td>Bananas<td>
   </tr>
</h:table>
 
 
 ```




#### xml文件 
    头中声明的xmlns：xx="http://xxx/xxx", 不是以xsd结尾
              xsi:schemaLocation 定义多个xsd的位置，是W3C的规范，固定格式
    最多只能有一个没有后缀的xmlns, 并被当作默认namespace, 如果在element中没有使用前缀，就是指这个默认空间  
    
##### 参考
http://www.w3school.com.cn/schema/schema_complex_any.asp  
                 
             
