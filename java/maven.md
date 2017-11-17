

### 打包
将多个module下的class打到另一个module中，使用maven-assembly-plugin
将多个module下的sources打到Parent(POM)中，使用maven-assembly-plugin（包含子module的目录）

任意打包使用 maven-antrun-plugin



### plugin
使用execution goal可以给plugin绑定mvn的生命周期   
如果plugin中不指定execution的goal时, 需要在命令行中指定此plugin的名称和参数, eg: mvn assembly:run, mvn antrun:run   
Parent(POM)中的plugin会在各子模块中生效


