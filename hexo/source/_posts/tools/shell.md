
##系统
* history 100: 显示最后100条指令

* rpm 
** 1.列出rmp包中所有文件 `rpm -qlp httpd-2.2.3-31.el5_4.2.x86_64.rpm`

* xWindow
** 1.以XWindow启动：修改/etc/inittab中id:3:initdefault中数字，以选择默认启动界面

---


## 网络指令
### 端口
netstat -apn | grep 80
kill -9 PID


---


## 字符处理

* 重定向
> dir file.xxx > output.msg 2> output.err
注意`2>`不能写成`2 >`

* grep
** egrep == grep -e
** 查找source目录下的所有c/cpp文件，find ./source | grep "\.cpp$|\.c$"


