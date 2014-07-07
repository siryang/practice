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

## rails配置
### Controller
对应源码在app/controllers中
### 

|檔案/目錄 	| 用途|
| --------  | -----:  |
|Gemfile	| 設定Rails應用程式會使用哪些Gems套件|
|README		| 專案說明：你可以用來告訴其他人你的應用程式是做什麼用的，如何使用等等。|
|Rakefile	| 用來載入可以被命令列執行的一些Rake任務|
|app/		| 放Controllers、Models和Views檔案，接下來的內容主要都在這個目錄。|
|config/	| 應用程式設定檔、路由規則、資料庫設定等等|
|config.ru	| 用來啟動應用程式的Rack伺服器設定檔|
|db/		| 資料庫的結構綱要|
|doc/		| 用來放你的文件|
|lib/		| 放一些自定的Module和類別檔案|
|log/		| 應用程式的Log記錄檔|
|public/	| 唯一可以在網路上看到的目錄，這是你的圖檔、JavaScript、CSS和其他靜態檔案擺放的地方|
|script/	| 放rails這個指令和放其他的script指令|
|test/		| 單元測試、fixtures及整合測試等程式|
|tmp/		| 暫時性的檔案|
|vendor/	| 用來放第三方程式碼外掛的目錄|

