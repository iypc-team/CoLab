# 12/05/2020
from __future__ import absolute_import
import os, shutil, sys
from os.path import *
from glob import glob
from pathlib import Path
from BashColors import C

class ColabDriveFiles:
    '''List all files in Collab '''
    def __init__(self):
        self.cdf=None
        self.contentPth='/content'
        self.drivePth='/content/drive'
        self.myDrivePth='/content/drive/My Drive'
        self.pythonFilesPth='/content/drive/My Drive/PythonFiles'

        self.allDirectoriesDict={}
        self.allFilesDict={}
        self.allFiles=self.updateFileList().copy()

    def clearAllCaches(self, silent=True):
        '''clear all __pycache__ and content'''
        all_files = self.allFiles
        for fil in all_files:
            if isdir(fil) and fil.__contains__('__pycache__'):
                cache_pth=realpath(fil)
                if not silent:
                    print(f'{C.IRed}{cache_pth}')
                shutil.rmtree(fil)
            else: pass

    def cleanDrive(self):
        '''removes sample_data directory and contents'''
        os.chdir('/content')
        delete_path='/content/sample_data'
        if exists(delete_path):
            shutil.rmtree(delete_path)
            self.updateFileList()
        else: pass

    def updateFileList(self):
        '''Updates self.allFiles'''
        os.chdir('/content')
        file_list=glob('**', recursive=True)
        return file_list

    def listColabFiles(self, silent=False):
        '''List all files available in Collab
        populate self.allDirectoriesDict
        populate self.allFilesDict'''
        dirCount=1
        dirDict={}
        fileCount=0
        fileDict={}
        self.updateFileList()
        if not '/content' in sys.path.copy():
            sys.path.append('/content')
        if dirCount==1 and dirDict=={}:
            dirDict[1]='/content'
        else: pass
        if not silent:
            print(f'{C.Blue}{Path.cwd()}')
        for fil in sorted(self.allFiles):
            fullPath=abspath(fil)
            if isdir(fullPath) and not fullPath.__contains__('__pycache__'):
                if not fullPath in sys.path.copy():
                    sys.path.append(fullPath)
                dirCount+=1
                dirDict[dirCount]=fullPath
                if not silent:
                    print(f'\n{C.Blue}{fullPath}')
            elif isfile(fullPath) and not fullPath.__contains__('__pycache__'):
                fileCount+=1
                fileDict[fileCount]=fullPath
                if not silent:
                    print(f'{C.White}{fileCount}. {basename(fullPath)}')
        self.allDirectoriesDict=dirDict.copy()
        self.allFilesDict=fileDict.copy()

    def printSystemPaths(self):
        '''list system paths'''
        pathCount=0
        sysPaths=sys.path.copy()
        sysPaths=sorted(sysPaths)
        for pth in sysPaths:
            pathCount+=1
            print(f'{pathCount}. {C.Blue}{pth}')

cdf=ColabDriveFiles()