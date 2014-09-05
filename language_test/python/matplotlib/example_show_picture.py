# -*- coding: cp936 -*-
#import numpy
#from matplotlib import * 
from pylab import *

#zhfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\meiryo.ttc')
x = arange(0,11, 1)
y = 3 + x - x
plot(x, y)

x = arange(10, 15, 1)
y = 5 + x - x
plot(x, y)

x = arange(15, 20, 1)
y = 3 + x
plot(x, y)
#title(u'roowe',fontproperties=zhfont)
#savefig('roowe.png', dpi=75)
#grid on
show()
