#!/usr/bin/env python
# 
# Example use of method light()
#
import vtkplotter

vp = vtkplotter.Plotter()

cow = vp.load('data/cow.g', c='grey', alpha=.7)

vp.plane(pos=[0,-3.6,0], normal=[0,1,0], sx=20, texture='grass')

# vp.light() returns a vtkLight object with focal point, fp, to actor cow
# fp can also be explicitly set as fp=[x,y,z]
l = vp.light(pos=[-6,6,6], fp=cow, deg=12, showsource=1)

# can be switched on/off this way
#l.SwitchOff()

vp.show()


