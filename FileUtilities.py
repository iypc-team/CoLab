# 09/07/2020

import glob, os, pathlib, sys
from os.path import *
from pathlib import Path
from importlib import reload

from BashColors import C
import TZInfo
from TZInfo import *

class FileUtilities:
    __all__ = sorted(['allFiles', 'allFilesDict', 'cwdPath', 'homePath', 
           'fu', 'inspectFile', 'listFiles', 'printSystemPaths', 
           'setSystemPaths', 'updateAllFiles'])
    
    def __init__(self):
        self.C = C
        self.homePath = Path.home()
        self.cwdPath = Path.cwd()
        self.allFiles = glob.glob('**', recursive=True)
        self.allFilesDict = {}

    def updateAllFiles(self):
        self.allFiles = glob.glob('**', recursive=True)

    def setSystemPaths(self, addNewPath, quit=True):  
        addNewPath = realpath(addNewPath)
        pathList = sys.path.copy()
        if not addNewPath in pathList and exists(addNewPath):
            sys.path.append(addNewPath)

    def listFiles(self, silent=False):
        self.updateAllFiles()
        self.allFiles = sorted(self.allFiles)
        tempDict = self.allFilesDict
        fileCount = 0
        if not silent:
            print(f'{C.IBlue}{self.cwdPath}')
        self.setSystemPaths(addNewPath=self.cwdPath)
        for fil in self.allFiles:
            fullPath = Path(realpath(fil)) # POSIX path
            realPath = realpath(fil) # String path
            if isdir(fullPath) and not realPath.__contains__('__pycache__'):  
                if not silent:
                    print(f'\n{C.IBlue}{fullPath}')
                self.setSystemPaths(addNewPath=realPath) 
            elif isfile(fullPath) and not realPath.__contains__('__pycache__'): 
                fileCount += 1
                filStats = tzi.getFileStats(realPath)
                if not silent:
                    print(f'{C.IWhite}{fileCount}. {fullPath.name}')
                    print(f'{C.Cyan}{filStats}')
                tempDict[fileCount] = fullPath
                self.allFilesDict = {}
                self.allFilesDict.update(tempDict)

    def inspectFile(self, selection):
        if selection <= len(self.allFilesDict):  
            try:
                pth = self.allFilesDict[selection]  
                with open(pth, 'r') as openFile:  
                    print(f'# %%writefile {pth.name}\n')  
                    print(openFile.read())
            except:
                print(f'{C.Red}BULLSHIT')

    def printSystemPaths(self):
        pathList = sys.path.copy() 
        pathCount = 0
        for pth in sorted(pathList):
            pathCount += 1
            print(f'{C.IWhite}{pathCount}. {C.IBlue}{pth}')

fu = FileUtilities()
fu.listFiles(silent=True)