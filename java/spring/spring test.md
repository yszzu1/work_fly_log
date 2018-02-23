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




### spring boot test

```
@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = WebEnvironment.NONE)
public class XXXServiceImplTest2 {

    @Autowired
    private XXXserv xxxServ;

    @Test
    public void test_XXX() {
      xxxServ.xxx();
    }
}
```
使用@SpringBootTest的一些限制：
package结构最好符合规范, SpringBootApplication查找算法默认是根据包名,https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-testing.html#boot-features-testing-spring-boot-applications-detecting-config, 可以自动注入properties, @Configuration类中的bean
如果没有包名，需要手动确定
