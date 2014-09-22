### Apache安装

### Apache配置

``` shell
vim /ect/httpd/conf/httpd.conf
增加如下代码用于配置domain.com/ruby可访问/workspace/ruby
Alias /ruby /workspace/ruby
<Directory /workspace/ruby>
    Options  -Indexes FollowSymLinks
    AllowOverride All
    Order deny,allow
    Allow from all
</Directory>

注意selinux对目录权限的限制
```
