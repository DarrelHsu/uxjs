#!/usr/bin/python
#
# This a js compressor
# You can use it as a single command or import into your project as a library
#
#
#
#
#
from sys import argv
import os
import re


GCC = "/lib/compiler.jar"
YUI = "/lib/yuicompressor-2.4.2.jar"
LIB =  os.path.dirname(__file__)
MODE = "GCC"
filetype = 'js'
infile = outfile = params = None;
def getFileName (  ) :
    global outfile , infile , filetype , MODE
    if infile[-4:] == '.css':
        MODE = 'YUI'
        outfile,number = re.subn('.css$','.min.css',infile)
        filetype = "css" 
    else:
        outfile,number = re.subn('.[Jj][Ss]$','.min.js',infile)
if len(argv) < 2 :
	print "input file is need !"
	exit()
else:
    params = argv 
    params.pop(0)
    infile = params.pop(0)
    if infile == '--yui' :
        MODE = 'YUI'
        infile = params.pop(0)
    if len( params ) >= 1 :
        if params[-1] == '--yui':
            MODE = 'YUI'
            params.pop(-1);
            if len( params ) == 0 :
               getFileName() 
            else :
                outfile = params.pop()
        else :
            outfile = params.pop()
            if infile[-4:] == '.css' :
                MODE = 'YUI'
                filetype = 'css'
    else :
        getFileName()
    print "Start to compile with mode : " + MODE 
    if MODE == 'GCC' :
        cmdline = "java -jar %s  --js_output_file=%s --js=%s"
        MODE = GCC 
    else:
        MODE = YUI
        cmdline = "java -jar %s --type "+ filetype +" --charset utf-8 -o %s %s"
    cmdline = cmdline % ( LIB + MODE , outfile , infile  )
    os.system( cmdline )

print "Success ! The desinate file this " + outfile

