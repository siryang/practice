```
	cp /etc/samba/smb.conf /etc/samba/smb.conf-original
	vim /etc/samba/smb.conf
	useradd samba // ���������˻�
	passwd samba // �˻�����
	smbpasswd -a samba // samba ����
	service smb reload / restart // ����samba����
	service iptables stop // �رշ���ǽ, Ҳ�����޸�/etc/sysconfig/iptables�򿪶˿ڣ�Ҳ������Linuxͼ�ι�����
	chcon -t samba_share_t /share // ����selinux
	chcon -t samba_share_t /home/samba
	testparm // ����
	smbclient //127.0.0.1/share --user samba //�ڱ��ز�������
```

```
insert to smb.conf
[share]
        comment = share
        writeable = yes
        browseable = yes
        path = /share

```



[�������]( service smb status)
[����tree connect failed: NT_STATUS_ACCESS_DENI](http://callmepeanut.blog.51cto.com/7756998/1304442)

### ����NT_STATUS_ACCESS_DENIED


[����NT_STATUS_ACCESS_DENIED listing - Access](http://www.it2down.com/it-access/412718.htm)
> NT_STATUS_ACCESS_DENIED listing *
��CENTOS�����˸�SAMBA��WINDOW�����ļ���

һ���ʹ���Ŀ¼�͡�NT_STATUS_ACCESS_DENIED listing *�� �����˺þã�������SELINUX�赲�ˡ�



[root@linux tmp]# smbclient //127.0.0.1/sambar -U sambar%sambar
Domain=[WORKGROUP] OS=[Unix] Server=[Samba 3.5.10-114.el6]
smb: > ls
NT_STATUS_ACCESS_DENIED listing *

                52265 blocks of size 1048576. 48406 blocks available

�������һ��

�ر�SELIUNX

[root@linux /]# getenforce   ;�鿴��ǰ״̬
Enforcing 

[root@linux /]# setenforce 0;



SELINUX����״̬��ʾ��

enforcing��ǿ��ģʽ������ SELinux �����У����Ѿ���ȷ�Ŀ�ʼ���� domain/type �ˣ�
permissive������ģʽ������ SELinux �����У����������о�����Ϣ������ʵ������ domain/type �Ĵ�ȡ������ģʽ����������Ϊ SELinux �� debug ֮�ã�
disabled���رգ�SELinux ��û��ʵ�����С�



�����������

����selinux�Ĳ���

chcon -t samba_share_t  ����Ŀ¼(/var/www/html)


chcon -t samba_share_t /share /workspace

