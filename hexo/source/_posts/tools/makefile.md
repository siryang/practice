


## 自定义表达式

``` makefile
.PHONY:all

define show
	cd subdir && pwd # subdir @要在其它目录执行某个命令时，要使用&&连接
	pwd # not subdir
    echo $(1)
endef

str:= 123

all:
    echo $(call show, $(str))
    echo "begin"
```

## 获取指定目录中的c/cpp文件

``` makefile
my_sources := $(shell find $(SOURCE_DIR) | grep -v $(JNI_SOURCE_DIR) | egrep "\.c$(str_end)|\.cpp$(str_end)")
my_objs := $(patsubst %.c,%.o, $(my_sources))
my_objs := $(patsubst %.cpp,%.o, $(my_objs))
## 下面两句应该可以合并
```
