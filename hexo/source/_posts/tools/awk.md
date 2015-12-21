

删除带clean的所有进程
ps -x | grep clean | awk '{system("kill -9 "$1)}'