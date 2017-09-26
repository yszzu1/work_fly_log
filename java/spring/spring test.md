``` 

@ContextConfiguration(classes={RedisConfig.class, ClusterConfigurationProperties.class})
@PropertySource("classpath:application-test.properties") //Resource location wildcards (e.g. *&#42;/*.properties) are not permitted;
@EnableAutoConfiguration
@RunWith(SpringJUnit4ClassRunner.class)
public class RedisDaoTest {

}

``` 


### ContextConfiguration 
用于指定spring context启动的上下文位置，通常是@ContextConfiguration("classpath:spring-context.xml") <br>
但是如果使用@Configuration 也可以只指定class, 此时需要配合@EnableAutoConfiguration使用  
### PropertySource
用于加载配置文件， 必须使用全名，不能使用通配符。此注解可以使用多个




