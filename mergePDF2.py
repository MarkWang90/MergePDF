# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 10:56:16 2018

@author: markp
"""

import PyPDF2
import os
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

class pdfmerger():
    def __init__(self):
        
        self.path = askdirectory(title = "Select folder", mustexist = True)
        os.chdir(self.path)
        self.methods = input("methods: 1 - merge all under a folder; 2 - select files: ")
        
        if self.methods == '2':
            self.n_files = input("number of files to be merged: ")
            nf = int(self.n_files)
        
            self.pdfs = ['']*nf
            os.chdir(self.path)
            for i in range(nf):
                self.pdfs[i]=askopenfilename(title = f"Select {i}th PDF: ")
                
        if self.methods == '1':
            self.pdfs = [elem for elem in os.listdir(self.path) if elem.endswith('.pdf')]
            
            
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
