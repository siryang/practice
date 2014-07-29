title: mysql
date: 2014-06-24 11:06:41
tags: Mysql
---


##启动
mysql -u @user -p 


##命令
select version();
select user();

show databases;

use @table_name


###用户权限

```
show grants for @user_name
grant all privileges on route_c.* to 'comment'@'%';
```

###经验

