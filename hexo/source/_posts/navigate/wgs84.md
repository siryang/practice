title: GCJ-02坐标
date: 2014-06-11 15:41
categories:
- Navigate
tags: 
- WGS84
---

## 
由中国国家测绘局制订的地理信息系统的坐标系统，常被称为火星坐标。
所有的电子地图和所有的导航设备，都需要加入国家保密插件。这样GPS导航仪和电子地图就能完全匹配，导航仪仍能正常工作。


``` c
< %codeblock lang:cpp GCJ-02坐标和百度BD-09坐标转换 http://blog.woodbunny.com/post-68.html %>
#include <math.h>  

const double x_pi = 3.14159265358979324 * 3000.0 / 180.0;  
  
void bd_encrypt(double gg_lat, double gg_lon, double &bd_lat, double &bd_lon)  
{  
    double x = gg_lon, y = gg_lat;  
    double z = sqrt(x * x + y * y) + 0.00002 * sin(y * x_pi);  
    double theta = atan2(y, x) + 0.000003 * cos(x * x_pi);  
    bd_lon = z * cos(theta) + 0.0065;  
    bd_lat = z * sin(theta) + 0.006;  
}  
  
void bd_decrypt(double bd_lat, double bd_lon, double &gg_lat, double &gg_lon)  
{  
    double x = bd_lon - 0.0065, y = bd_lat - 0.006;  
    double z = sqrt(x * x + y * y) - 0.00002 * sin(y * x_pi);  
    double theta = atan2(y, x) - 0.000003 * cos(x * x_pi);  
    gg_lon = z * cos(theta);  
    gg_lat = z * sin(theta);  
}  
```
##参考
[GCJ-02_百度百科](http://baike.baidu.com/link?url=4mvEGZjtGFkON8WChTERKxFiIWVRGcegAJz5J8LME3z2TYu_dxYZnqZqIE47mNZ9fpwQ_u12vV9ANB9Qk1VaDq)
