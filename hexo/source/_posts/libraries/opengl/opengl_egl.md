# 常用链接
[EGL extensions](https://www.khronos.org/registry/gles/extensions/)


# EGL介绍
* EGL是Native平台和OpenGL ES之间的抽象层。完成了本地相关的环境初始化和上下文控制。保证OpenGL ES平台无关。

* display: 显示设备。

* surface: 存储图像的内存区域FrameBuffer的抽象，包括Color Buffer, Stencil Buffer, Depth Buffer。

* context: 保存Opengl状态的内存块。


eglGetDisplay

eglInitialize

eglGetConfigs

eglChooseConfig

eglCreateWindowSurface

eglCreateContext

eglQuerySurface

eglMakeCurrent



# Opengl MutiThread

# Opengl non-power-of-two

GL_ARB_texture_non_power_of_two (OES_texture_npot for OpenGL ES platform).

ES 3.0 has full NPOT support
ES 2.0 has limited NPOT support (no mipmaps, no Repeat wrap mode) in core; and ES 1.1 has no NPOT support.

For ES 1.1 and 2.0, full NPOT support comes with GL_ARB_texture_non_power_of_two or GL_OES_texture_npot extension. In practice, iOS devices don’t support this; and on Android side there’s support on Qualcomm Adreno and ARM Mali. Possibly some others.

For ES 1.1, limited NPOT support comes with GL_APPLE_texture_2D_limited_npot (all iOS devices) or GL_IMG_texture_npot (some ImgTec Android devices I guess).

WebGL and Native Client currently are pretty much OpenGL ES 2.0, and thus support limited NPOT textures.


