title: C
date: 2014-06-24 11:06:41
tags: C
---

### 浮点数

	IEEE-754标准的浮点数由`符号位`,`阶码`，`尾数`组成。
	尾数域所表示的值是1.M（存储的是M）
	阶码用移码表示法
	* 单精度格式（32位）：符号位（S）1位；阶码（Ｅ）8位，阶码的偏移量为127（7FH）；尾数（M）23位，用小数表示，小数点放在尾数域的最前面；
	* 双精度格式（64位）：符号位（S）1位；阶码（Ｅ）11位，阶码的偏移量为1023（3FFH）；尾数（M）52位，用小数表示，小数点放在尾数域的最前面。

	X = (-1)s×(1.M)×2^E-127       e = E-127

``` c
	for (int i = 0; i < 0x7FFFFF; i++)
	{
		float j = i;
		CQ_ASSERT(i == (int)j);
	}

	void breakFloat(float f, int* s, int* e, int* m)
	{
		int temp = *(int*)(&f);
		*s = temp >> 31;
		*e = ((temp >> 23) & 0xFF) - 127;
		*m = temp & 0x7FFFFF;
		int test = (1 << *e) + (*m >> (23 - *e));
		CQ_ASSERT(test == (int)f);
	}
```

浮点数总结：把表示这个数字的二进制码，从前往后，找到第一个1，从下一位开始保存到尾数。再将尾数总位数（值）保存到阶码中。
所以，尾数拥有的位数能表示的精度都可以精确表示（即第一个1到最后一个1之间的位数小于等于尾数）

### 优化

``` c
    const char* p = a + 3; // good
00291073  mov         eax,dword ptr [a]
00291076  add         eax,3
00291079  mov         dword ptr [p],eax
    const char* q = &a[3]; // bad
0029107C  mov         ecx,1
00291081  imul        edx,ecx,3
00291084  add         edx,dword ptr [a]
00291087  mov         dword ptr [q],edx
```

### 语法
enum class/struct EnumType: uint32 {};


