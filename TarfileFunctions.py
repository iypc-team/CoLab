
# from __future__ import absolute_import
from IPython.display import clear_output
from BashColors import C
import glob, os, shutil, tarfile
import os.path

class TarfileFunctions:
    from IPython.display import clear_output
    from BashColors import C
    import glob, os, shutil, tarfile
    # from os.path import os.path.abspath, os.path.basename

    __all__ = ['listTarfiles', 'inspectTarfile', 'extractTarfiles', 'tarfileFromDirectory']
    global tff
    
    def __init__(self):
        # self.tff = None
        self.tff = TarfileFunctions
        self.rootPth=os.getcwd()
        self.tarfileList=list()
        self.tarfilePathList=list()
        
    def listTarfiles(self):
        print(f'Available tar files:')
        tarfile_list = glob.glob('**', recursive=True)
        for fil in sorted(tarfile_list):
            if fil.endswith('.gz'):
                fil=os.path.basename(fil)
                fullPth = os.path.abspath(fil)
                print(f'{C.IPurple}{fil}{C.ColorOff}')
                print(f'{C.Green}{fullPth}{C.ColorOff}\n')
                self.tarfileList.append(fil)
                self.tarfilePathList.append(fullPth)
            
    def tarfileFromDirectory(self,
                                   output_filename, source_dir):
        print(source_dir)
        print(os.path.basename(source_dir))
        with tarfile.open(output_filename, "w:gz") as tar:
            # pass
            tar.add(source_dir, arcname=os.path.basename(source_dir))

    def extractTarfiles(self, fileName):
        fil=os.path.basename(fileName)
        print(f'extracting: {fil}')
        tar = tarfile.open(fil, 'r:gz')
        tar.extractall()
        tar.close()

    def inspectTarfile(self, named):
        named=str(named)
        named=os.path.basename(named)
        print(named)
        tar = tarfile.open(named, "r:gz")
        for tarinfo in tar:
            print(f'{C.IPurple}{tarinfo.name}{C.ColorOff}')
            print('type:', tarinfo.type)
            print('chksum:', tarinfo.chksum)
            print('size:', tarinfo.size)
            print()
        tar.close()

tff = TarfileFunctions()