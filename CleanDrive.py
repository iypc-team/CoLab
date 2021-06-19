# 12/29/2020
from __future__ import absolute_import
import os, shutil
from os.path import *
from google.colab import drive, files

class CleanDrive:
    """class CleanDrive removes '/content/sample_data' directory"""
    global cd
    def __init__(self):
        self.cd=None
        self.contentPth = '/content'
        self.removePth = '/content/sample_data'

    def showDrive(self):
        """showDrive method"""
        files.view(self.contentPth)

    def cleanDrive(self):
        """cleanDrive method"""
        if exists(self.removePth):
            shutil.rmtree(self.removePth)
        else: self.showDrive()

cd = CleanDrive()
cd.cleanDrive()