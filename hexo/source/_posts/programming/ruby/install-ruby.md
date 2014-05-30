title: install ruby
date: 2014-05-30 10:35:49
categories:
- Ruby
tags: 
- ruby
---

##Why install 
the version of `yum install ruby` is 1.8.5, but new version of ruby is 2.1.2

##Download
[`Ruby 2.1.2`](http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz "Download Ruby 2.1.2"):http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz

##Install

```
tar -zxvf ruby-2.1.2.tar.gz
cd ruby-2.1.2
./configure --prefix=/usr/bin/ruby
make & make install
```

