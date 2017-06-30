#!/usr/bin/python3
# -*- coding: utf-8 -*-

from webappFunctions.webStartPageFunctions import StartPage
from webappFunctions.webPicturesFunctions import PicturesPage
from webappFunctions.webUploadFunctions import UploadPage


class WebApp:

    def __init__(self,driver):
        self.driver = driver
        self.appStartPage=StartPage()
        self.appPicturePage=PicturesPage()
        self.appUploadPage=UploadPage()
    '''Menu Functions'''    
    def sp_isPicturesPage(self):
        return self.appStartPage.isPictures(self.driver)
    def sp_isUploadPage(self):
        return self.appStartPage.isUpload(self.driver)
    def sp_switchToUploadPage(self):
        self.appStartPage.switchToUploadPage(self.driver)
    def sp_switchToPicturesPage(self):
        self.appStartPage.switchToPicturesPage(self.driver)
    def sp_logOut(self):
        self.appStartPage.logOut(self.driver)
    def sp_logIn(self,mail,pwd):
        self.appStartPage.logIn(self.driver,mail,pwd)
    def sp_isLoggedIn(self):
        return self.appStartPage.isLoggedIn(self.driver)
    def sp_getAlertPresentNotLoggedIn(self):
        return self.appStartPage.getAlertPresentNotLoggedIn(self.driver)
    def sp_getImageCount(self):
        return self.appStartPage.getImageCount(self.driver)
    def sp_logInChooseAccount(self,mail):
        self.appStartPage.logInChooseAccount(self.driver,mail)
    def sp_logInAndconfirmPageUse(self,mail,pwd):
        self.appStartPage.confirmPageUsage(self.driver,mail,pwd)
    ''' Upload Functions'''
    def up_uploadFile(self,path):
        self.appUploadPage.uploadFile(self.driver,path)
    def up_setDescriptionForPicture(self,description,picture):
        self.appUploadPage.setDescriptionForPicture(self.driver,description,picture)        
    def up_setDescriptionsForPictures(self,descriptionsAndPictures):
        self.appUploadPage.setDescriptionsForPictures(self.driver,descriptionsAndPictures)
    def up_uploadFiles(self,paths):
        self.appUploadPage.uploadFiles(self.driver,paths)
    def up_pressFileUploadSubmit(self):
        self.appUploadPage.pressFileUploadSubmit(self.driver)
    ''' Pictures Functions '''
    def pp_getImagePreviewCount(self):
        return self.appPicturePage.getImagePreviewCount(self.driver)
    def pp_deleteFiles(self):
        self.appPicturePage.deleteFiles(self.driver)
  