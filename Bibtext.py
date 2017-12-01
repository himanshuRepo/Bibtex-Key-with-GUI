#!/usr/bin/env python

"""
Code for generating the bibtex key from Google Scholar for the list of papers, whose names are stored
    in the excel sheet.


Author: Himanshu Mittal (himanshu.mittal224@gmail.com)
Referred: https://github.com/venthur/gscholar
"""

import Tkinter
from Tkinter import *
import extract

def fetchKey():
	extract.extractr(Entry1.get())


mainwindow = Tkinter.Tk()

Tkinter.Label(mainwindow,text = "Path To Excel File:").grid(row=0)

Entry1 = Tkinter.Entry(mainwindow)

Entry1.grid(row=0,column=1)

Entry1.focus()

Tkinter.Button(mainwindow,text = 'Fetch',command = fetchKey).grid(row=3, column =0)
Tkinter.Button(mainwindow, text='Close', command=mainwindow.destroy).grid(row=3, column =1)

mainwindow.mainloop()