# Tool box
A collection of tools commonly used, keep updating...

## Table of Contents
1. [merge pdfs](#mergepdf)
2. [find large files](#largefiles)

## 1. **mergePDF.py**: A little program to merge PDF using PyPDF2 <a name='mergepdf'></a>

1. Enter the # of PDF files to be merged: 
<img src="https://github.com/MarkWang90/MergePDF/blob/master/pic/fig1.PNG" alt="Fig. 1" width="500">
2. Enter the folder where the final PDF to be saved:
<img src="https://github.com/MarkWang90/MergePDF/blob/master/pic/fig2.PNG" alt="Fig. 1" width="500">
3. Select the PDF files one by one:
<img src="https://github.com/MarkWang90/MergePDF/blob/master/pic/fig3.PNG" alt="Fig. 1" width="500">
<img src="https://github.com/MarkWang90/MergePDF/blob/master/pic/fig4.PNG" alt="Fig. 1" width="500">

4. Enter the name of the merged file:
<img src="https://github.com/MarkWang90/MergePDF/blob/master/pic/fig5.PNG" alt="Fig. 1" width="500">



## 2. **findlargefile.py**: find files under a specific folder above certain size <a name='largefiles'></a>
* filesize in MB
* location gives the path (sub-path auto added)
```python
filesize = 30
location = r'D:\GDrive\water\RioGrande_MakeData_Mark'

if __name__ == '__main__':
    print('This program searches for ...')
    print('Files larger than %d MB in location: %s' % (filesize, location))
    for filename, size in search_folder(location, filesize):
        print(filename)
```
