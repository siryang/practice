

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