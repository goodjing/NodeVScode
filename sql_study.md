## 数据语言分类
- DQL：数据查询语言，用于对数据进行查询，例如：select
- DML：数据操作语言，对数据进行增加、修改、删除，例如：insert、update、delete
- TPL：事务处理语言，对事务进行处理，例如：begin transaction、commit、rollback
- DCL：数据控制语言，进行授权与权限回收，例如：grant、revoke
- DDL：数据定义语言，进行数据库、表的管理等，例如：create、drop
- CCL：指针控制语言，通过控制指针完成表的操作，例如：declare cursor

## 数据表操作
### 创建表
```
create table 表名(
  字段名 类型 约束,
  字段名 类型 约束
  ...
)
```
**例：创建学生表**
姓名(长度为10)， 年龄， 身高(保留小数点2位) 
``` sql
create table students(
    id int unsigned primary key auto_increment,
    name varchar(20),
    age int unsigned,
    height decimal(5,2)
)
```
### 删除表
- 格式一： drop table 表名 
- 格式二： drop table if exists 表名 
**例：删除学生表**
``` sql
drop table students
或 
drop table if exists students
```

## 数据操作-增删改查
### 简单查询
``` 
select * from 表名
```
**例：查询所有学生数据**
```sql
select * from students
```
### 添加数据
#### 添加一行数据
**格式一：**
所有字段设置值， 值的顺序与表中字段的顺序对应
- 说明：主键列是自动增长， 插入时需要占位， 通常使用0或者 default 或者 null 来占位， 插入成功后以实际数据为准 
```
insert into 表名 values(...) 
```
**例：插入一个学生， 设置所有字段的信息**
``` sql
insert into students values(0,'亚瑟',22,177.56)
```
**格式二：**
部分字段设置值， 值的顺序与给出的字段顺序对应
**例：插入一个学生， 只设置姓名** 
``` sql
insert into students(name) values('老夫子')
```
#### 添加多行数据
**方式一：写多条insert语句， 语句之间用英文分号隔开**
``` sql
insert into students(name) values('老夫子2');
insert into students(name) values('老夫子3');
insert into students values(0,'亚瑟2',23,167.56)
```
**方式二：写一条insert语句，设置多条数据，数据之间用英文逗号隔开**
**格式一：**
```
insert into 表名 values(...),(...)...
```
**例：插入多个学生，设置所有字段的信息**
``` sql
insert into students values(0,'亚瑟3',23,167.56),(0,'亚瑟4',23,167.56)
```
**格式二：**
```
insert into 表名(列1,...) values(值1,...),(值1,...)...
```
**例：插入多个学生， 只设置姓名**
``` sql
insert into students(name) values('老夫子5'),('老夫子6')
```

