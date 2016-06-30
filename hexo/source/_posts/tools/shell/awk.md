

删除带clean的所有进程
ps -x | grep clean | awk '{system("kill -9 "$1)}'

查找wl_egl_window_create所在的so
ls *.so.* |  awk '{system("echo " $1); system("nm "$1" | grep wl_egl_window_create")}' > 123.txt