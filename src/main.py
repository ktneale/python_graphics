#!/usr/bin/python
#
# Written by Kevin Neale 2015
#
# Demonstrates usage of a simple graphics library written for Python
#
# To install this lib:
#
# 1) Download from: http://mcsp.wartburg.edu/zelle/python/graphics.py
# 2) $ sudo cp ~/Downloads/graphics.py /usr/local/lib/python3.4/dist-packages/
# 3) $ sudo apt-get install python3-tk
#
# Run using Python3

from graphics import *

def main():
    win = GraphWin("My Circle", 800, 600)
    #c = Circle(Point(400,300), 250)
    #c.setFill('black')
    #c.draw(win)


    ring_width = 5
 
    previous_colour = 'white'
    count = 300
    while (count >= ring_width):
        c = Circle(Point(400,300), count)

        if ( previous_colour == 'black'):
            c.setFill('white')
            previous_colour = 'white'
        else:
            c.setFill('black')
            previous_colour = 'black'

        c.draw(win)
        count = count - ring_width;

    win.getMouse() # pause for click in window
    win.close()

main()
