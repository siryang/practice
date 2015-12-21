


### Events

* Click - 用户点击鼠标时触发
* DblClick - 用户双击鼠标时触发
* MouseDown - 用户按下鼠标键触发 (click事件前半部分)
* MouseUp - 用户释放鼠标键触发 (click事件后半部分)
* MouseOut - 当鼠标指针离开对象物理边界时触发
* MouseOver - 当鼠标指针进入对象物理边界时触发
* MouseMove -当鼠标指针在对象物理边界内移动时触发
* ContextMenu - 用户点击鼠标右键时触发


### Data Type

JavaScript只有5中基本数据类型。

* number
* bool
* string
* null
* undefined

JS的变量作用域都是整个函数，后声明的变量也可以提前使用
undefined值在布尔类型环境中会被当作false。

所以有 ``` map.zoom = option.zoom || 9; // 如果option.zoom未定义, 则设置为默认值9```

### 转义字符

Character	Meaning
\b	Backspace
\f	Form feed
\n	New line
\r	Carriage return
\t	Tab
\v	Vertical tab
\'	Apostrophe or single quote
\"	Double quote
\\	Backslash character (\).
\XXX	The character with the Latin-1 encoding specified by up to three octal digits XXX between 0 and 377. For example, \251 is the octal sequence for the copyright symbol.
\xXX	The character with the Latin-1 encoding specified by the two hexadecimal digits XX between 00 and FF. For example, \xA9 is the hexadecimal sequence for the copyright symbol.
\uXXXX	The Unicode character specified by the four hexadecimal digits XXXX. For example, \u00A9 is the Unicode sequence for the copyright symbol. See Unicode escape sequences.

### 运算符

`"3" == 3`, return true; 判断值相等
`"3" === 3`, return false; 判断值和类型都相等
`!===`, 值或类型不相等
`>>>`, 高位补零右移
`"Dog" && "Cat"; return "Cat";` A&&B中,A为false则返回A,否则返回B。
`'Dog' && 'Cat'; return 'Dog';` A||B中,A为true则返回A,否则返回B。

[JS运算符优先级](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Operator_Precedence#Table)


### 特殊标识符

`use strict`:JS的严格模式。

function(){}();立即执行的匿名函数。最后一个()代表立即执行。

### 优化
1. 避免循环引用，导致JS-GC无法自动回收。
2. 动态修改Objecet属性类型会导致hash表重置，影响性能，所以尽量避免。
3. `delete a` 和 `a = null`的区别，前者是强制释放内存，后者是引用计数-1.要尽量使用null，因为2。

