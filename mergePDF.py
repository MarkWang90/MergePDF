# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:22:29 2018

Automated PDF processing

@author: markp
"""

import PyPDF2
import os
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

class pdfmerger():
    def __init__(self):
        self.n_files = input("number of files to be merged: ")
        nf = int(self.n_files)
        self.path = askdirectory(title = "Select folder", mustexist = True)
        self.pdfs = ['']*nf
        os.chdir(self.path)
        for i in range(nf):
            self.pdfs[i]=askopenfilename(title = f"Select {i}th PDF: ")
        self.savename = input("Name of merged file: ")
        
    def merge(self):
        pdfWriter = PyPDF2.PdfFileWriter()
        for file in self.pdfs:
            pdfFile = open(file,'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            for page in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(page)
                pdfWriter.addPage(pageObj)
            pdfOutputFile = open(self.savename, 'wb')
            pdfWriter.write(pdfOutputFile)   
            pdfFile.close()
        pdfOutputFile.close()

        
merger = pdfmerger()
merger.merge()
