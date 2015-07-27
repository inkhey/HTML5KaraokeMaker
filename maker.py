#!/usr/bin/python
# -*- coding: utf-8 -*-
#  HTML5KaraokeMaker
#
#  Copyright 2015 Guénaël Muller <contact@inkey-art.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
import logging
import setting
import configparser
import re
import csv
from decimal import *
logging.basicConfig()

class Maker(object):

    """Make karaoke"""


    def __init__(self,webpath,datapath,logLevel=setting.LOGLEVEL):

        #logger
        self.logger = logging.getLogger("Maker")
        self.logLevel = logLevel
        self.logger.setLevel(logLevel)
        #file
        self.webpath = webpath
        self.datapath = datapath
        self._openModel()
        self.config = configparser.ConfigParser()
        self.config.read(self.datapath+'/global.ini')

    def _openModel(self):
        with open(self.datapath+"/model.html", "r") as doc:
            self.doc=doc.read()

    def _replace(self,word):
        tmp=self.config['DEFAULT'][word]
        if tmp:
            tmp=str(tmp)
            self.doc=self.doc.replace('['+word+']',tmp)

    def make(self):

        #usable word
        listWord=['title','subtitle','mp3file','oggfile','wavfile',
            'footer']
        listWord.extend(['initaudiomsg','error','audioerrormsg',
        'formaterrormsg','speederrormsg','jserrormsg','speedratemsg'])
        for word in listWord:
            self._replace(word)

        getcontext().prec = 7
        tmpKaraokeStr="\n"
        for elem in self.config.sections():
            tmpfile=self.config[elem]['file']
            try:
                heading=self.config[elem]['heading']
            except:
                heading=""
            if heading:
                tmpKaraokeStr+="<h3 class=\"section-heading\">"
                tmpKaraokeStr+=str(heading)+"</h3>\n"

            tmpKaraokeStr+="<p>\n"
            with open(self.datapath+"/"+tmpfile) as csvfile:
                fieldnames = ['begin', 'end','word']
                reader = csv.DictReader(csvfile,delimiter='\t',
                                    fieldnames=fieldnames)
                for row in reader:
                    beginStr=row['begin'].replace(",",".")
                    begin=Decimal(beginStr)
                    endStr=row['end'].replace(",",".")
                    end=Decimal(endStr)
                    dur=end-begin
                    tmpKaraokeStr+="\t<span data-dur="+str(dur)+" "
                    tmpKaraokeStr+="data-begin="+str(begin)+">"
                    tmpKaraokeStr+=row['word']+"</span>"
                    tmpKaraokeStr+="\n"
            tmpKaraokeStr+="</p>\n"
        self.doc=self.doc.replace('[sections]',tmpKaraokeStr)

    def __str__(self):
        return self.doc

if __name__ == '__main__':

        m=Maker("/web","./data")
        m.make()
        print (m)
