#!/usr/bin/python
from os import listdir
import os
from pypdfocr.pypdfocr import PyPDFOCR
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

onlyfiles = []
for f in listdir('Desktop/PDF/'):
	if f.endswith('.pdf'):
		onlyfiles.append(f)

if __name__ == '__main__':
	for f in onlyfiles:
                
		file_name = os.path.abspath(f)
		file_name_arr = file_name.split('\\')
		file_name_arr.insert(3, "Desktop\PDF")
		file_name = "\\".join(file_name_arr)
		file_name2 = file_name
		converter = PyPDFOCR()
		converter.go([file_name])
		print "yes"
		file_name_arr = file_name.split(".pdf")
		file_name = "_ocr.pdf".join(file_name_arr)
		rsrcmgr = PDFResourceManager()
		retstr = StringIO()
		codec = 'utf-8'
		laparams = LAParams()
		device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
		fp = file(file_name, 'rb')
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		password = ""
		maxpages = 0
		caching = True
		pagenos=set()
		
		for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
			interpreter.process_page(page)
			text = retstr.getvalue()

		fp.close()
		device.close()
		str = retstr.getvalue()
		retstr.close()
		print f
		text_arr=text.split("\n")
		newfile = text_arr[0]
		text_arr = newfile.split("/")
		newfile="".join(text_arr)
		text_arr = newfile.split("\"")
		newfile="".join(text_arr)
		text_arr = newfile.split("*")
		newfile="".join(text_arr)
		text_arr = newfile.split(":")
		newfile="".join(text_arr)
		text_arr = newfile.split("@")
		newfile="".join(text_arr)
		text_arr = newfile.split("?")
		newfile="".join(text_arr)
		text_arr = newfile.split("<")
		newfile="".join(text_arr)
		text_arr = newfile.split(">")
		newfile="".join(text_arr)
		newfilename ="".join([newfile,"-",f])
		new_file = os.path.join("Desktop/PDF/Renamed PDF", newfilename)
		print newfile
		print newfilename
		print new_file
		print file_name
		os.rename(file_name, new_file)
		#os.remove(os.path.join(os.getcwd(),f))
                os.remove(file_name2)

	
