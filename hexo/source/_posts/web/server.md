title: WEB
date: 2014-05-26 20:02:52
categories:
- Technology
tags: 
- web toolkit
---

##服务器
###云主机

###虚拟主机
###域名服务
*	fight4seat.com
*	

----------------------------
##HTTP服务器

Apache / Nginx / lighttpd 是一类，都是专用的WEB服务器，Tomcat / Jetty 是一类，是servlet/jsp应用服务器+WEB服务器 ，Jboss则是一个大框架，也是应用服务器 + WEB服务器，但是Tomcat 或则Jetty 都是它的一部分

###Apache
1. WEB服务器，通常仅用于处理静态页面，用于URL转发
2. 移植性强，支持Perl, FCGI

###Lighttpd
1. 开源、支持FCGI、CGI、Auth
2. 内存和CPU开销低
3. 稳定性不如Nginx和Apache

###Nginx
1. 资源占用少
2. 来自俄罗斯
3. 似乎仅支持FCGI
4. 支持热部署

#### Nginx安装
* 1.yum -y install pcre-devel

###Tomcat
Apache常用于支持静态页面，所以需要Tomcat支持jsp/servlet等
Apache支持PHP,Perl,CGI,但不支持JAVA/JSP/JS
Tomcat静态页面处理能力上没Apache专业。当使用Apache+Tomcat时，Apache只是作为转发
Tomcat常用于服务器对Java/Jsp/JS的支持

###Jetty

---
## CGI & Fast CGI
CGI和FCGI和语言无关，WEB服务器通过CGI/FCGI调用本地程序并获取返回结果
CGI的生命周期是一次调用时间
FCGI在CGI基础上做了优化，启动多个CGI解释器(进程)供WEB服务器连接（资源池）

<!--可以认为FCGI和CGI只是一种协议-->

<!--另外，可以在HTTP服务器中集成一些语言的解释器，就可以直接由HTTP服务器调用此程序（一种非CGI方式）-->

###ASP
微软公司开发的代替CGI脚本程序的一种应用

---

##Web应用框架

### Rails
ruby

### jQuery
js

### django
python

### Spring
java

--------------------------
## 动态网页

###PHP
服务端，超文本处理语言

###JSP
动态网页技术标准
在传统的网页HTML（标准通用标记语言的子集）文件(*.htm,*.html)中插入Java程序段(Scriptlet)和JSP标记(tag)
由Sun Microsystems公司倡导、许多公司参与一起建立

---

## 服务器语言

###Ruby
###JSP

## 客户端语言

###JavaScript
###Silverlight
微软出的一套接口，用于终端渲染，据说是和Adobe Flash竞争市场。Linux版的叫Moonlight(开源)

---
[IIS]
[Apache]
[Nginx](http://zh.wikipedia.org/wiki/Nginx)
[Tomcat]
[Jetty]
[Passenger]
[Rails]
[Lighttpd](http://zh.wikipedia.org/wiki/Lighttpd)

[CGI]
[FCGI]
[ASP]
[JSP]
[JS]
[Silverlight]


[Servlet]