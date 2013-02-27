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


global outfile , infile , filetype , MODE
GCC = "/lib/compiler.jar"
YUI = "/lib/yuicompressor-2.4.2.jar"
LIB =  os.path.dirname(__file__)
def getFileName (  ) :
    global outfile , infile , filetype , MODE
    if infile[-4:] == '.css':
        MODE = 'YUI'
        outfile,number = re.subn('.css$','.min.css',infile)
        filetype = "css" 
    else:
        outfile,number = re.subn('.[Jj][Ss]$','.min.js',infile)
def getParams( args ):
  global outfile , infile ,  MODE , filetype
  for arg in args :
    if arg == '--yui' :
      MODE = "YUI"
    elif os.path.isfile( arg ) :
      infile = arg
    else :
      outfile = arg
  if infile[-4:] == '.css' :
    MODE = 'YUI'
    filetype = 'css'
  if outfile is None :
    getFileName()
def Main( args ) :
  global outfile , infile , filetype , MODE
  infile = outfile = params =  None
  MODE = "GCC"
  filetype = 'js'
  if len(args) < 1 :
      print "input file is need !"
      return 254
  else:
      getParams( args )
      print "Start to compile with mode : %s for  %s " % ( MODE , outfile )
      if MODE == 'GCC' :
          cmdline = "java -jar %s  --js_output_file=%s --js=%s"
          MODE = GCC 
      else:
          MODE = YUI
          cmdline = "java -jar %s --type "+ filetype +" --charset utf-8 -o %s %s"
      cmdline = cmdline % ( LIB + MODE , outfile , infile  )
      result = os.system( cmdline )
      return result
if __name__ == '__main__' :
    ot = Main( argv[1:] ) 
    print "Success ! "
    exit( ot )
