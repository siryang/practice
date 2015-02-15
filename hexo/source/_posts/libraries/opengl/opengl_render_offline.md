title: OpenGL������Ⱦ
categories:
- OpenGL

# brief
```
A FBO (Framebuffer object) is a target where you can render images other than the default frame buffer or screen.

A PBO (Pixel Buffer Object) allows asynchronous transfers of pixel data to and from the device. 
PBO(���ػ������): �������غ��豸ͬ������/������

This can be helpful to improve overall performance when rendering if you have other things that can be done while waiting for the pixel transfer.
���ڵȴ�����ת��ʱ��Ҫ������������ʱ�������������������
```

* GLTStopwatch 1/100����Ⱦ��������
	* GLTStopwatchReset()
	* GLTStopwatchRead()


# ʹ��OpenGL��ͼ���ļ�

��ȡ��OpenGL��ͼ�������Ϊ`glReadPixels`, ����ʵ�ֽ���Ļ����copy�������ڴ�


## GLX PixelMap
��Ӳ������
����һ���ڴ������OpenGL, �����������OpenGL��ʵ�ʻ�ͼ����

## PBuffer
PBufferʹ��ͼ���ڴ������XPixelMap
��˵���°��OpengGL���Ѿ����𲽷���

## Framebuffer Object
ͨ��ָ��Render Buffer Objectָ����Ⱦλ�ã����ҿ��Կ����л���Ⱦλ��

## Pixel Buffer Object
��Ҫ����֧���첽�����д


## �Ƚ�
OpenGL��Ƥ��������н�����Linux��ʹ��GLX PixelMap��PBuffer��������Ⱦ�ķ������ڵ������ɾ�������£�
��˵�����𲽷�������PBuffer����

FBO�������ᳫ������������Ⱦ

PBO�������ᳫ�������첽���ش���


http://www.opengl.org/discussion_boards/showthread.php/168610-pBuffer-vs-PBO-vs-FBO