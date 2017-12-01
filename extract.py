#!/usr/bin/env python

"""
Code for generating the bibtex key from Google Scholar for the list of papers, whose names are stored
    in the excel sheet.


Author: Himanshu Mittal (himanshu.mittal224@gmail.com)
Referred: https://github.com/venthur/gscholar
"""

import optparse
import sys
import os
# import xlsxwriter
import pandas as pd
import gscholar as gs

def extractr(filePath):

    # Path to the excel sheet containing the list of paper title in the second colum, heading as 'Name'.
    pathToFile=filePath

    xl = pd.ExcelFile(pathToFile)
    df = xl.parse("Sheet1")
    bt = []
    f=df['PaperName']
    for i in range(f.size):
        a1=f[i]
        x1 = a1.replace(u'\xa0', ' ')
        args1=x1.encode('ascii','ignore')
        # args ="Detection of skin cancer by classification of Raman spectra"
        biblist = gs.query(args1)
        print(biblist[0])
        k=biblist[0]
        k1 = k.replace(u'\n ', ' ')
        x2=k1.encode('ascii','ignore')
        x2=x2.decode('utf-8')
        bt.append(x2)
    df1 = pd.DataFrame({'bibtex': bt})
    f=pd.concat([df, df1], axis=1)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('bibtexFile.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    f.to_excel(writer, sheet_name='Sheet1')

    writer.save()


    # # Get the xlsxwriter objects from the dataframe writer object.
    # workbook  = writer.book
    # worksheet = writer.sheets['Sheet1']
    # workbook.close()



if __name__ == "__main__":
    pathToFile="PaperList.xlsx"
    extractr(pathToFile)