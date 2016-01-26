# GDB


* run gdb with arguments
```
gdb --args a.out arg1 arg2
```

* coredump

```
ulimit -c unlimited
echo "core" >  /proc/sys/kernel/core_pattern
./my_app.out
gdb --args my_app.out
core {core.dump.file}
```

* break points

    b <file:line>
    b <line>
    b <function>
    b main
    delete(d) number
    condition <break-number> <condition>

* other command
directory : set source search directory.
print array@10

### multi-thread

info thread: list thread info.
t 3: set current thread to #3.










