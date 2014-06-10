title: Install Ruby
date: 2014-05-30 10:35:49
categories:
- Ruby
tags: 
- ruby
---

##Ruby
###Why install 
the version of `yum install ruby` is 1.8.5, but new version of ruby is 2.1.2

###Download
[`Ruby 2.1.2`](http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz "Download Ruby 2.1.2"):http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz

###Install

```
tar -zxvf ruby-2.1.2.tar.gz
cd ruby-2.1.2
./configure --prefix=/usr/local/ruby
make & make install
```
所有的configure都支持通过指定--prefix设置编译目标文件路径

在PATH中添加ruby所在目录
修改/etc/profile，增加export PATH=/usr/local/ruby/bin:$PATH
source /etc/profile


--------------------------------
##Gem
###Download
[`Gem 2.2.2`](http://production.cf.rubygems.org/rubygems/rubygems-2.2.2.zip "Download rubygems")
###Install
```
unzip rubygems-2.2.2.zip
cd rubygems-2.2.2
gem install rails
```
*找不到zlib
	*	ERROR:  Loading command: install (LoadError)
		cannot load such file -- zlib
	*
	{% codeblock 重编zlib lang:shell %}
		cd /opt/ruby-2.1.2/ext/zlib
		ruby extconf.rb
		make 
		make install
	{% endcodeblock %}

*找不到OpenSSL
	*	ERROR:  While executing gem ... (Gem::Exception)
    	Unable to require openssl, install OpenSSL and rebuild ruby (preferred) or use non-HTTPS sources
    *
    {% codeblock 安装OpenSSL lang:shell %}
    	cd /opt/ruby-2.1.2/ext/openssl
    	ruby extconf.rb
    	make & make install
	{% endcodeblock %}
	编译(make)OpenSSL过程中出现没有发现ossl.o依赖的/thread_native.h，即找不到根目录下的thread_native.h。
	很少有开发会在根目录下放头文件，而在ruby-2.1.2目录下有这个文件。所以猜测是Makefile的错误
	编辑Makefile，在文件头部添加
	{% codeblock 编辑Makefile lang:makefile %}
	top_srcdir=../..
	{% endcodeblock %}
	重新`make & make install`，编译安装完成


--------------------------------
##Rails
`gem install rails`


--------------------------------
##node.js
[Node.js](http://nodejs.org/dist/v0.10.28/node-v0.10.28-linux-x64.tar.gz):http://nodejs.org/download/

--------------------------------
##Git
`yum install git`

