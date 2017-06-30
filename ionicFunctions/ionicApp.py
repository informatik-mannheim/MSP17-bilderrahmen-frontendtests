#!/usr/bin/python3
# -*- coding: utf-8 -*-
from appium import webdriver
from ionicFunctions.ionicStartPageFunctions import StartPage
from ionicFunctions.ionicImageGalleryFunctions import ImageGallery
from ionicFunctions.ionicFullscreenFunctions import Fullscreen
from ionicFunctions.ionicSettingsFunctions import Settings
# Tested only with android devices. Swiping is native context, but should work with ios apps too. If ionic app will be available for ios too.

class AndroidApp:
    def __init__(self,server,capabilities):
        self.driver = webdriver.Remote(server, capabilities)
        self.appStartPage=StartPage()
        self.appFullscreen=Fullscreen()
        self.appImageGallery=ImageGallery()
        self.appSettings=Settings()
    '''All Interactions on the Start Page (starts with sp_)'''
    def sp_useGoogleAccount(self,mail,pwd):
        self.appStartPage.useGoogleAccount(self.driver,mail,pwd)
    def sp_isStartPage(self):
        return self.appStartPage.isStartPage(self.driver)
    '''All Interactions on the Fullscreen Page (starts with fp_)'''
    def fp_isFullscreen(self):
        return self.appFullscreen.isFullscreen(self.driver)
    def fp_swipeLeft(self):
        self.appFullscreen.swipeLeft(self.driver)
    def fp_swipeRight(self):
        self.appFullscreen.swipeRight(self.driver)
    def fp_selectMaster(self):
        self.appFullscreen.selectMaster(self.driver)
    def fp_isMaster(self):
        return self.appFullscreen.isMaster(self.driver)
    def fp_getImageInformations(self):
        return self.appFullscreen.getImageInformations(self.driver)
    def fp_getImageDescription(self):
        return self.appFullscreen.getImageDescription(self.driver)
    def fp_switchToImageGallery(self):
        self.appFullscreen.switchToImageGallery(self.driver)
    def fp_switchToSettings(self):
        self.appFullscreen.switchToSettings(self.driver)
    def fp_getImageName(self):
        return self.appFullscreen.getImageName(self.driver)
    '''All Interactions on the ImageGallery Page (starts with igp_)'''
    def igp_isImageGallery(self):
        return self.appImageGallery.isImageGallery(self.driver)
    def igp_selectImageFromIndex(self,index):
        self.appImageGallery.selectImageFromIndex(self.driver,index)
    def igp_selectImageViaName(self,name):
        self.appImageGallery.selectImageViaName(self.driver,index)
    def igp_getImageCount(self):
        return self.appImageGallery.getImageCount(self.driver)
    '''All Interactions on the Settings Page'''
    def s_isSettings(self):
        return self.appSettings.isSettings(self.driver)
    def s_isAutoStart(self):
        return self.appSettings.isAutoStart(self.driver)
    def s_setAutoStart(self,value):
        self.appSettings.setAutoStart(self.driver,value)
    def s_setServerAdress(self,serverAdress):
        self.appSettings.setServerAdress(self.driver,serverAdress)
    def s_getServerAdress(self):
        return self.appSettings.getServerAdress(self.driver)
    def s_saveSettings(self):
        self.appSettings.saveSettings(self.driver)
                                           