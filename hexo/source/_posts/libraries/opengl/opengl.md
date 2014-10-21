title: OpenGL离屏渲染
categories:
- OpenGL

# brief
```
A FBO (Framebuffer object) is a target where you can render images other than the default frame buffer or screen.

A PBO (Pixel Buffer Object) allows asynchronous transfers of pixel data to and from the device. 
PBO(像素缓冲对象): 允许像素和设备同步传入/传出，

This can be helpful to improve overall performance when rendering if you have other things that can be done while waiting for the pixel transfer.
当在等待像素转换时，要进行其他处理时，有利于提高整体性能
```

* GLTStopwatch 1/100秒渲染多少屏？
	* GLTStopwatchReset()
	* GLTStopwatchRead()


# 使用OpenGL绘图到文件

读取将OpenGL绘图结果函数为`glReadPixels`, 可以实现将屏幕内容copy到本地内存


## GLX PixelMap
非硬件加速
创建一块内存区域给OpenGL, 申请的区域是OpenGL的实际绘图区域

## PBuffer
PBuffer使用图形内存而不是XPixelMap
据说在新版的OpengGL中已经被逐步废弃

## Framebuffer Object
通过指定Render Buffer Object指定渲染位置，并且可以快速切换渲染位置

## Pixel Buffer Object
主要用于支持异步纹理读写


## 比较
OpenGL蓝皮书第三版中讲解了Linux下使用GLX PixelMap和PBuffer做离屏渲染的方法，在第五版中删除了这章，
据说厂商逐步废弃上述PBuffer方案

FBO方案被提倡用来做离屏渲染

PBO方案被提倡用来做异步像素处理


http://www.opengl.org/discussion_boards/showthread.php/168610-pBuffer-vs-PBO-vs-FBO