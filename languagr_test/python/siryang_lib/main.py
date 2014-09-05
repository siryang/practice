# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename main.py

from basictype import *
import mercator
import imageop
import os

def test1():
    baidu = PointArray([Point(11640394, 3991461),
                        Point(11640444, 3990631),
                        Point(11642406, 3990714),
                        Point(11642457, 3991444)])

    mapbar = PointArray([Point(11639751, 3990880),
                         Point(11639789, 3990015),
                         Point(11641760, 3990115),
                         Point(11641802, 3990825)])

    baidu.sub(mapbar)
    #http://192.168.0.111/test/chargeLatLon.jsp?cp=116.39751,39.90880&igb=1&ogb=2
    mapbar.convert()
    baidu.sub(mapbar)


def test2():
    baidu = PointArray([Point(11640394, 3991461),
                        Point(11640444, 3990631),
                        Point(11642406, 3990714),
                        Point(11642457, 3991444),
                        Point(11640392, 3991406)])
    
    mapbar = PointArray([Point(11639751, 3990880),
                         Point(11639789, 3990015),
                         Point(11641760, 3990115),
                         Point(11641802, 3990825),
                         Point(11639756, 3990774)])

    baidu.sub(mapbar)
    #http://192.168.0.111/test/chargeLatLon.jsp?cp=116.39751,39.90880&igb=1&ogb=2
    mapbar.convert()
    baidu.sub(mapbar)
    
if __name__ == "__main__":
    print ""
    test2()
    print os.getcwd();
    
#    mercX = mercator.merc_x(116.32466)
#    mercY = mercator.merc_y(39.961028)
#
#    print "(%f, %f)" % (mercX, mercY)  
#    pos = Point(11640394,3991461)
#    pos.show();
    
    
    
    
