Layer--xml
	Linear Layout
	Relative Layout

	TextView



Android界面设计为xml格式，存放在res目录下

	android:layout_width // 窗体宽度--match_parent代表填满parent
	android:layout_height // 窗体高度--match_parent代表填满parent

	android:id // 窗体唯一标识
	
values/string.xml
	将字符串以name="key">value<格式写入放到中，在窗体设计的xml中使用@string:key访问
	

Context:
	Context类是抽象类，提供了一组通用的POI用于访问应用程序全局信息。一些应用级别的类（Android内部类）都继承自Context
	总Context实例个数 = Service个数 + Activity个数 + 1（Application对应的Context实例）
Activity:
	一个Activity对应一个应用程序界面，可以启动其它Activity以跳转界面
	创建方法：startActivity() / startActivityForResult()
	提供onCreate(), onStart()接口，当Activity创建时，回调

Service:
	应用的后台服务，生命周期不取决于某个Activity。
	创建方法：startService() / bindService()

Intent:
	用于屏幕管理切换，操作方法分“动作（）”和“数据（URL表示）”两部分
	IntentFilter:
		用于描述一个Activity/IntentReceiver能够操作哪些intent
		需要在AndroidMainifest.xml中定义怎么去处理View动作和URL，当startActivity()调用时，会去解析对应的xml，并触发相应动作。
	IntentReceiver:
		InetnetReceiver可以对系统事件的响应，当事件发生时会用NotificationManager通知用户
		在AndroidMainifest.xml中注册 ，也可以用Context.registerReceiver()注册
		使用Context.broadcastIntent()可以将事件广播给其它程序。
Content Provider：
	用于Android应用之间传递数据，如某应用读通讯录和微博数据


Android提供的API
android.app ：提供高层的程序模型、提供基本的运行环境
android.content ：包含各种的对设备上的数据进行访问和发布的类
android.database ：通过内容提供者浏览和操作数据库
android.graphics ：底层的图形库，包含画布，颜色过滤，点，矩形，可以将他们直接绘制到屏幕上.
android.location ：定位和相关服务的类
android.media ：提供一些类管理多种音频、视频的媒体接口
android.net ：提供帮助网络访问的类，超过通常的 java.net.* 接口
android.os ：提供了系统服务、消息传输、IPC 机制
android.opengl ：提供 OpenGL 的工具
android.provider ：提供类访问 Android 的内容提供者
android.telephony ：提供与拨打电话相关的 API 交互
android.view ：提供基础的用户界面接口框架
android.util ：涉及工具性的方法，例如时间日期的操作
android.webkit ：默认浏览器操作接口
android.widget ：包含各种 UI 元素（大部分是可见的）在应用程序的屏幕中使用


JVM和Dalvik虚拟机

.java 源文件
.class 目标文件(无法在Android Dalvik上执行,需要链接成dex文件)
.dex Android上的可执行文件
.apk Android上的安装文件，打包了AndroidMainifest.xml、dex、资源文件和其他文件










