首先使用apache创建http目录
将wordpress内容复制到目录

。。。


### 目录权限问题导致无法安装插件的问题
chomod 777 wp-content
上传插件, 发现wp自己创建了一个wp-content/upload目录，owner是apache:apache
将父目录chown为apache:apache
