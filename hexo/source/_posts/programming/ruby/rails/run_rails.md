title: run_rails
date: 2014-06-10 14:28:03
categories: Ruby
tags: Ruby Rails
---

* 创建rails服务
```shell
#输入以下指令创建一个叫demo的rails工作目录
rails new demo
cd demo
#检查服务器依赖的组件
bundle install
#启动服务
rails server
```

* 修改rails服务对应页面
	*	`config/routes.rb`:指定URL对应的页面位置，每个页面对应一个Action和一个View
	*	`app/controllers/*.rb`:定义Action, *处保存的是Controller
	*	`app/views/*/*.html.erb`:第一个*是Controller,第二个是页面名称
		*	welcome_say_hello_path, root_path
```shell
rails generate controller welcome
```