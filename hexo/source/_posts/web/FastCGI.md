title: FastCGI
date: 2014-05-26 20:02:52
categories:
- Technology
tags: 
- FastCGI
---


## 源码

FCGI的源码有多个版本，可以从不同地址上下载到，某些下载链接不可用，下载到的源码可能还不同

## 编译

### Windows下编译

某个版本的FCGI下有WIN32目录，是配置好的vcproc

~~FCGI会修改environ这个全局变量，这里保存的是环境变量。使用FCGI后，用evniron这个变量的接口都无法使用了。~~

直接编译可以生成dll, 修改vcproc增加静态库编译配置



### 运行

修改Nginx配置 nginx.config
>server {
        listen   80;
        server_name _;

 		location / {
            # host and port to fastcgi server
            root   /home/user/www;
            index  index.html;

            fastcgi_pass 127.0.0.1:9000;
        }
}


`spawn-fcgi -s /temp/123.socket -F 1 -u nginx -d directory -f a.out`