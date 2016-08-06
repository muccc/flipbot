# -*- coding: utf-8 -*-

import willie.module

 
font7px={
    "lineheight":7,
    "whitespace":0,
    "A": [
    [0,0,0,0,0],
    [0,1,1,0,0],
    [1,0,0,1,0],
    [1,1,1,1,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    ],
    "B": [
    [0,0,0,0,0],
    [1,1,1,0,0],
    [1,0,0,1,0],
    [1,1,1,0,0],
    [1,0,0,1,0],
    [1,1,1,0,0],
    ],
    "C": [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [0,1,1,1,0],
    ],
    "D": [
    [0,0,0,0,0],
    [1,1,1,0,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [1,1,1,0,0],
    ],
    "E": [
    [0,0,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,1,1,0],
    ],
    "F": [
    [0,0,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    ],
    "G": [
    [0,0,0,0,0,0],
    [0,1,1,1,0,0],
    [1,0,0,0,0,0],
    [1,0,0,1,1,0],
    [1,0,0,0,1,0],
    [0,1,1,1,0,0],
    ],
    "H": [
    [0,0,0,0,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [1,1,1,1,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    ],
    "I": [
    [0,0],
    [1,0],
    [1,0],
    [1,0],
    [1,0],
    [1,0],
    ],
    "J": [
    [0,0,0,0],
    [0,0,1,0],
    [0,0,1,0],
    [0,0,1,0],
    [1,0,1,0],
    [0,1,0,0],
    ],
    "K": [
    [0,0,0,0],
    [1,0,1,0],
    [1,0,1,0],
    [1,1,0,0],
    [1,0,1,0],
    [1,0,1,0],
    ],
    "L": [
    [0,0,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,1,1,0],
    ],
    "M": [
    [0,0,0,0,0,0],
    [1,0,0,0,1,0],
    [1,1,0,1,1,0],
    [1,0,1,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    ],
    "N": [
    [0,0,0,0,0],
    [1,0,0,1,0],
    [1,1,0,1,0],
    [1,0,1,1,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    ],
    "O": [
    [0,0,0,0,0],
    [0,1,1,0,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [0,1,1,0,0],
    ],
    "P": [
    [0,0,0,0,0],
    [1,1,1,0,0],
    [1,0,0,1,0],
    [1,1,1,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    ],
    "Q": [
    [0,0,0,0,0],
    [0,1,1,0,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [0,1,1,0,0],
    ],
    "R": [
    [0,0,0,0,0],
    [1,1,1,0,0],
    [1,0,0,1,0],
    [1,1,1,0,0],
    [1,0,1,0,0],
    [1,0,0,1,0],
    ],
    "S": [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [1,0,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,0],
    [1,1,1,0,0],
    ],
    "T": [
    [0,0,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,1,0,0],
    ],
    "U": [
    [0,0,0,0,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [0,1,1,1,0],
    ],
    "V": [
    [0,0,0,0,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [0,1,0,1,0],
    [0,0,1,1,0],
    [0,0,0,1,0],
    ],
    "W": [
    [0,0,0,0,0,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,1,0,1,0],
    [1,1,0,1,1,0],
    [1,0,0,0,1,0],
    ],
    "X": [
    [0,0,0,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,1,0,0],
    [1,0,1,0],
    [1,0,1,0],
    ],
    "Y": [
    [0,0,0,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,1,0,0],
    ],
    "Z": [
    [0,0,0,0,0],
    [1,1,1,1,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,1,0,0,0],
    [1,1,1,1,0],
    ],
    "Ä": [
    [1,0,0,1,0],
    [0,0,0,0,0],
    [0,1,1,0,0],
    [1,0,0,1,0],
    [1,1,1,1,0],
    [1,0,0,1,0],
    ],
    "Ö": [
    [1,0,0,1,0],
    [0,0,0,0,0],
    [0,1,1,0,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [0,1,1,0,0],
    ],
    "Ü": [
    [1,0,0,1,0],
    [0,0,0,0,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [1,0,0,1,0],
    [0,1,1,0,0],
    ],
    "-": [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [1,1,1,0],
    [0,0,0,0],
    [0,0,0,0],
    ],
    "?": [
    [0,1,1,0],
    [1,0,1,0],
    [0,0,1,0],
    [0,1,0,0],
    [0,0,0,0],
    [0,1,0,0],
    ],
    "!": [
    [0,0],
    [1,0],
    [1,0],
    [1,0],
    [0,0],
    [1,0],
    ],
    "\"": [
    [0,0,0,0],
    [1,0,1,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    ],
    "$": [
    [0,0,1,0,0],
    [0,1,1,1,0],
    [1,0,1,0,0],
    [0,1,1,0,0],
    [0,0,1,1,0],
    [1,1,1,0,0],
    ],
    "%": [
    [0,0,0,0,0],
    [1,0,0,1,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,1,0,0,0],
    [1,0,0,1,0],
    ],
    "&": [
    [0,0,0,0,0],
    [0,1,0,0,0],
    [1,0,1,0,0],
    [0,1,0,0,0],
    [1,0,1,0,0],
    [0,1,0,1,0],
    ],
    "/": [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [0,0,1,0,0],
    [0,1,0,0,0],
    [1,0,0,0,0],
    ],
    "\\": [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    ],
    "(": [
    [0,0,0],
    [0,1,0],
    [1,0,0],
    [1,0,0],
    [1,0,0],
    [0,1,0],
    ],
    ")": [
    [0,0,0],
    [1,0,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [1,0,0],
    ],
    "=": [
    [0,0,0],
    [0,0,0],
    [1,1,0],
    [0,0,0],
    [1,1,0],
    [0,0,0],
    ],
    "`": [
    [0,0,0],
    [1,0,0],
    [0,1,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    ],
    "+": [
    [0,0,0,0],
    [0,0,0,0],
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [0,0,0,0],
    ],
    "-": [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [1,1,1,0],
    [0,0,0,0],
    [0,0,0,0],
    ],
    "#": [
    [0,0,0,0,0,0],
    [0,1,0,1,0,0],
    [1,1,1,1,1,0],
    [0,1,0,1,0,0],
    [1,1,1,1,1,0],
    [0,1,0,1,0,0],
    ],
    ".": [
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [1,0],
    ],
    " ": [
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    ],
    ",": [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,1,0],
    [0,1,0],
    [1,0,0],
    ],
    ";": [
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    ],
    ":": [
    [0,0],
    [0,0],
    [1,0],
    [0,0],
    [1,0],
    [0,0],
    ],
    "_": [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [1,1,0],
    ],
    "'": [
    [0,0],
    [1,0],
    [1,0],
    [0,0],
    [0,0],
    [0,0],
    ],
    "*": [
    [0,0,0,0,0,0],
    [0,0,1,0,0,0],
    [1,0,1,0,1,0],
    [0,1,1,1,0,0],
    [1,0,1,0,1,0],
    [0,0,1,0,0,0],
    ],
    "'": [
    [0,0,0],
    [0,1,0],
    [1,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    ],
    "^": [
    [0,0,0,0],
    [0,1,0,0],
    [1,0,1,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    ],
    "<": [
    [0,0,0],
    [0,0,0],
    [0,1,0],
    [1,0,0],
    [0,1,0],
    [0,0,0],
    ],
    ">": [
    [0,0,0],
    [0,0,0],
    [1,0,0],
    [0,1,0],
    [1,0,0],
    [0,0,0],
    ],
    "[": [
    [0,0,0],
    [1,1,0],
    [1,0,0],
    [1,0,0],
    [1,0,0],
    [1,1,0],
    ],
    "]": [
    [0,0,0],
    [1,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [1,1,0],
    ],
    "|": [
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    ],
    "\n": [
    [],
    [],
    [],
    [],
    [],
    [],
    ],    
    "1": [
    [0,0,0],
    [0,1,0],
    [1,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    ],
    "2": [
        [0,0,0,0],
        [0,1,0,0],
        [1,0,1,0],
        [0,0,1,0],
        [0,1,0,0],
        [1,1,1,0],
    ],
    "3": [
        [0,0,0,0],
        [1,1,0,0],
        [0,0,1,0],
        [0,1,0,0],
        [0,0,1,0],
        [1,1,0,0],
    ],
    "4": [
        [0,0,0,0],
        [0,0,1,0],
        [0,1,0,0],
        [1,0,0,0],
        [1,1,1,0],
        [0,1,0,0],
    ],
    "5": [
        [0,0,0,0],
        [1,1,1,0],
        [1,0,0,0],
        [1,1,0,0],
        [0,0,1,0],
        [1,1,0,0],
    ],
    "6": [
        [0,0,0,0],
        [0,1,1,0],
        [1,0,0,0],
        [1,1,0,0],
        [1,0,1,0],
        [0,1,0,0],

    ],
    "7": [
        [0,0,0,0],
        [1,1,1,0],
        [0,0,1,0],
        [0,1,0,0],
        [0,1,0,0],
        [0,1,0,0],
    ],
    "8": [
        [0,0,0,0,0],
        [0,1,1,0,0],
        [1,0,0,1,0],
        [0,1,1,0,0],
        [1,0,0,1,0],
        [0,1,1,0,0],
    ],
    "9": [
        [0,0,0,0],
        [0,1,0,0],
        [1,0,1,0],
        [0,1,1,0],
        [0,0,1,0],
        [1,1,0,0],
    ],
    "0": [
        [0,0,0,0],
        [0,1,0,0],
        [1,0,1,0],
        [1,0,1,0],
        [1,0,1,0],
        [0,1,0,0],
    ],
        }


import socket

class FlipdotMatrix():
    def __init__(self,
                 udpHostsAndPorts = [("localhost", 2323)],
                 imageSize=(11*16, 20),
                 transposed = False
                 ):
        self.__sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        self.transposed = transposed
        self.udpHostsAndPorts=udpHostsAndPorts
        self.numberOfMatrixes = len(udpHostsAndPorts)
        self.MatrixSize = (imageSize[0]/self.numberOfMatrixes, imageSize[1])
        self.flipdotImage = FlipdotImage.newBlackFlipdotImage(imageSize[0], imageSize[1])
    
    def resetAll(self):
        """
        flip every pixel at least once, end with cleared Matrix
        """
        width = self.flipdotImage.width
        height = self.flipdotImage.height
        whiteImage = FlipdotImage.newWhiteFlipdotImage(width, height)
        blackImage = FlipdotImage.newBlackFlipdotImage(width, height)
        self.show(whiteImage)
        self.show(blackImage)
    
    def __showSerializedArrayOfPixels(self, imageArray, udpHostAndPort):
        udpPacket = FlipdotMatrix.__arrayToPacket(imageArray) 
        self.__sendUdpPackage(udpPacket, udpHostAndPort)
    
    def show(self, image):
        """
        send FlipdotImage to display. fills up with black pixels
        """
        self.__clearFlipdotImageWithoutUpdate()
        self.flipdotImage.blitImageAtPosition(image)
        self.__updateFlipdotMatrixes()

    def showBlit (self, image, xPos=0, yPos=0):
        """
        send FlipdotImage to display, keeps old pixels around
        """ 
        self.flipdotImage.blitImageAtPosition(image, xPos, yPos)
        self.__updateFlipdotMatrixes()

    def __updateFlipdotMatrixes(self):
        for i in range(self.numberOfMatrixes):
            MatrixSize = self.MatrixSize
            xOffset = i*MatrixSize[0]
            yOffset = 0
            flipdotImage = FlipdotImage.NewPartOfAnotherFlipdotImage(self.flipdotImage, newSize=MatrixSize, offset=(xOffset, yOffset))
            serializedImageArray = flipdotImage.serializeImageArray(self.transposed)
            udpHostAndPort = self.udpHostsAndPorts[i]
            self.__showSerializedArrayOfPixels(serializedImageArray, udpHostAndPort)
    
    def clear(self):
        """
        clears display. fills with black pixels
        """
        self.__clearFlipdotImageWithoutUpdate()
        self.__updateFlipdotMatrixes()
    
    def __clearFlipdotImageWithoutUpdate(self):
        width = self.flipdotImage.width
        height = self.flipdotImage.height
        self.flipdotImage = FlipdotImage.newBlackFlipdotImage(width, height)

    def showText(self, text, linebreak = False, xPos=0, yPos = 0):

        """
        print text to display
        """
        self.__clearFlipdotImageWithoutUpdate()
        self.flipdotImage.blitTextAtPosition(text, linebreak, xPos, yPos)
        self.__updateFlipdotMatrixes()

    def showBlitText(self, text, linebreak=False, xPos=0, yPos=0):
        """
        print text to display, keeps old pixels around
        """
        self.flipdotImage.blitTextAtPosition(text, linebreak, xPos, yPos)
        self.__updateFlipdotMatrixes()

    @staticmethod
    def __arrayToPacket(imageArray):
        return str(bytearray([FlipdotMatrix.__list2byte(imageArray[i*8:i*8+8]) for i in range(len(imageArray)/8)]))
    
    @staticmethod
    def __list2byte(ArrayOfBinaryInts):
        byte  = 0
        for i in range(8):
            byte += 2**(7-i) if not ArrayOfBinaryInts[i] else 0
        return byte

    def __sendUdpPackage(self, udpPacket, udpHostAndPort):
        self.__sock.sendto(udpPacket, udpHostAndPort)
        


class FlipdotImage(object):
    BLACKPIXEL = 0
    WHITEPIXEL = 1

    def __init__(self, pixel2DArray):
        self.width = len(pixel2DArray[0])
        self.height = len(pixel2DArray)
        self.rowArrayOfLineArraysOfPixels =  pixel2DArray

    def blitImageAtPosition(self, flipdotImage, xPos=0, yPos=0):
        for lineNr in range(self.height):
            newImageLineNr = lineNr-yPos
            if newImageLineNr >= 0 and flipdotImage.height > newImageLineNr:
                self.__blitLineAtPosition(flipdotImage, lineNr, newImageLineNr, xPos, yPos)
    
    def __blitLineAtPosition(self, flipdotImage, lineNr, newImageLineNr, xPos, yPos):
        for rowNr in range(self.width):
            newImageRowNr = rowNr - xPos
            if newImageRowNr >= 0 and flipdotImage.width > newImageRowNr:
                self.rowArrayOfLineArraysOfPixels[lineNr][rowNr] = flipdotImage.rowArrayOfLineArraysOfPixels[newImageLineNr][newImageRowNr]

    def blitTextAtPosition(self, text, autoLineBreak = False, xPos = 0, yPos = 0, __indentXPos=None):
        if __indentXPos==None:
            __indentXPos = xPos

        if len(text) <= 0:
            return
        
        letterImage = self.__getLetterImageForNextLetter(text)
        
        if self.__isLineBreakRequired(text, autoLineBreak, letterImage, xPos):
            xPos = __indentXPos
            yPos = yPos + font7px["lineheight"]
            
        self.blitImageAtPosition(letterImage, xPos, yPos)
        
        nextLetterXPos = xPos + letterImage.width + font7px["whitespace"]
        self.blitTextAtPosition(text[1:], autoLineBreak, nextLetterXPos, yPos, __indentXPos)
    
    def __isLineBreakRequired(self, text, autoLineBreak, letterImage, xPos):
        if text[:1] == ";":
            return True
        elif autoLineBreak and self.__isEndOfLineReached(letterImage, xPos):
            return True
        else:
            return False
                
    def __isEndOfLineReached(self, letterImage, xPos):
        return letterImage.width > self.width-xPos

    def __getLetterImageForNextLetter(self, text):
        nextLetter = text[:1].upper()
        if not nextLetter in font7px:
            nextLetter="?"
        return FlipdotImage(font7px[nextLetter])

    def serializeImageArray(self, transposed = False):
        if transposed:
            return self.__serializeTransposedImageArray()
        
        imageArray = []
        for y in range(self.height):
            for x in range(self.width):
                imageArray.append(self.rowArrayOfLineArraysOfPixels[y][x])
        return imageArray

    def __serializeTransposedImageArray(self):
        imageArray = []
        for x in range(self.width):
            for y in reversed(range(self.height)):
                imageArray.append(self.rowArrayOfLineArraysOfPixels[y][x])
        return imageArray
        

    def getLine(self, line):
        return self.rowArrayOfLineArraysOfPixels[line]
    
    def getSinglePixel(self, x, y):
        return self.rowArrayOfLineArraysOfPixels[y][x]
    
        
    @classmethod
    def newBlackFlipdotImage(cls, width, height):
        pixel2DArray = cls.generateColoredRowArrayOfLineArraysOfPixels(width, height, FlipdotImage.BLACKPIXEL) 
        return cls(pixel2DArray)

    @classmethod
    def newWhiteFlipdotImage(cls, width, height):
        pixel2DArray = cls.generateColoredRowArrayOfLineArraysOfPixels(width, height, FlipdotImage.WHITEPIXEL) 
        return cls(pixel2DArray)

    @classmethod
    def newLinesFlipdotImage(cls, width, height):
        array = [[(x+y)%2 for y in xrange(width)] for x in xrange(height)]
        return cls(array)


    @classmethod
    def NewPartOfAnotherFlipdotImage(cls, oldFlipdotImage, newSize, offset):
        pixel2DArray = cls.cutPartOfAnotherFlipdotImage(oldFlipdotImage, newSize, offset)
        return cls(pixel2DArray)
    
    @classmethod
    def cutPartOfAnotherFlipdotImage(cls, oldFlipdotImage, newSize, offset):
        width = newSize[0]
        height = newSize[1]
        xOffset = offset[0]
        yOffset = offset[1]
        rowArrayOfLineArrayOfPixels = []
        for y in range(height):
            lineArrayOfPixels = []
            for x in range(width):
                lineArrayOfPixels.append(oldFlipdotImage.getSinglePixel(xOffset+x, yOffset+y))
            rowArrayOfLineArrayOfPixels.append(lineArrayOfPixels)
        return rowArrayOfLineArrayOfPixels
        
    
    @staticmethod
    def generateColoredRowArrayOfLineArraysOfPixels(width, height, color):        
        rowArrayOfLineArrayOfPixels = []
        for y in range(height):
            rowArrayOfLineArrayOfPixels.append(FlipdotImage.generateColoredLineArrayOfPixels(width, color))
        return rowArrayOfLineArrayOfPixels

    @staticmethod
    def generateColoredLineArrayOfPixels(width, color):
        lineArrayOfPixels = []
        for x in range(width):
            lineArrayOfPixels.append(color)
        return lineArrayOfPixels



resetToTopicCounter = 0

@willie.module.rule('.*(alarm|Alarm|ALARM).*')
@willie.module.rate(30)
def alarmierung(bot, trigger):
    resetToTopicCounter  = 0
    matrix = FlipdotMatrix()
    matrix.showText(" "+trigger.nick+": "+trigger.group(0), True)
    bot.action("flipped to: >>"+trigger.nick+": "+trigger.group(0)+"<<", recipient="#ccc")



import re

theTopic = ""

def changeTopic (bot, trigger, newTopic):

    matrix = FlipdotMatrix()
#    matrix.resetAll()
    matrix.showText(newTopic, True)
    

@willie.module.rule(".*")
@willie.module.event("topic")
def topicierung(bot, trigger):
    global theTopic

    p = re.compile( 'club (closed|down|member|public) \| ?')
    newTopic = trigger.group(0)
    newTopic = p.sub('', newTopic)


    if (theTopic != newTopic):
        theTopic = newTopic
        changeTopic(bot, trigger, theTopic)


@willie.module.interval(10)
def check_every_5s(bot):
    global theTopic
    global resetToTopicCounter
    if (resetToTopicCounter == 2 and theTopic != ""):
        changeTopic(bot, None, theTopic)

    resetToTopicCounter+=1





        
    

    




    

