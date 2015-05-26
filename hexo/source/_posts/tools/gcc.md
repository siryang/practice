title: GCC
categories:
- cpp
- program
---

``` gdb����������
gdb --args a.out arg1 arg2
```

``` coredump
ulimit -c unlimited
echo "core" >  /proc/sys/kernel/core_pattern
./my_app.out
gdb --args my_app.out
core {core.dump.file}
```



