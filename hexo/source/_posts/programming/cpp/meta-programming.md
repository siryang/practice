title: Modern C++ Design(1)
date: 2014-06-04 15:29:59
categories:
- cpp
tags: 
- reading
- template
- cpp
---


###特化与偏特化
支持`成员函数特例化`，不支持`成员函数偏特化`
{% codeblock 特化与偏特化 lang:cpp %}
    template <class T> 
    class Widget
    {
        void Fun() { .. generic implementation ... }
    };

    // OK: specialization of a member function of Widget
    // 
    template <> void Widget<char>::Fun() // 譯註：原文少了 void
    {
        ... specialized implementation ...
    }

    template <class T, class U> class Gadget
    {
        void Fun() { .. generic implementation ... }
    };

    // Error! Cannot partially specialize a member class of Gadget
    // 譯註 : 因為這是 member function 的 Explicit specialization 並無 partial
    // specialization機制。注意這和class templates 不同! 參見 C++ Primer,16.9 節
    // 
    template <class U> void Gadget<char，U>::Fun()
    {
        ... specialized implementation ...
    }
{% endcodeblock %}

--------------------------------------

###Policies和Policy Classes

`OpNewCreator`和`MallocCreator`是策略类，`WidgetManager`可以选择使用何种策略

{% codeblock 策略类 lang:cpp %}
template <class T>
struct OpNewCreator
{
    static T* Create()
    {
        return new T;
    }
};

template <class T>
struct MallocCreator
{
    static T* Create()
    {
        void* buf = std::malloc(sizeof(T));
        if (!buf) return 0;
        return new(buf) T;
    }
};

// OpNewCreator和MallocCreator（策略）称为CreationPolicy（策略集）
// WidgetManager继承CreationPolicy
// Library code
template <class CreationPolicy>
class WidgetManager : public CreationPolicy
{ ... };

typedef WidgetManager< OpNewCreator<Widget> > MyWidgetMgr;


// Library code
// class Created是CreationPolicy的形式参数，所以可以忽略
template <template <class /*Created*/> class CreationPolicy>
class WidgetManager : public CreationPolicy<Widget>
{ ... };


typedef WidgetManager<OpNewCreator> MyWidgetMgr;
{% endcodeblock %}



{% blockquote %}
{% endblockquote %}

---------------------------------------


{% codeblock instance_eval lang:ruby%}
{% endcodeblock %}

1.Created<Type>
2.

