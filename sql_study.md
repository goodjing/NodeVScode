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
### 修改
```
update 表名 set 列1=值1,列2=值2... where 条件 
```
**例：修改id为5的学生数据，**姓名改为 狄仁杰， 年龄改为 20 
```sql
update students set name='狄仁杰',age=20 where id=5
```
### 删除
**格式一：**
```
delete from 表名 where 条件
```
**例：删除id为6的学生数据**
```sql
delete from students where id=6
```

**逻辑删除**
对于重要的数据，不能轻易执行delete语句进行删除。因为一旦删除，数据无法恢复，这时可以进行逻辑删除。
1. 给表添加字段，代表数据是否删除，一般起名isdelete，0代表未删除，1代表删除，默认值为0
2. 当要删除某条数据时，只需要修改这条数据的isdelete字段为1
3. 以后在查询数据时，只查询出isdelete为0的数据  

**例：**
1. **给学生表添加字段(isdelete)，默认值为0，**如果表中已经有数据，需要把所有数据的isdelete字段更新为0
```sql
update students set isdelete=0
```
2. **删除id为1的学生**
```sql
update students set isdelete=1 where id=1
```
3. **查询未删除的数据**
```sql
select * from students where isdelete=0
```

**格式二：**
```
truncate table 表名（删除表的所有数据， 保留表结构）
```
**例：删除学生表的所有数据**
```sql
truncate table students
```

**格式三：**
```
drop table 表名（删除表， 所有数据和表结构都删掉）
```
**例：删除学生表**
```sql
drop table students
```
#### Truncate、 Delete、 Drop 的区别
1. Delete 删除数据时， 即使删除所有数据， 其中的自增长字段不会从1开始
2. Truncate 删除数据时， 其中的自增长字段恢复从1开始
3. Drop 是删除表， 所有数据和表结构都删掉

**总结:**
1. 在速度上， drop > truncate > delete
2. 如果想删除部分数据用 delete， 注意带上 where 子句
3. 如果想删除表， 用 drop
4. 如果想保留表而将所有数据删除， 自增长字段恢复从1开始， 用 truncate

## 数据操作-查询
### 数据准备
#### 创建数据表
```sql
drop table if exists students;
create table students (
  studentNo varchar(10) primary key,
  name varchar(10),
  sex varchar(1),
  hometown varchar(20),
  age tinyint(4),
  class varchar(10),
  card varchar(20)
);
```
#### 插入数据
```sql
insert into students values
('001', '王昭君', '女', '北京', '20', '1班', '340322199001247654'),
('002', '诸葛亮', '男', '上海', '18', '2班', '340322199002242354'),
('003', '张飞', '男', '南京', '24', '3班', '340322199003247654'),
('004', '白起', '男', '安徽', '22', '4班', '340322199005247654'),
('005', '大乔', '女', '天津', '19', '3班', '340322199004247654'),
('006', '孙尚香', '女', '河北', '18', '1班', '340322199006247654'),
('007', '百里玄策', '男', '山西', '20', '2班', '340322199007247654'),
('008', '小乔', '女', '河南', '15', '3班', null),
('009', '百里守约', '男', '湖南', '21', '1班', ''),
('010', '妲己', '女', '广东', '26', '2班', '340322199607247654'),
('011', '李白', '男', '北京', '30', '4班', '340322199005267754'),
('012', '孙膑', '男', '新疆', '26', '3班', '340322199000297655');
```
### 查询的基本语法
```
select * from 表名
和
select 字段1,字段2,... from 表名
```
**例：查询全部字段和部分字段**
```sql
select * from students;
select name,sex,age from students
```
## 高级查询
[详细文档见语雀](https://www.yuque.com/loulou-ambjk/welvha/epwxau)
