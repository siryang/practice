title: mysql
date: 2014-06-24 11:06:41
tags: Mysql
---

## 安装MYSQL

``` shell
rpm -e --nodeps mysql # remove old
yum install -y mysql-server mysql mysql-deve
service mysqld start # mysqld not mysql
chkconfig mysqld on # check is mysqld started
netstat -nat | grep 3306 # check 3306
vim /etc/sysconfig/iptables # firewall, add accept rule to 3306
service iptables restart
```


##启动
mysql -u @user -p 

CREATE USER 'jeffrey'@'localhost' IDENTIFIED BY 'mypass';
CREATE USER 'jeffrey'@'%' IDENTIFIED BY 'mypass';


##命令
select version();
select user();

show databases;
use @database name;

show tables;
use @table_name

show variables;
show variables like "%time%";
select @@global.wait_timeout;

set wait_timeout=2;
set global wait_timeout=2;



###用户权限

```
show grants for @user_name
GRANT ALL PRIVILEGES ON *.* TO 'comment'@'%' IDENTIFIED BY "comment" WITH GRANT OPTION; 
REVOKE INSERT ON *.* FROM 'comment'@'%';
```
mysql --host=10.10.23.74 --user=comment --password=comment

###经验
libmysqlclient文档中关于MYSQL_OPT_RECONNECT的用法是：
//mysql_option(mysql, MYSQL_OPT_RECONNECT, &bool); // call after mysql version xxx
mysql_real_connect();
//mysql_option(mysql, MYSQL_OPT_RECONNECT, &bool); // call before mysql version xxx
mysql_ping(); // mysql_ping会判断mysql->reconnect参数并进行重新连接

实测MYSQL_OPT_RECONNECT不好用（难道是上面用法有问题？），尽量自己实现RECONNECT
