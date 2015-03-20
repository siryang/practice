### 列编辑模式

[参考](http://sharkyan.blog.51cto.com/536264/283982)

Ctrl+v 进入列视图模式
方向键选中文本
I 进入插入模式模式/ R 进入修改模式/ D 删除选中块
输入结束后，ESC两次，结束插入

### 问题
1. 备份用的~结尾文件用途，能否去掉
2. Python自动build
3. Python运行及Debug

### VIMRC

    set nu
    set tabstop/ts=4
    set guifont/gfn=Consolas:h10:cANSI
    syntax enable
    syntax on

tips:
    输入`set ts`然后`tab`会自动补全为`tablestop`
    输入`set ts=`然后`tab`会自动补全成当前设置

### 插件

TAG:

* 1.build

    cd my_source_directory
    ctags -R .
    :set tags=abs_path\tags

* 2.run
    
    C+]
    C+t



