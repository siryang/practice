
##系统
* history 100: 显示最后100条指令

* rpm 
** 1.列出rmp包中所有文件 `rpm -qlp httpd-2.2.3-31.el5_4.2.x86_64.rpm`

* xWindow
** 1.以XWindow启动：修改/etc/inittab中id:3:initdefault中数字，以选择默认启动界面

---


## 网络指令
### 端口

``` shell
netstat -apn | grep 80
kill -9 PID
```

## 服务

``` shell
service mysqld start/status/stop #mysql
service httpd start # apache
service nginx start
```

---


## 字符处理

* 重定向
> dir file.xxx > output.msg 2> output.err
注意`2>`不能写成`2 >`

* grep
** egrep == grep -e
** 查找source目录下的所有c/cpp文件，find ./source | grep -e "\.cpp$|\.c$"


## 脚本

### 执行参数

	$0 param 1
	$1 param 2
	$2 param 3
	$3 param 4
	$# param number 
	$@ all params

```shell

while getopts ":dh" opt;
do
	case $opt in 
		h)
			echo "-h"
			;;
		d)	echo "-d";;
		?)  echo "invalid";;
	esac
done

```
### 判断
if [ "$var" == "" ]; then
	echot "empty string"
fi

### 函数

```shell
function system_info
{
    echo "<h2>System release info</h2>"
    echo "<p>Function not yet implemented</p>"

}   # end of system_info
```









