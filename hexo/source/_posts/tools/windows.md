

## 设置开机自动启动
WIN+R运行`shell:startup`,将快捷键放入打开的目录。Example:`C:\Users\yangdi\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

## C盘空间过小

### 将其他主分区空闲空间追加到C盘
[EaseUS Partition](http://www.partition-tool.com/)

### 将文件复制到D盘，并创建硬链接

> robocopy source_dir dest_dir /mir

robocopy是对windows的复制粘贴的补充

> junction source_dir dest_dir

junction可以创建一个类似硬链接的文件，同时可以跨盘链接


## 系统事件

>6006 关机
>6009 开机

## 奇怪问题

### PhotoShop导致ESC失效

### 删除虚拟网卡
    在设备管理中









