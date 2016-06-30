## Shell脚本语法

### 执行参数

    $0 param 1  #命令自身
    $1 param 2
    $2 param 3
    $3 param 4
    $# param number
    $@ all params

```shell

while getopts ":dh" opt;
do
    case $opt in
        h)
            echo "-h"
            ;;
        d)  echo "-d";;
        ?)  echo "invalid";;
    esac
done

```

### 判断

注意用`=`不是`==`。

``` shell
if [ "$var" = "" ] || [ "$var2" = "" ] ; then
    echo "empty string"
fi
```

### 函数

```shell
function system_info
{
    echo "<h2>System release info</h2>"
    echo "<p>Function not yet implemented</p>"

}   # end of system_info
```
