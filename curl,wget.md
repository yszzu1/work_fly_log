格式化json
`curl -d @swiftuser.json -H "Content-type:application/json"  http://172.25.71.13:35357/v2.0/tokens  |python -mjson.tool`

格式化xml
`curl -d @swiftuser.json -H "Content-type:application/json"  http://172.25.71.13:35357/v2.0/tokens  |xmllint --format -`


curl -d 'xxx' http://xxxx/url 默认使用的就是POST请求


wget http://xxxl?name=&link=8828 因为url会有一些shell特殊字符,因此url部分最好使用单引号或者双引号括起来。
