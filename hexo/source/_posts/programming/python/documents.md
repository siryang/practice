title: Python基础
date: 2014-06-09 18:51:49
categories:
- Python
tags: 
- python
---

##Grammar

*   for
```python
for w in words[1:-1]:
     print w, len(w),
myArray = range(2,5)

myArray = [i for i in range(2,5)]
```
-------
##Interface
###Basic
*   raw_input
*   DataStructure
    *   Array
    ```PYTHON
    enumerate
    ```
    
    *   Tuples
    ```PYTHON
    zip(list1, list2)
    ```
    
    *   Sequences
    *   Sets
    *   Dictionaries

###Inheritance
```python
class Child(module.Parent):
    def __init__(self, other):
        module.Parent(self)
```

###muti-thread
>CPython implementation detail: In CPython, due to the Global Interpreter Lock, only one thread can execute Python code at once (even though certain performance-oriented libraries might overcome this limitation). If you want your application to make better use of the computational resources of multi-core machines, you are advised to use multiprocessing. However, threading is still an appropriate model if you want to run multiple I/O-bound tasks simultaneously.
CPython实现详情：在CPython中，由于`GIL(Global Interpreter Lock)`的原因，同一时刻只有一个线程在执行。如果期望更好利用计算机的多核性能，建议使用`multiprocessing`,而多线程则更多应用于IO并发。

```python
import threading
class MyThread(threading.Thread):
    def run():
        #do task here
def main():
    thread = MyThread()
    thread.start()
    thread.join()
```

###muti-processing

####多进程
*   通信
*   同步
*   运行方式
    *   async:异步调用
    *   apply:apply(function, args) == function(args)
    *   map: 同map
    *   imap: 

```python
import multiprocessing

def worker(num):
    """thread worker function"""
    print 'Worker:', num
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
```

---------
##Functional Programming Tools
```python
filter(function, list1, list2) 
map(function, list1, list2)
reduce(function, list)
sum(function, list)

[x**2 for x in range(10)]
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```

```python
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
```


----------