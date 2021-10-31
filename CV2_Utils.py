
import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob, os, uuid
from os.path import *
from time import sleep
from BashColors import C

try:
    from google.colab import drive, files
    from google.colab.patches import cv2_imshow
except: pass

try:
    pass
    # import tensorflow as tf
except ModuleNotFoundError as err:
    print(err)
    # %pip install tensorflow

class CV2_Utils:
    ''' '''
    __all__ = ['cvu','rootPth','contentPath','tfImagesPth','cv2ImagesPth',
               'cv2ImagePathList','tfImagePathList',
               'originalImageZeroPixel', 'zeroPixel']
    # __builtin__ = []

    def __init__(self):
        ''' '''
        self.cvu = CV2_Utils

        self.rootPth = expanduser("~")
        self.contentPath = os.getcwd()
        self.tfImagesPth = join(os.getcwd(), 'TensorflowImages')
        self.cv2ImagesPth = join(os.getcwd(), 'CV2Images')

        self.zeroPixel = np.ndarray([0, 0, 0, 0])
        self.originalImageZeroPixel = np.ndarray([0, 0, 0, 0])

    def __iter__(self):
         ''' '''
         for key in self.some_sequence:
            yield (key, 'Value for {}'.format(key))
            
    def flipImage2(self, thisImage, axes):
        '''hflp = flip(img, 0)\nvflp = flip(img, 1)\nbflp = flip(img,-1)'''
        if (axes == 0): # horizental flip
            print('hflp')
            return cv2.flip(thisImage, 0 )
        elif(axes == 1): # vertical flip
            print('vflp')
            return cv2.flip(thisImage, 1 )
        elif(axes == -1): # both directions
            print('bflp')
            return cv2.flip(thisImage, -1 )
        
    def saveCV2Image(self, path, img):
        cv2.imwrite(path, img)
        
    def loadCV2Image(self, path):
        '''IMREAD_UNCHANGED'''
        img=cv2.imread(path, cv2.IMREAD_UNCHANGED)
        return img
    
    def getCV2SavePath(self, path, append='', silent=True):
        ''' '''
        fileName=basename(path)
        fileName=fileName.replace('_', '')
        splitFileName=splitext(fileName)
        if append != '':
            fileName = splitFileName[0] + append + splitFileName[1]

        if path.__contains__('enemy'):
            newPath=join('/home/jovyan/CV2Images/Enemy/', fileName)
            if not silent:
                print(f'{C.IPurple}{path}')
                print(f'{C.IPurple}{fileName}')
                print(f'newPath: {C.Green}{newPath}{C.ColorOff}\n')
            return newPath
        
        elif path.__contains__('friendly'):
            newPath=join('/home/jovyan/CV2Images/Friendly/', fileName)
            if not silent:
                print(f'{C.IPurple}{path}')
                print(f'{C.IPurple}{fileName}')
                print(f'newPath: {C.Green}{newPath}{C.ColorOff}\n')
            return newPath

    def listCV2Images(self):
        cwd=os.getcwd()
        os.chdir(self.cv2ImagesPth)
        globList=glob.glob('**', recursive=True)
        fileCount=0
        for fil in sorted(globList):
            fullPath=abspath(fil)
            if fullPath.endswith('.png'):
                fileCount+=1
                print(fullPath)
        os.chdir(cwd)
        
    def fillImage3(self, thisImage, zp, silent=True):
        ''' '''
        if zp == np.ndarray([64,64,64,255]):
            pass
        original_image = np.copy(thisImage)
        img = np.copy(original_image)

        black = np.where((img[:,:,0]==0) & (img[:,:,1]==0) & (img[:,:,2]==0))

        white = np.where((img[:,:,0]==255) & (img[:,:,1]==255) & (img[:,:,2]==255))

        img[black] = (zp[0], zp[1], zp[2], zp[3])
        img[white] = (0, 0, 0, 0)

        if not silent:
            cvu.showTwoImages(original_image, img)
        return img

    def resizeImage(self, thisImage, newSize=(224,224)):
        '''return resized_image'''
        resized_image = cv2.resize(thisImage, newSize,
                                   interpolation=cv2.INTER_CUBIC)
        return resized_image

    def createCV2ImagesTarfile(self):
        ''' '''
        os.chdir(self.cv2ImagesPth)
        from TarfileFunctions import tff, tarfileFromDirectory
        thisDir = cvu.cv2ImagesPth
        if exists(thisDir):
            # print(thisDir)
            try: tff.tarfileFromDirectory(output_filename='CV2Images.tar.gz',
                                          source_dir=thisDir)
            except BaseException as err: print(err)

    def renameFileWithPath(self, path, append=''):
        '''return newPath'''
        file_path, extension = path.split('.')
        # print(f'file_path: {file_path}')
        # print(f'extension: {extension}')
        newPath = file_path + append + '.' + extension
        newPath = join(newPath)
        
        return newPath
        
    def showTwoImages(self, img1, img2):
        '''display two images with  CV2'''
        img1 = self.resizeImage(img1)
        img2 = self.resizeImage(img2)
        combinedImage = cv2.hconcat([img1, img2])
        try:
            cv2.waitKey(50)
            cv2.destroyAllWindows()
            cv2_imshow(combinedImage)
        except: 
            self.plotShowSingleImage(img1, img2)

    def plotShowSingleImage(self, thisImage, title1='', showAxis=False):
        ''' '''
        thisImage = cv2.cvtColor(thisImage, cv2.COLOR_BGR2RGBA)

        fig=plt.figure()
        ax1=fig.add_subplot(1,1,1)
        ax1.imshow(thisImage)
        if showAxis: ax1.axis('on')
        else: ax1.axis('off')
        ax1.set_title(title1)
        plt.show()

    def plotShowTwoImages(self, thisImage, compareImage,
                                title1='Original Image',
                                title2='', showAxis=False):
        ''' '''
        thisImage = cv2.cvtColor(thisImage, cv2.COLOR_BGR2RGBA)
        compareImage = cv2.cvtColor(compareImage, cv2.COLOR_BGR2RGBA)

        fig=plt.figure()
        ax1 = fig.add_subplot(1,2,1)
        ax1.imshow(thisImage)
        if showAxis: ax1.axis('on')
        else: ax1.axis('off')
        ax1.set_title(title1)

        ax2 = fig.add_subplot(1,2,2)
        ax2.imshow(compareImage)
        if showAxis: ax2.axis('on')
        else: ax2.axis('off')
        ax2.set_title(title2)
        plt.show()

    def createImageWithColor(self, pxColor, silent=True):
        '''return save_path'''
        bgImage = np.zeros(shape=[224,224,4], dtype=np.uint8)
        save_path = join(self.contentPath, 'bgImage.png')

        for px in bgImage:
            bgImage[:] = pxColor
            sleep(0.1)

        cv2.imwrite(save_path, bgImage)
        
        if not silent:
            print(f'shape: {bgImage.shape}')
            bgImage = cv2.imread(save_path, cv2.IMREAD_UNCHANGED)
            try:
                cv2_imshow(bgImage)
                cv2.waitKey(50)
                cv2.destroyAllWindows()
            except:
                self.plotShowSingleImage(bgImage)
        return save_path

    def zoomImage(self, thisImage, newScale=1, silent=True):
        '''return zoomImage'''
        zeroPixel = thisImage[0][0]
        angle = 0
        width, height, _ = thisImage.shape
        rotPoint = width//2, height //2
        dimentions = width, height
        rotPoint = width//2, height//2
        rotMatrix = cv2.getRotationMatrix2D(rotPoint, angle, scale=newScale)
        zoomImage = cv2.warpAffine(thisImage, rotMatrix, dimentions)
        zoomImage = self.cv2FillImage(zoomImage)
        if not silent:
            print('cv2ZoomImage()')
            self.plotCompareTwoImages(thisImage, zoomImage)
        return zoomImage

    def rotateImage(self, thisImage, angle=0, rotPoint=None,
                    newScale=1, silent=True):
        '''return rotImage'''
        thisImage = np.copy(thisImage)
        # self.originalImageZeroPixel = thisImage[0, 0]
        # print(thisImage.shape)
        width, height, _ = thisImage.shape
        if rotPoint == None:
            rotPoint = width//2, height//2
            rotMat = cv2.getRotationMatrix2D(rotPoint, angle, scale=newScale)
            dimentions = width, height
            rotImage = cv2.warpAffine(thisImage, rotMat, dimentions)
            # rotImageZeroPixel = rotImage[0][0]
            if not silent:
                print('cv2Rotation()')
                self.plotShowTwoImages(thisImage, rotImage)
                sleep(0.1)
            try:
                cv2.waitKey(50)
                cv2.destroyAllWindows()
            except:
                sleep(0.05)
                
            return rotImage

    def translateImage(self, thisImage, x=0, y=0, silent=True):
        '''-x shift left -y shift up\nx shift right y shift down\n
        return newImage'''
        thisImage = np.copy(thisImage)
        zeroPixel=thisImage[0][0]
        translateMatrix = np.float32([[1,0,x],[0,1,y]])
        dimentions = (thisImage.shape[1], thisImage.shape[0])
        newImage = cv2.warpAffine(thisImage, translateMatrix, dimentions)

        if not silent:
            print('cv2Translate()')
            self.plotCompareTwoImages(thisImage, newImage)

        try:
            cv2.waitKey(50)
            cv2.destroyAllWindows()
        except: pass
        return newImage

    def edgeDetection(self, thisImage, t1=50, t2=100, silent=True):
        '''return canny'''

        # gray = cv2.cvtColor(thisImage, cv2.COLOR_BGR2GRAY)
        # thisImage = cv2.GaussianBlur(gray,(3,3),0)

        canny = cv2.Canny(thisImage, t1, t2)
        if not silent:
            self.plotCompareTwoImages(thisImage, canny)
        try:
            cv2.waitKey(50)
            cv2.destroyAllWindows()
        except: pass
        return canny

    def changeBackgroundColors(self, path, image=None):
        '''returns newImg'''
        splitPath = split(path)
        filePath = splitPath[0]
        fileName = splitPath[1]
        fileName = 'new_' + fileName
        print(filePath)
        print(fileName)
        saveImagePath = join(contentPath, fileName)

        print(f'saveImagePath: {saveImagePath}')
        original_image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        originalZeroPixel = original_image[0][0]
        plt.imshow(original_image)
        newImg = np.copy(original_image)

        zeroPixel = newImg[0][0]
        print('newImg zeroPixel:', zeroPixel)
        print('originalZeroPixel:', originalZeroPixel)

        width, height, channels = original_image.shape
        print(width, height, channels)

        for x in range(0, width):
            for y in range(0, height):
                channels_xy = newImg[y][x]
                # print(channels_xy)
                if all(channels_xy == zeroPixel):
                    newImg[y][x] = originalZeroPixel

        cv2.imwrite(saveImagePath, newImg)
        newImg = cv2.imread(saveImagePath, -1)
        try:
            cv2.waitKey(50)
            cv2.destroyAllWindows()
        except: pass
        return newImg

    def cv2FillImage(self, thisImage, silent=True):
        '''returns filledImage'''
        print('cv2FillImage')
        # plotShowSingleImage(thisImage)
        zp = thisImage[0][0]
        bgImagePath = self.cv2CreateImageWithColor(pxColor=cvu.zeroPixel)
        # print(zp)
        img1 = np.copy(thisImage)
        img2 = cv2.imread(bgImagePath, cv2.IMREAD_UNCHANGED)
        filledImage = cv2.bitwise_or(img1, img2)
        filledImage = cv2.bitwise_or(filledImage, img2)
        if not silent:
            self.cv2ShowTwoImages(img1, filledImage)
        try:
            cv2.waitKey(50)
            cv2.destroyAllWindows()
        except Exception as err:
            print(err)
            sleep(0.05)
            img1=None
            img2=None
                
        return filledImage

    def addTwoImages(self, imagePath1, imagePath2, alfa=1, beta=1, gamma=0.0):
        '''return  addImage'''
        # read two imagePaths
        src1 = cv2.imread(imagePath1)
        src2 = cv2.imread(imagePath2)
        try:
            # add or blend the imagePaths
            addImage = cv2.addWeighted(src1, alfa, src2, beta, gamma)
            # save the output imagePath
            # cv2.imwrite('image.png', dst)
            return addImage
        except Exception as err:
            print(f'{C.IRed}{err}')

    def flipImage(self, thisImage, axes=0, silent=True):
        '''axes=0 flip vert\naxes=1 flip horiz\naxes=-1 flip vert and horiz'''
        if axes == 0:
            flipImg = cv2.flip(thisImage, 0)
            if not silent:
                print('_flipVert')
                self.showTwoImages(thisImage, flipImg)
        elif axes == 1:
            flipImg = cv2.flip(thisImage, 1)
            if not silent:
                print('_flipHorz')
                self.showTwoImages(thisImage, flipImg)
        elif axes == -1:
            flipImg = cv2.flip(thisImage, -1)
            if not silent:
                print('_flipVertAndHorz')
                self.showTwoImages(thisImage, flipImg)
        try:
            cv2.waitKey(50)
            cv2.destroyAllWindows()
        except: sleep(0.1)
        return flipImg

    def getUniqueFileName(self, uniquePrefix='_'):
        '''return uniqueName'''
        uniqueName = uniquePrefix + str(uuid.uuid4())
        return uniqueName
        
    def getNewSavePath(self, initialPath, new_path='', postfix='', silent=True):
        ''' '''
        if new_path=='':
            new_path = self.cv2ImagesPth + '/'
        
        directory, fileName = split(initialPath)
        # dirr, name, extension = splitext(directory)
        # print(initialPath)
        # print(directory)
        # print(fileName)
        _, subDir = split(directory)
        name, extension = splitext(fileName)
        # print(subDir)

        if not silent:
            print(f'{C.IWhite}')
            print(f'newPath: {new_path}')
            print(f'subDir: {subDir}')
            print(f'name: {name}')
            print(f'postfix: {postfix}')
            print(f'extension: {extension}')

        newSavePath = new_path + subDir + '/' + name + postfix + extension
        print(f'{C.IWhite}savePath: {C.IPurple}{newSavePath}{C.ColorOff}')
        return newSavePath

    def saveImage(self, savePath, thisImage, silent=True, save=False):
        ''' '''
        if not silent:
            print(f'{C.IWhite}saved to: {C.Green}{savePath}{C.ColorOff}')
            try: cv2_imshow(thisImage)
            except BaseException as err:
                self.plotShowSingleImage(thisImage,
                                            title=basename(savePath))

        if save and not exists(savePath):
            print(f'{C.IWhite}saved to: {C.Green}{savePath}{C.ColorOff}')
            cv2.imwrite(savePath, thisImage)

    def fillImage(self, thisImage, silent=True):
        ''' '''
        original_image = np.copy(thisImage)
        img = np.copy(original_image)

        black = np.where((img[:,:,0]==0) & 
                         (img[:,:,1]==0) & 
                         (img[:,:,2]==0))
        
        white = np.where((img[:,:,0]==255) & 
                         (img[:,:,1]==255) & 
                         (img[:,:,2]==255))
        
        img[black] = (255, 255, 255, 255)
        img[white] = (0, 0, 0, 255)
        
        if not silent:
            try:
                cvu.showTwoImages(original_image, img)
            except Exception as err:
                print(err)
        try:
            cv2.waitKey(50)
            cv2.destroyAllWindows()
        except:
            sleep(0.1)
        return img

    def rotateImagesFixed(self, thisPath, silent=True, save=False):
        '''Rotates images 90, 180, and 270 degrees fixed increments\n'''
        rotationList = ['90','180','270']
        for angleString in rotationList:
            newAngle=float(angleString)
            appendFileName= 'Rot' + angleString
            originalImg = self.loadCV2Image(thisPath)
            # originalImg = self.resizeImage(originalImg)
            rotImage = np.copy(originalImg)
            rotImage = self.rotateImage(rotImage, newAngle)
            savePath=''
            if not silent:
                savePath = self.getCV2SavePath(thisPath,
                                              append=appendFileName,
                                              silent=False)
                self.plotShowTwoImages(originalImg, rotImage,
                                      title2=basename(savePath))
            if save and not exists(savePath):
                print(f'{C.ColorOff}saved to: {C.Green}{savePath}{C.ColorOff}\n')
                self.saveCV2Image(savePath, rotImage)
            elif exists(savePath):
                print(f'{C.ColorOff}file already exists : {C.IRed}{savePath}{C.ColorOff}\n')
                    
cvu = CV2_Utils()
