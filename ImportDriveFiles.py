# 11/10/2020
import glob, os, shutil
from pathlib import Path
from os.path import abspath
from google.colab import drive

class ImportDriveFiles:
    '''Import files to Colab Google Drive'''
    def __init__(self):
        # self.idf=None
        self.contentPath='/content'
        self.drivePath='/content/drive'
        self.myDrivePath='/content/drive/My Drive'
        self.pythonFilesPath='/content/drive/My Drive/PythonFiles'
        self.importFileList=None
        if os.path.exists(self.pythonFilesPath):
            os.chdir(self.pythonFilesPath)
            self.importFileList=glob.glob('*.py')
            self.importFiles()
            os.chdir(self.contentPath)
        else:
            print('path not exist\nMounting google drive')
            drive.mount(self.drivePath, force_remount=True)
            os.chdir(self.pythonFilesPath)
            self.importFileList=glob.glob('*.py')
            self.importFiles()
            os.chdir(self.contentPath)

    def importFiles(self):
        for fil in sorted(self.importFileList):
            sourcePath=abspath(fil)
            destinationPath=os.path.join(self.contentPath, fil)
            shutil.copy(sourcePath, destinationPath)

idf=ImportDriveFiles()