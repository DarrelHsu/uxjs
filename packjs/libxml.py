#!/usr/bin/python
#
#  Lib file for read and write xml of  packjs
#  Author : Darrel
#  msn   : xdarui@xdarui.com
#

from xml.dom import minidom
from sys import argv
import toolbox
import re

class BuildXml:
    """This a lib class for packjs     """
    def __init__(self,filename=None):
        if not filename :
            print "Error : filename is nessary"
        else:
            sock = toolbox.openAnything( filename )
            self.xml = minidom.parse( sock )
            sock.close()
            if not self.xml :
                print "Error : file is not exists"
                exit()
    def getProject(self,n):
        pj = self.getTag(self.xml,'project')
        if len(pj) == 0:
            print "Error : project is not defined in xml file !"
        else:
            self.projects = pj
            self.project = pj[n]
            default = self.getTag(self.xml,'default')
            #
            if not default :
                self.getTarget( pj[n] )
                self.__p__ = 0
            else:
                self.target = default.attributes['target'].value      
                self.__p__ =  default.attributes['project'].value
        return pj
    def getTargetName( self , target ) :
        return target.attributes["name"].value 
    def getTarget(self,pj):
        self.getTargetAt( pj , 0 )
    def getTargetAt( self , pj , index ): 
        if not pj:
           print "Error : no project selected !"
        else :
            tg = self.getTag( pj , 'target' )
            if len( tg ) < index + 1 :
                self.target = None 
            else :
                self.target = tg[ index ].attributes['name'].value ;
    def getTag(self,tag,name):
        if tag:
            return tag.getElementsByTagName(name) 
        else:
            return None
    def getDest(self,target):
        #if len(argv) >= 2 :
        #    target = argv[2]
        #else :
        #    target = None
        #print target 
        #exit();
        ct = self.getTag(self.project,'target')
        if target:
            for t in ct:
                if t.attributes['name'].value == target : d = t;
        else:
            d =  ct[0]
        basedir = self.project.attributes['basedir'].value
        concat = self.getTag(d,"concat")[0]
        desc = concat.attributes['destfile'].value
        paths = self.getTag( concat , "path" )
        urls = [] ;
        for i in range( len( paths ) ) :
           path = paths[i];
           urls.append( path.attributes["path"].value.replace("${basedir}",basedir) )
        return desc.replace("${basedir}",basedir) , urls
        
    def nextProject(self):
        if len(self.projects) < self.__p__ + 1:
            print "Error : Projects list out of bound"
        else:
            self.project = self.projects[self.__p__] 
