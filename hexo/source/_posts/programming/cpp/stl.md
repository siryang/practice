
### vector<bool>

``` cpp
bool in[] = { true, true, false, false };

vector<bool> a;
a.assign(&in[0], &in[0] + element_of(in));

// bool* m = &a[0]; // compile error;

reverse(a.begin() + 1, a.begin() + 3); // recommend

// reverse(&a[0], &a[3]); // error

//STL对vector<bool>做了特例化，所以&a[0]的类型不是bool*，而且用其调用reverse的结果也是未知的

```



