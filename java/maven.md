

### 打包
将多个module下的class打到另一个module中，使用maven-assembly-plugin   
将多个module下的sources打到Parent(POM)中，使用maven-assembly-plugin（包含子module的目录）

任意打包使用 maven-antrun-plugin



### plugin
使用execution goal可以给plugin绑定mvn的生命周期   
如果plugin中不指定execution的goal时, 需要在命令行中指定此plugin的名称和参数, eg: mvn assembly:single, mvn antrun:run   
Parent(POM)中的plugin会在各子模块中生效

1. 只有goals,没有parse(mvn的生命周期). 
需要手动调用mvn xxx:xxx
```
<groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-maven-plugin</artifactId>
  <executions>
      <execution>
          <goals>
              <goal>repackage</goal>
          </goals>
      </execution>
  </executions>
```
这个示例实际默认绑定到<a href='https://docs.spring.io/spring-boot/docs/current/maven-plugin/repackage-mojo.html'>package parse</a>上了 

2.有parse，也有goal. 在执行到parse时自动执行goal
```
  <groupId>com.alibaba.citrus.tool</groupId>
    <artifactId>autoconfig-maven-plugin</artifactId>
    <configuration>
        <dest>${project.build.outputDirectory}</dest>
        <exploding>false</exploding>
        <userProperties>${root-dir}/antx-${env}.properties</userProperties>
    </configuration>
    <executions>
        <execution>
            <phase>prepare-package</phase>
            <goals>
                <goal>autoconfig</goal>
            </goals>
        </execution>
    </executions>
```


### mirrors
mirrorOf和id值不能相同   
https://maven.apache.org/settings.html#Mirrors


### 哪些属性可以被子model继承
https://maven.apache.org/pom.html#Inheritance

maven搜索顺序relativePath==>local repo ==> remote repo
