# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename convert84And02.py

import urllib
from basictype import Point

def conver02to84(pos):
    result = Point()
    response = urllib.urlopen("http://192.168.0.111/test/chargeLatLon.jsp?cp=%f,%f&igb=2&ogb=1" % (pos.m_x / 100000.0, pos.m_y / 100000.0))
    html = response.readlines();
    for line in html:
        #
        if line.startswith("out"):
            line = line[line.find("=") + 1: line.rfind(";")]
            line = line.split(",")
            result.m_x = int(float(line[0]) * 1E5)
            result.m_y = int(float(line[1]) * 1E5)
            return result
        

def conver84to02(pos):
    result = Point()
    response = urllib.urlopen("http://192.168.0.111/test/chargeLatLon.jsp?cp=%f,%f&igb=1&ogb=2" % (pos.m_x / 100000.0, pos.m_y / 100000.0))
    html = response.readlines();
    for line in html:
        #
        if line.startswith("out"):
            line = line[line.find("=") + 1: line.rfind(";")]
            line = line.split(",")
            result.m_x = int(float(line[0]) * 1E5)
            result.m_y = int(float(line[1]) * 1E5)
            return result
                

    
        

