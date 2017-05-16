增加一列：

   alter table emp4 add test varchar2(10);

修改一列：

   alter table emp4 modify test varchar2(20);

删除一列：

alter table emp4 drop column test;

 

　　这里要注意几个地方，首先，**增加和修改列是不需要加关键字COLUMN**，否则会报错ora-00905。

　　其次，对删除单列的话，一定要加COLUMN，然后记住，删除是不需要加列类型的。

 

增加多列：

   alter table emp4 add (test varchar2(10),test2 number);

修改多列：

   alter table emp4 modify (test varchar2(20),test2 varchar2(20));

删除多列：

   alter table emp4 drop (test,test2);

很奇怪的现象，再单列中要加关键字COLUMN，然而再删除多列的时候，不能加COLUMN关键字。
