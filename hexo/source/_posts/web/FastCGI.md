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
FCGI会修改environ这个全局变量，这里保存的是环境变量。使用FCGI后，用evniron这个变量的接口都无法使用了。

### Linux下编译

README文件中写的是configure & make & make install
实际使用gcc 4.9.0 和 gcc 4.1.2 make时都会有错误



