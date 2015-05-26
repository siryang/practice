title: GCC
categories:
- cpp
- program
---

``` gdb带参数调试
gdb --args a.out arg1 arg2
```

``` coredump
ulimit -c unlimited
echo "core" >  /proc/sys/kernel/core_pattern
./my_app.out
gdb --args my_app.out
core {core.dump.file}
```



