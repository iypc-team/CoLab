# 11/04/2020-3
from __future__ import absolute_import, print_function
from IPython.display import clear_output
import os
from pathlib import Path
import tensorflow as tf

class GetTPU:
    '''Initializes Colab TPU Cluster'''
    from google.colab import drive
    from pathlib import Path
    import os
    import tensorflow as tf

    def __init__(self):
        '''Initialize class GetTPU'''
        self.contentPath = '/content/drive'
        self.myDrivePath = '/content/drive/My Drive'
        self.gt = None
        self.tpu = None
        self.tpu_strategy = None
        
    def getMyDrive(self):
        '''Changes directory to /content/drive/My Drive'''
        os.chdir(self.myDrivePath)

    def mountGoogleDrive(self):
        '''Mount Google Drive at /content/drive'''
        from google.colab import drive
        drive.mount('/content/drive', force_remount=True)

    def copyToContent(self):
        from shutil import copyfile
        from os.path import exists, join
        os.chdir(self.myDrivePath)
        sourcePath = join(self.myDrivePath, 'BashColors.py')
        destinationPath = join(self.contentPath, 'BashColors.py')
        if exists(sourcePath):
            # print(f'source: {sourcePath}\ndestination: {destinationPath}')
            copyfile(sourcePath, destinationPath)
        

    def startTPU(self, clearOutput=True):
        '''start TPU cluster  '''
        self.tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
        tf.config.experimental_connect_to_cluster(self.tpu)
        tf.tpu.experimental.initialize_tpu_system(self.tpu)
        self.tpu_strategy = tf.distribute.TPUStrategy(self.tpu)
        if clearOutput:
            clear_output(wait=0)

    def getTPUStrategy(self):
        '''returns TPU strategy '''
        return self.tpu_strategy

    def stopTPU(self):
        '''stops TPU cluster '''
        tf.tpu.experimental.shutdown_tpu_system()

gt = GetTPU()