
## cut

```
echo "aaa,bbb,ccc" | cut -d ',' -f1
# output : aaa
```

```
echo "123456" | cut -b2-5
# output : 2345
```

## sed

```
echo "libmapcore.so(function + 123)" | sed 's/ //g; s/[()+]/ /g'
# 1. remove ' '.
# 2. replace '()+' to ' '.
```

## printf

```
printf "%d" 0xa
# output: 10

printf "%x" 10
# output: 0xa
```