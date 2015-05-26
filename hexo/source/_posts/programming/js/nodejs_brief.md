
# NodeJS应用场景

## 和其他语言的比较

NodeJS优点主要体现在业务逻辑上，尤其是在有异步IO需求较多的地方。

## 操作系统: node-os

NodeOS 是采用NodeJS开发的一款友好的操作系统，该操作系统是完全建立在Linux内核之上的，并且采用shell和NPM进行包管理，采用NodeJS不仅可以很好地进行包管理，还可以很好的管理脚本、接口等。目前，Docker和Vagrant都是采用NodeOS的首个版本进行构建的。

![Image-node-os](http://www.nodejs.net/upload_files/as_images/2014/10/1522020lQ.png)

---

# NodeJS用法

## 模块加载

NodeJS模块加载顺序`文件模块缓存` > `原生模块` > `文件模块`。

`以下分别是什么东西`?

* http、fs、path等，原生模块。
* ./mod或../mod，相对路径的文件模块。
* /pathtomodule/mod，绝对路径的文件模块。
* mod，非原生模块的文件模块。

## 事件


### Emitter
``` JavaScript
	listener = callback();

	Emitter.on(event, listener);
	Emitter.once(event, listener);

	Emitter.emit(event, [arg1], [arg2], [...]);

	Emitter.removeListener(event, listener)
	Emitter.removeAllListener([event]);
```

### Error事件

如果Error事件没有相应的监听器，JS会默认退出程序并打印调用栈。

### 继承Emitter

多数时候我们不会直接使用 EventEmitter，而是在对象中继承它。只要是支持事件响应的核心模块都是 EventEmitter 的子类。

## CPP调用

* 1.


* isolate: 具有私有堆的虚拟机实例。
* local handle: 对象指针，因为V8内存回收机制需要，所有V8对象都用此类指针访问。
* handle scope: 应该是handle的内存管理工具，可以通过delete scope销毁所有handle,代替挨个销毁。
* context: 通过contex让所有JS代码独立的运行在同一个V8虚拟机上，所以执行JS代码时，必须制定contex。


## 内存机制

### Local<Type>
局部变量，分配在栈上。
随HandleScope销毁。HandleScope一般会在函数一开始声明。
HandleScope只能分配在栈上，不能用new分配。













