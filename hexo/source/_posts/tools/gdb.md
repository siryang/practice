title: GDB
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

b <file:line>
b <line>
b <function>
b main

删除breakpoint
delete(d) %number

condition <break-number> <condition>

directory : set source search directory.