## 一.PVR工具安装说明
IMG比较靠谱，PVR所有工具都是免费的！！！

PVR安装在你的PC上，作为Host端；我们的target端已经有相应的文件了，具体位置在：

    /opt/img-powervr-sdk

有Windows、Linux、MacOS版本，下载地址：

    http://community.imgtec.com/developers/powervr/tools/

## 二.PVR使用说明

1. PVRTune：

    首先，在PC上启动PVRTune;

    然后，执行

        adb forward tcp:6520 tcp:6520

    然后，在target上执行

        /opt/img-powervr-sdk/PVRHub/PVRPerfServer/PVRPerfServerDeveloper

    然后，在PC上PVRTune上点击

        "Android USB device" 按扭
     OK！ 启动你的进程即可！
2. PVRTrace

        首先，push pvrtraceconfig.json（见附件）到某个目录下，比如/opt/app/com.yunos.apidemo/; 注意，里面假设你有个目录为/test，你可以修改为任意位置; 假设只capture 64帧，你可以修改;所有配置参数意义可见PVRTrace的帮助文档;

        然后，export LD_PRELOAD=/opt/img-powervr-sdk/PVRHub/PVRTrace/Recorder/libEGL.so:/opt/img-powervr-sdk/PVRHub/PVRTrace/Recorder/libGLESv2.so:/opt/img-powervr-sdk/PVRHub/PVRTrace/Recorder/libPVRTrace.so

       然后，对于genric程序，忽略这一步; 对于node起的程序，由于PVR存在bug，我们需要做个 patch：

              http://gerrit3.alibaba-inc.com:8080/#/c/142335/

       把编译好的libQt5Gui.so.5.3.0/libQt5Core.so.5.3.0等等push到/usr/lib/下，libqtforyunos.so应该push到/usr/lib/qt5/plugins/platforms/yunos/下，当前由于image存在bug，还需要同时push到/usr/lib/下;

       一切准备OK，运行你的程序，比如apidemo：

              node --harmony index.js

       生成的文件pull到PC上，使用PVRTrace打开即可！

## 三.PVR当前问题

1. PVRTrace对于node起的程序存在bug;

2. PVRTrace对于sendlink起的程序存在crash;

3. 据我的测试，PVRTrace在Linux上有时候打开一些文件会crash，没有windows上的稳定。

