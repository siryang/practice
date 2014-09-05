from pylab import *

## write point
def writePoint():
    plot(11571461, 3957120, "bo");
    plot(11571528, 3957106, "bo");
    plot(11571541, 3957103, "bo");
    plot(11571554, 3957100, "bo");
    plot(11571592, 3957090, "bo");
    plot(11571669, 3957071, "bo");
    plot(11571734, 3957055, "bo");
    show();


##
def writeBar():
    xlabel(u"Sexly")
    ylabel(u"Number")
    xticks((0, 1, 2),(u'A', u'B', u'C'))
    bar(left = 0, height = 1, width = 0.5, align="center")
    bar(left = 1, height = 10, width = 0.5, align="center")
    bar(left = 2, height = 7, width = 0.5, align="center")
    show()


writeBar();
59564008844
