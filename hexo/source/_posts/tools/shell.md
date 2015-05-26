
##系统
* history 100: 显示最后100条指令

* rpm
** 1.列出rmp包中所有文件 `rpm -qlp httpd-2.2.3-31.el5_4.2.x86_64.rpm`

* xWindow
** 1.以XWindow启动：修改/etc/inittab中id:3:initdefault中数字，以选择默认启动界面

* 资源管理

** 查看目录大小
`du -h --max-depth=1 .` -h: human readable.

* 后台运行

	+ nohup cmd > log.msg 2> log.err & : 让命令忽略所有SIGHUP信号
	+ setsid cmd : 运行为守护进程
	+ (cmd &) : 运行为守护进程
	+ disown -h %jobId : 将job忽略SIGHUP信号。
	+ screen : 创建一个离线的伪终端，所有命令都离线执行。

* Mount Remote File
+ 如何Mount远程目录到本地？

* SSH
+ 为什么使用rsa-key连接ssh，忽然需要输密码了？

创建.ssh/config文件，写入以下内容，就可以用`ssh compiler`登录了。 config文件记录的是ssh连接时的默认设置。
> 	Host compiler
	Hostname 10.218.145.106
	IdentityFile ~/.ssh/gitlab_rsa
	User yangdi.yd
	Port 22

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

* find
** find -name "*.c"


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


## rsync

-a 参数，相当于-rlptgoD，-r 是递归 -l 是链接文件，意思是拷贝链接文件；-p 表示保持文件原有权限；-t 保持文件原有时间；-g 保持文件原有用户组；-o 保持文件原有属主；-D 相当于块设备文件；
-z 传输时压缩
-P 传输进度
-u, --update 仅仅进行更新，也就是跳过所有已经存在于DST，并且文件时间晚于要备份的文件。(不覆盖更新的文件)




