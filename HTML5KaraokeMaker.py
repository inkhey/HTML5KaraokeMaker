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

# sys
import sys
import os
# translate
import locale
import gettext
# settings
from setting import *
from maker import Maker
# other
import shutil
import logging
logging.basicConfig()

# init translation


def initTranslation():
    ''' init Translation with gettext'''

    lang = gettext.NullTranslations()
    try:
        lang = gettext.translation(APP, localedir=LOCALE_DIR)
    except IOError:
        pass
    lang.install()


def translateArgparse(Text):
    ''' to Translate argparse module'''

    Text = Text.replace("usage", _("usage"))
    Text = Text.replace("show this help message and exit",
                        _("show this help message and exit"))
    Text = Text.replace("error:", _("error:"))
    Text = Text.replace("the following arguments are required:",
                        _("the following arguments are required:"))
    Text = Text.replace("too few arguments",
                        _("too few arguments"))
    Text = Text.replace("optional arguments",
                        _("optional arguments"))

    return Text

initTranslation()
gettext.gettext = translateArgparse
import argparse


class HTML5kKaraokeMaker(object):

    "CLI interface of HTML5kKaraokeMaker"

    def readCli(self):
        '''CLI:Argument parser'''

        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-p',
            '--webpath',
            help=_("use a local web path file"),
            default=D_WEB_DIR
        )
        parser.add_argument(
            '-d',
            '--datapath',
            help=_("use a local data path file"),
            default=D_DATA_DIR
        )
        parser.add_argument(
            '-o',
            '--output',
            help=_("choose a specific output directory"),
            default=D_WEB_DIR
        )
        self.args = parser.parse_args()
        return True

    def __init__(self, logLevel=LOGLEVEL):
        ''' Launch CLI'''

        self.logger = logging.getLogger("HTML5kKaraokeMaker")
        self.logger.setLevel(logLevel)

        if self.readCli():
            self.maker = Maker(self.args.webpath,self.args.datapath)
            self.maker.make()
            self.saveFile()
        else:
            print(_("Interface error"))

    def __str__(self):
        '''Print text'''

        if self.maker:
            return str(self.maker)
        else:
            return _("No file")

    def saveFile(self):

        #copy needed data
        audioPath=self.args.output+'/audio'
        dependPath=self.args.output+'/depend'
        if os.path.exists(audioPath):
            shutil.rmtree(audioPath)
        if os.path.exists(dependPath):
            shutil.rmtree(dependPath)
        shutil.copytree('data/audio','web/audio')
        shutil.copytree('data/depend','web/depend')

        with open(self.args.output+"/index.html", "w+") as doc:
            doc.write(self.__str__())


if __name__ == '__main__':

    k = HTML5kKaraokeMaker()
