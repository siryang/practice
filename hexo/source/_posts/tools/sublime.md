

---

## ��ݼ�

`Ctrl+D`:Expand Secection to Word, ����ѡ����ͬ����
`Ctrl+L`:Expand Secection to Line, ����ѡ��һ��
`Alt+��ָ`:��ѡ��

### �����ؿ�ݼ�

`Cmd+g`: go to definition.

### ���ܣ�


* 1.python����̨
    ʹ��Ctrl+`��

* 2.Package Control��װ
    ��python����̨���������´���

    ``` python
    import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
    ```

    Ctrl+Shift+P������install��ѡ��Package Control:Install Packet���԰�װ���

* 3.��װ�Զ���ColorTheme
    a.Preferences --> Browse Package
    b.��ѹ���򿪵�Ŀ¼
    c.Perferences --> Color Scheme --> User

* 4.Add Repository

    Add a repository that is not included in the default channel. This allows users to install and automatically update packages from GitHub and BitBucket. To add a package hosted on GitHub, enter the URL in the form https://github.com/username/repo. Don��t include .git at the end! BitBucket repositories should use the format https://bitbucket.org/username/repository.


## ���⣺

* 1.Sublime�ƽ� - http://bbs.pediy.com/showthread.php?t=182774

* 2.Sublime��������
    * a.��ANSI���������ĵ�����
        ANSI(Windows-1252)��ʾ�������� - ʹ��Package Control��Install Packet��װConvertToUTF8��������ɽ��
    * b.�򿪵��ļ����ļ�����������
    * c.ruby��������е���������
        ��winrar�򿪡���װĿ¼\\Packages"Ŀ¼��Ruby.sublime-package
        �޸�����Ruby.sublime-build������"encoding": "GBK"��windows�����з��ص��ַ����룩
        ����ĸķ����ᵼ��UTF-8�ı��޷����������������ԸĻ�utf-8(Ĭ��)�����ҽ������ַ�ת���utf-8

* 3.����ִ��rubyʱ��gets()�޷�����
* 4.sublimeĬ�ϲ�֧��ini�ļ����� https://github.com/clintberry/sublime-text-2-ini
* 5.����Python�޷�������ģ�ͬ2-c�з������޸�Python.sublime-build���� "encoding": "cp936"����
* 6.��װNode��/usr/local/bin���޷����룬���������path��û��/usr/local/bin

>   �����ѽ����
    �����ǲ���Sublime��Package Contol��װ����ֱ�Ӱ�װgithub�ϵ��ļ������޸�Nodejs.sublime-setting�ļ������

>   ������δ���������������;��
    * a.����/etc/launchd.conf�ļ�������Ϊ`setenv PATH /usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`δ���
    * b.����~/.bash_profile�ļ�������Ϊ
        `
        export PATH=$PATH:/usr/local/bin
        launchctl setenv PATH $PATH
        `
        δ���
    * c.�޸�Sublime��Preference��NodeJS�û����ã���node_command����Ϊ����·����δ���
