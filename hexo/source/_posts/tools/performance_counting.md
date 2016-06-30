
# perf

perf是linux 2.6+提供的系统工具，包含在linux kernel的tools/perf目录下。

perf利用CPU硬件寄存机统计硬件事件，如instructions executed, cache-misses suffered, or branches mispredicted。封装成简单命令用于统计linux上运行程序的性能。

## perf stat
obtain event counts
运行命令，收集性能统计数据

## perf record
record events for later reporting
运行命令，并且将profile生成到perf.data中。

## perf report
break down events by process, function, etc.
解析perf.data，输出profile

## perf annotate
annotate assembly or source code with event counts
Read perf.data (created by perf record) and display annotated code
使用perf.data统计汇编和源代码event counts

## perf top
see live event count

## perf bench
run different kernel microbenchmarks


# gprof

# 比较