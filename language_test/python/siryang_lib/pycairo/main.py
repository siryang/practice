#!/usr/bin/python

'''
ZetCode PyCairo tutorial 

This program uses PyCairo to 
produce a PNG image.

author: Jan Bodnar
website: zetcode.com 
last edited: August 2012
'''

import cairo
        
def main():
    
    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, 390, 160)
    cr = cairo.Context(ims)
    
    cr.set_source_rgb(0, 0, 0)
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
        cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(40)
    
    cr.move_to(10, 50)
    cr.show_text("Disziplin ist Macht.")
    
    cr.set_source_rgb(0, 0, 0);
    cr.set_line_width(1)
    cr.move_to(0,0)
    cr.line_to(100, 100)
    
    
    cr.set_source_rgb(0, 0, 0)
    cr.set_line_width(0.5)
        
    for i in self.coords:
        for j in self.coords:
            cr.move_to(i[0], i[1])
            cr.line_to(j[0], j[1]) 
            cr.stroke()

    del self.coords[:]   

    ims.write_to_png("image.png")
        
        
if __name__ == "__main__":    
    main()
    
    