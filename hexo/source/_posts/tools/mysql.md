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


##命令
select version();
select user();

show databases;
use @database name;

show tables;
use @table_name


###用户权限

```
show grants for @user_name
grant all privileges on route_c.* to 'comment'@'%';
```
###经验

