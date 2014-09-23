```
	cp /etc/samba/smb.conf /etc/samba/smb.conf-original
	vim /etc/samba/smb.conf
	useradd samba // 创建共享账户
	passwd samba // 账户密码
	smbpasswd -a samba // samba 密码
	service smb reload / restart // 重启samba服务
	service iptables stop // 关闭防火墙, 也可以修改/etc/sysconfig/iptables打开端口，也可以用Linux图形管理工具
	chcon -t samba_share_t /share // 设置selinux
	chcon -t samba_share_t /home/samba
	testparm // 测试
	smbclient //127.0.0.1/share --user samba //在本地测试连接
```

```
insert to smb.conf
[share]
        comment = share
        writeable = yes
        browseable = yes
        path = /share

```



[如何配置]( service smb status)
[错误：tree connect failed: NT_STATUS_ACCESS_DENI](http://callmepeanut.blog.51cto.com/7756998/1304442)

### 错误：NT_STATUS_ACCESS_DENIED


[错误：NT_STATUS_ACCESS_DENIED listing - Access](http://www.it2down.com/it-access/412718.htm)
> NT_STATUS_ACCESS_DENIED listing *
在CENTOS上配了个SAMBA与WINDOW共享文件。

一访问共享目录就”NT_STATUS_ACCESS_DENIED listing *“ ，找了好久，发现是SELINUX阻挡了。



[root@linux tmp]# smbclient //127.0.0.1/sambar -U sambar%sambar
Domain=[WORKGROUP] OS=[Unix] Server=[Samba 3.5.10-114.el6]
smb: > ls
NT_STATUS_ACCESS_DENIED listing *

                52265 blocks of size 1048576. 48406 blocks available

解决方法一：

关闭SELIUNX

[root@linux /]# getenforce   ;查看当前状态
Enforcing 

[root@linux /]# setenforce 0;



SELINUX几种状态表示：

enforcing：强制模式，代表 SELinux 运行中，且已经正确的开始限制 domain/type 了；
permissive：宽容模式：代表 SELinux 运行中，不过仅会有警告信息并不会实际限制 domain/type 的存取。这种模式可以运来作为 SELinux 的 debug 之用；
disabled：关闭，SELinux 并没有实际运行。



解决方法二：

更改selinux的策略

chcon -t samba_share_t  共享目录(/var/www/html)


chcon -t samba_share_t /share /workspace

