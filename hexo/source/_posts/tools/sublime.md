

---

## 快捷键

`Ctrl+D`:Expand Secection to Word, 向下选中相同单词
`Ctrl+L`:Expand Secection to Line, 向下选中一行
`Alt+三指`:列选择

### 编程相关快捷键

`Cmd+g`: go to definition.

### 功能：


* 1.python控制台
    使用Ctrl+`打开

* 2.Package Control安装
    打开python控制台，输入以下代码

    ``` python
    import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
    ```

    Ctrl+Shift+P后搜索install，选择Package Control:Install Packet可以安装插件

* 3.安装自定义ColorTheme
    a.Preferences --> Browse Package
    b.解压到打开的目录
    c.Perferences --> Color Scheme --> User

* 4.Add Repository

    Add a repository that is not included in the default channel. This allows users to install and automatically update packages from GitHub and BitBucket. To add a package hosted on GitHub, enter the URL in the form https://github.com/username/repo. Don’t include .git at the end! BitBucket repositories should use the format https://bitbucket.org/username/repository.


## 问题：

* 1.Sublime破解 - http://bbs.pediy.com/showthread.php?t=182774

* 2.Sublime中文乱码
    * a.打开ANSI编码中文文档乱码
        ANSI(Windows-1252)显示中文乱码 - 使用Package Control：Install Packet安装ConvertToUTF8插件，即可解决
    * b.打开的文件的文件名中文乱码
    * c.ruby程序输出中的中文乱码
        用winrar打开“安装目录\\Packages"目录中Ruby.sublime-package
        修改其中Ruby.sublime-build，增加"encoding": "GBK"（windows命令行返回的字符编码）
        上面的改法，会导致UTF-8文本无法正常输出，最好是仍改回utf-8(默认)，并且将其他字符转码成utf-8

* 3.编译执行ruby时，gets()无法交互
* 4.sublime默认不支持ini文件高亮 https://github.com/clintberry/sublime-text-2-ini
* 5.编译Python无法输出中文，同2-c中方法，修改Python.sublime-build增加 "encoding": "cp936"后解决
* 6.安装Node到/usr/local/bin后，无法编译，错误输出是path中没有/usr/local/bin

>   问题已解决：
    方法是不用Sublime的Package Contol安装，而直接安装github上的文件，并修改Nodejs.sublime-setting文件解决。

>   问题仍未解决，尝试了以下途径
    * a.增加/etc/launchd.conf文件，内容为`setenv PATH /usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`未解决
    * b.增加~/.bash_profile文件，内容为
        `
        export PATH=$PATH:/usr/local/bin
        launchctl setenv PATH $PATH
        `
        未解决
    * c.修改Sublime的Preference的NodeJS用户设置，将node_command设置为绝对路径，未解决
