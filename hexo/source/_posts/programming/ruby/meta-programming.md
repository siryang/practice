title: meta-programming in ruby
date: 2014-05-27 08:09:49
categories:
- Ruby
tags: 
- meta-programming 
- ruby
---

{% blockquote %}
元编程最通俗的解释就是用代码生成代码
静态元编程和动态元编程的区别是后者可以在程序在运行时生成代码
{% endblockquote %}

---------------------------------------


####instance_eval
`instance_eval`接收块作为参数，把调用对象置换成`self`来执行，所以`@name=`变成了`self.@name=`
{% codeblock instance_eval lang:ruby%}
class User
    attr_accessor :name, :passwd
    
    def initialize(&block)
        instance_eval(&block)
    end

    def show
        puts "name:#{@name}, passwd:#{@passwd}"
    end
end

def main()
    user = User.new{
        @name = "sir"
        @passwd = "yang"	
    }

    user.show
    user.show_name
    user.show_passwd
end

main
{% endcodeblock %}

######Output
	name:sir, passwd:yang
	sir
	yang





####class_eval
{% codeblock class_eval lang:ruby%}
class User
    def User.my_attr(*names)
        names.each{|n|
            class_eval %{
                def show_#{n}()
                    puts @#{n}
                end
            }
        }
    end
    my_attr :name, :passwd
end
{% endcodeblock %}


####method_missing
