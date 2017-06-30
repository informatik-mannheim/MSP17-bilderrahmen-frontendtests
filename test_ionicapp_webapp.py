#!/usr/bin/python3
# -*- coding: utf-8 -*-   

# Testcases testing ionic app and webapp together.

import unittest, time, os,sys
from appium import webdriver

from webappFunctions.webApp import WebApp
import selenium
from time import sleep
from ionicFunctions.ionicApp import AndroidApp
from testValues import *
from testEnvironmentValues import *
ionic_webapp_browser="Firefox"

class IonicAppAndWebapp(unittest.TestCase):
    def setUp(self):
        # setup ionic app(s)
        device1_desired_caps['noReset']=False
        self.client1= AndroidApp('http://localhost:'+APPIUM_PORT1+'/wd/hub',device1_desired_caps)
        #self.client2= AndroidApp('http://localhost:'+APPIUM_PORT2+'/wd/hub',device2_desired_caps)
        time.sleep(20)
        
        # if capability noReset is false, a google account must be selected and settings must be set
        self.client1.sp_useGoogleAccount(WEBAPP_VALUE_USER_2_MAIL,WEBAPP_VALUE_USER_2_PWD)
        #self.client2.sp_useGoogleAccount(WEBAPP_VALUE_USER_2_MAIL,WEBAPP_VALUE_USER_2_PWD)
        time.sleep(10)
        #self.client1.driver.implicitly_wait(30)
        # Except for swiping, all Elements in the ionicapp will be tested with the dom (WebView)
        # If capabilities autoWebview is true, the context switch is not needed
        #self.client2.driver.switch_to.context("WEBVIEW_de.hsmannheim.bilderrahmen")
        self.client1.driver.switch_to.context("WEBVIEW_de.hsmannheim.bilderrahmen") 
        self.client1.driver.implicitly_wait(10)
        #self.client2.driver.implicitly_wait(10)
        self.client1.s_saveSettings()
        #self.client2.s_saveSettings()
        time.sleep(2)
        
        # set up webapp
        driver = selenium.webdriver.Firefox()
        if ionic_webapp_browser=="Chrome":
            driver = selenium.webdriver.Chrome()
        if ionic_webapp_browser=="IE":
            driver = selenium.webdriver.Ie()
        self.webapp=WebApp(driver)
        self.webapp.driver.get(WEBAPP_URL)
        self.webapp.driver.maximize_window()
        time.sleep(10)      
    def tearDown(self):     
        self.webapp.sp_switchToPicturesPage()
        time.sleep(10)
        # always delete the files.
        self.webapp.pp_deleteFiles()
        self.webapp.driver.quit()
        time.sleep(10)
        # sometimes appium doesn't quit well, when in Webview driver.
        self.client1.driver.switch_to.context("NATIVE_APP")
        #self.client2.driver.switch_to.context("NATIVE_APP")
        self.client1.driver.quit()
        #self.client2.driver.quit()
    def test_uploadFile_T18(self):
        self.webapp.sp_logIn(WEBAPP_VALUE_USER_2_MAIL,WEBAPP_VALUE_USER_2_PWD)
        time.sleep(5)
        self.assertEqual(True,self.webapp.sp_isLoggedIn())
        time.sleep(5)
        
        beforeUpload=self.webapp.sp_getImageCount() 
        self.assertEqual(0,beforeUpload)
        self.webapp.up_uploadFile(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_1)
        time.sleep(2)
        self.webapp.up_setDescriptionForPicture(WEBAPP_VALUE_TEST_DESCRIPTION_1,WEBAPP_VALUE_TEST_IMAGE_1)
        time.sleep(2)
        self.webapp.up_pressFileUploadSubmit()
        time.sleep(2)
        # bestätigungsnachricht ist bisher nur der image count (ob es geklappt hat, sieht man daran)
        self.assertEqual((beforeUpload+1),self.webapp.sp_getImageCount())  
        time.sleep(2)
        newPic1=self.client1.fp_getImageName()
        newDescription1=self.client1.fp_getImageDescription()
        #newPic2=self.client2.fp_getImageName()
        #newDescription2=self.client2.fp_getImageDescription()
        #self.assertEqual(True,newPic1==newPic2)
        #self.assertEqual(True,newDescription1==newDescription2)
        #self.assertEqual(WEBAPP_VALUE_TEST_IMAGE_1,newPic2)
        #self.assertEqual(WEBAPP_VALUE_TEST_DESCRIPTION_1,newDescription2)
        self.assertEqual(WEBAPP_VALUE_TEST_IMAGE_1,newPic1)
        self.assertEqual(WEBAPP_VALUE_TEST_DESCRIPTION_1,newDescription1)
    def test_choosePictureFromImageGalleryAndSwipe_T20_T22(self):
        # login to webapp
        self.webapp.sp_logIn(WEBAPP_VALUE_USER_2_MAIL,WEBAPP_VALUE_USER_2_PWD)
        time.sleep(3)
        self.assertEqual(True,self.webapp.sp_isLoggedIn())
        time.sleep(15)
        # make sure, no image is uploaded.
        beforeUpload=self.webapp.sp_getImageCount()       
        self.assertEqual(0,beforeUpload)
        # upload 2 images
        arrayOfImages=[]
        arrayOfImages.append(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_1)
        arrayOfImages.append(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_2)
        
        mapOfDescriptions={}
        mapOfDescriptions[WEBAPP_VALUE_TEST_IMAGE_1]=WEBAPP_VALUE_TEST_DESCRIPTION_1
        mapOfDescriptions[WEBAPP_VALUE_TEST_IMAGE_2]=WEBAPP_VALUE_TEST_DESCRIPTION_2
        
        self.webapp.up_uploadFiles(arrayOfImages)
        time.sleep(5)
        self.webapp.up_setDescriptionsForPictures(mapOfDescriptions)
        
        time.sleep(5)
        self.webapp.up_pressFileUploadSubmit()
        time.sleep(5)
        # check if upload succeeded
        self.assertEqual((beforeUpload+2),self.webapp.sp_getImageCount())  
        time.sleep(5)
        
        # select master and go to image gallery
        self.client1.fp_selectMaster()
        time.sleep(5)
        self.assertEqual(True,self.client1.fp_isMaster())
        #self.assertEqual(False,self.client2.fp_isMaster())
        self.client1.fp_switchToImageGallery()
        time.sleep(10)
        
        # check count of pictures
        self.assertEqual(2,self.client1.igp_getImageCount())
        # select the first picture (first uploaded)
        self.client1.igp_selectImageFromIndex("1") 
        time.sleep(10)
        # back in fullscreen page, check if first uploaded picture is present
        newPic1=self.client1.fp_getImageName()
        newDescription1=self.client1.fp_getImageDescription()
        #newPic2=self.client2.fp_getImageName()
        #newDescription2=self.client2.fp_getImageDescription()
        #self.assertEqual(True,newPic1==newPic2)
        #self.assertEqual(True,newDescription1==newDescription2)
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_1 == newPic2))
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_1 == newDescription2 ))
        
        # ionic doesnt set the class, which identifies the image name (per xpath) of the current picture
        # only occurs when selecting picture from image gallery. So this fail:
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_1 == newPic1))
        
        # but this works
        self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_1 == newDescription1))
        time.sleep(2)
        # swipe and check the last picture
        self.client1.fp_swipeRight()
        time.sleep(5)
        newPic1=self.client1.fp_getImageName()
        newDescription1=self.client1.fp_getImageDescription()
        #newPic2=self.client2.fp_getImageName()
        #newDescription2=self.client2.fp_getImageDescription()
        #self.assertEqual(True,newPic1==newPic2)
        #self.assertEqual(True,newDescription1==newDescription2)
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_2 == newPic2))
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_2 == newDescription2 ))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_2 == newPic1)) 
        self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_2 == newDescription1))
    def test_tryToSwipeWithOnlyOnePicture_T21(self):
        # login and upload in the webapp
        self.webapp.sp_logIn(WEBAPP_VALUE_USER_2_MAIL,WEBAPP_VALUE_USER_2_PWD)
        time.sleep(5)
        self.assertEqual(True,self.webapp.sp_isLoggedIn())
        time.sleep(5)
        
        beforeUpload=self.webapp.sp_getImageCount()
        self.assertEqual(0,beforeUpload)
        self.webapp.up_uploadFile(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_1)
        time.sleep(2)
        self.webapp.up_setDescriptionForPicture(WEBAPP_VALUE_TEST_DESCRIPTION_1,WEBAPP_VALUE_TEST_IMAGE_1)
        time.sleep(2)
        self.webapp.up_pressFileUploadSubmit()
        time.sleep(15)
        self.assertEqual((beforeUpload+1),self.webapp.sp_getImageCount())  
        time.sleep(2)
        # slave gets master and trys to swipe but always the same picture is shown. Slider works.
        self.client1.fp_selectMaster()
        time.sleep(5)
        
        self.assertEqual(True,self.client1.fp_isMaster())
        #self.assertEqual(False,self.client2.fp_isMaster())
        
        time.sleep(10)
        
        newPic1=self.client1.fp_getImageName()
        newDescription1=self.client1.fp_getImageDescription()
        #newPic2=self.client2.fp_getImageName()
        #newDescription2=self.client2.fp_getImageDescription()
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_1 == newPic2))
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_1 == newDescription2 ))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_1 == newPic1))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_1 == newDescription1))
        time.sleep(2)
        time.sleep(2)
        self.client1.fp_swipeRight()
        time.sleep(5)
        newPic1=self.client1.fp_getImageName()
        newDescription1=self.client1.fp_getImageDescription()
        #newPic2=self.client2.fp_getImageName()
        #newDescription2=self.client2.fp_getImageDescription()
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_1 == newPic2))
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_1 == newDescription2 ))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_1 == newPic1))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_1 == newDescription1))
        time.sleep(2)
        self.client1.fp_swipeLeft()
        time.sleep(5)
        newPic1=self.client1.fp_getImageName()
        newDescription1=self.client1.fp_getImageDescription()
        #newPic2=self.client2.fp_getImageName()
        #newDescription2=self.client2.fp_getImageDescription()
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_1 == newPic2))
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_1 == newDescription2 ))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_1 == newPic1))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_1 == newDescription1))
    def test_uploadLargeFile_T24(self):       
        self.webapp.driver.implicitly_wait(30)   
        self.webapp.sp_logIn(WEBAPP_VALUE_USER_2_MAIL,WEBAPP_VALUE_USER_2_PWD)
        time.sleep(5)
        self.assertEqual(True,self.webapp.sp_isLoggedIn())
        time.sleep(5)
        
        beforeUpload=self.webapp.sp_getImageCount()  
        self.assertEqual(0,beforeUpload)
        time.sleep(2)
        self.webapp.up_uploadFile(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_BIG)
        time.sleep(10)
        self.webapp.up_setDescriptionForPicture(WEBAPP_VALUE_TEST_DESCRIPTION_BIG,WEBAPP_VALUE_TEST_IMAGE_BIG)
        time.sleep(5)
        self.webapp.up_pressFileUploadSubmit()
        time.sleep(30)
        # bestätigungsnachricht ist bisher nur der image count (ob es geklappt hat, sieht man daran)
        self.assertEqual((beforeUpload+1),self.webapp.sp_getImageCount())  
        time.sleep(30)
        newPic1=self.client1.fp_getImageName()
        newDescription1=self.client1.fp_getImageDescription()
        #newPic2=self.client2.fp_getImageName()
        #newDescription2=self.client2.fp_getImageDescription()
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_BIG == newPic2))
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_BIG == newDescription2 ))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_BIG == newPic1))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_BIG == newDescription1))
    @unittest.skip('NOT RUNNING: Requries 2 Android devices and 2 appium servers on different ports')
    def test_SwipeLatenz_T3(self):
        pass
        # this implementation is not tested!
        self.webapp.sp_logIn(WEBAPP_VALUE_USER_2_MAIL,WEBAPP_VALUE_USER_2_PWD)
        time.sleep(3)
        self.assertEqual(True,self.webapp.sp_isLoggedIn())
        time.sleep(10)
        
        beforeUpload=self.webapp.sp_getImageCount()       
        self.assertEqual(0,beforeUpload) 
        arrayOfImages=[]
        arrayOfImages.append(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_1)
        arrayOfImages.append(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_2)
        
        mapOfDescriptions={}
        mapOfDescriptions[WEBAPP_VALUE_TEST_IMAGE_1]=WEBAPP_VALUE_TEST_DESCRIPTION_1
        mapOfDescriptions[WEBAPP_VALUE_TEST_IMAGE_2]=WEBAPP_VALUE_TEST_DESCRIPTION_2
        
        resultMap={}
        resultMap[WEBAPP_VALUE_TEST_IMAGE_1]=WEBAPP_VALUE_TEST_DESCRIPTION_1
        
        self.webapp.up_uploadFiles(arrayOfImages)
        time.sleep(5)
        self.webapp.up_setDescriptionsForPictures(mapOfDescriptions)
        
        time.sleep(5)
        self.webapp.up_pressFileUploadSubmit()
        time.sleep(5)
        self.assertEqual((beforeUpload+2),self.webapp.sp_getImageCount())  
        time.sleep(20)     
        
        self.client1.fp_selectMaster()
        time.sleep(5)
        
        self.assertEqual(True,self.client1.fp_isMaster())
        self.assertEqual(False,self.client2.fp_isMaster())
        self.client1.fp_swipeLeft()
        time.sleep(10)
        pic1BeforeSwipe=self.client1.fp_getImageInformations()
        pic2BeforeSwipe=self.client2.fp_getImageInformations()
        time.sleep(10)
        self.assertEqual(pic1BeforeSwipe,pic2BeforeSwipe)
        t_end = time.time() + 5
        newPicture=false
        # the slave will show the picture of the master within 5 seconds
        while time.time() < t_end:
            if cmp(self.client2.fp_getImageInformations(),pic2BeforeSwipe)==0:
                newPicture=True
        self.assertEqual(True,newPicture)
        self.assertEqual(resultMap,self.client1.fp_getImageInformations())
        self.assertEqual(self.client2.fp_getImageInformations(),self.client1.fp_getImageInformations())
    def test_MasterSlaveSelection_T23_T10(self):
        # upload pictures for assertion, if swipe was successful or not
        self.webapp.sp_logIn(WEBAPP_VALUE_USER_2_MAIL,WEBAPP_VALUE_USER_2_PWD)
        time.sleep(5)
        self.assertEqual(True,self.webapp.sp_isLoggedIn())
        time.sleep(10)
        
        beforeUpload=self.webapp.sp_getImageCount()    
        self.assertEqual(0,beforeUpload)
        arrayOfImages=[]
        arrayOfImages.append(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_1)
        arrayOfImages.append(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_2)
        
        mapOfDescriptions={}
        mapOfDescriptions[WEBAPP_VALUE_TEST_IMAGE_1]=WEBAPP_VALUE_TEST_DESCRIPTION_1
        mapOfDescriptions[WEBAPP_VALUE_TEST_IMAGE_2]=WEBAPP_VALUE_TEST_DESCRIPTION_2
        
        self.webapp.up_uploadFiles(arrayOfImages)
        time.sleep(5)
        self.webapp.up_setDescriptionsForPictures(mapOfDescriptions)
        
        time.sleep(5)
        self.webapp.up_pressFileUploadSubmit()
        time.sleep(5)
        self.assertEqual((beforeUpload+2),self.webapp.sp_getImageCount())  
        time.sleep(15)
        
        # on start up, all roles are slaves
        self.assertEqual(False,self.client1.fp_isMaster())
        #self.assertEqual(False,self.client2.fp_isMaster()),
        # last uploaded picture ist shown
        newPic1=self.client1.fp_getImageName()
        newDescription1=self.client1.fp_getImageDescription()
        #newPic2=self.client2.fp_getImageName()
        #newDescription2=self.client2.fp_getImageDescription()
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_2 == newPic2))
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_12== newDescription2 ))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_2 == newPic1))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_2 == newDescription1))
        
        # try to swipe as non master
        self.client1.fp_swipeLeft()
        time.sleep(2)
        newPic1=self.client1.fp_getImageName()
        newDescription1=self.client1.fp_getImageDescription()
        #newPic2=self.client2.fp_getImageName()
        #newDescription2=self.client2.fp_getImageDescription()
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_2 == newPic2))
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_12== newDescription2 ))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_2 == newPic1))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_2 == newDescription1))
        time.sleep(2)
        
        self.client1.fp_selectMaster()
        time.sleep(5)
        self.assertEqual(True,self.client1.fp_isMaster())
        # swipe again
        self.client1.fp_swipeLeft()
        time.sleep(2)
        # this should be successful this time (the first picture is shown)
        newPic1=self.client1.fp_getImageName()
        newDescription1=self.client1.fp_getImageDescription()
        #newPic2=self.client2.fp_getImageName()
        #newDescription2=self.client2.fp_getImageDescription()
        
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_1 == newPic2))
        #self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_1 == newDescription2 ))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_IMAGE_1 == newPic1))
        self.assertEqual(True,(WEBAPP_VALUE_TEST_DESCRIPTION_1 == newDescription1))
        
        # change master role between the two ionic clients
        #time.sleep(2)
        #self.assertEqual(False,self.client2.fp_isMaster())
        #self.client2.fp_selectMaster()#
        #time.sleep(10)
        #self.assertEqual(False,self.client1.fp_isMaster())
        #time.sleep(2)
        #self.assertEqual(True,self.client2.fp_isMaster())
        #self.client1.fp_selectMaster()
        #time.sleep(10)
        #self.assertEqual(True,self.client1.fp_isMaster())
        #time.sleep(2)
        #self.assertEqual(False,self.client2.fp_isMaster())
        