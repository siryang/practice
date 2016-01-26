# GDB

``` gdb´ø²ÎÊýµ÷ÊÔ
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


É¾³ýbreakpoint
delete(d) %number

condition <break-number> <condition>

directory : set source search directory.