#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Testcases for the webapp
import unittest, time, os,sys
from webappFunctions.webApp import WebApp
import selenium
from testValues import *
from testEnvironmentValues import *
import argparse
from selenium.common.exceptions import *


webapp_browser="Firefox"

class WebAppTest(unittest.TestCase):
    def setUp(self):
        driver = selenium.webdriver
        if webapp_browser=='Firefox':
            driver = selenium.webdriver.Firefox()
        if webapp_browser=='Chrome':
            driver = selenium.webdriver.Chrome()
        self.web=WebApp(driver)
        # navigate to the application home page
        self.web.driver.get(WEBAPP_URL)
        self.web.driver.maximize_window()
        # workaround for detecting a attribute aria-expanded (which tab is visible). It is not set on load
        self.web.sp_switchToPicturesPage()
        time.sleep(5)        
        self.web.sp_switchToUploadPage()
    def tearDown(self):
        if self.web.sp_isUploadPage():
            self.web.sp_switchToPicturesPage()
        time.sleep(10)
        self.web.pp_deleteFiles()
        self.web.driver.quit()
    def test_UploadOneFileAndDelete(self):
        self.web.driver.implicitly_wait(30)   
        self.web.sp_logIn(WEBAPP_VALUE_USER_2_MAIL,WEBAPP_VALUE_USER_2_PWD)
        time.sleep(5)
        self.assertEqual(True,self.web.sp_isLoggedIn())
        self.assertEqual(True,self.web.sp_isUploadPage())
        self.assertEqual(False,self.web.sp_isPicturesPage())
        time.sleep(5)
        
        beforeUpload=self.web.sp_getImageCount()
        self.web.up_uploadFile(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_1)
        time.sleep(2)
        self.web.up_setDescriptionForPicture(WEBAPP_VALUE_TEST_DESCRIPTION_1,WEBAPP_VALUE_TEST_IMAGE_1)
        time.sleep(2)
        self.web.up_pressFileUploadSubmit()
        time.sleep(2)
        self.assertEqual((beforeUpload+1),self.web.sp_getImageCount()) 
        
        # switch to other tab
        self.web.sp_switchToPicturesPage()
        self.assertEqual(False,self.web.sp_isUploadPage())
        self.assertEqual(True,self.web.sp_isPicturesPage())
        
        self.assertTrue(self.web.pp_getImagePreviewCount(),self.web.sp_getImageCount())
        
        # delete all files
        self.web.pp_deleteFiles()        
        
        # back to upload page
        self.web.sp_switchToUploadPage()
        self.assertEqual(True,self.web.sp_isUploadPage())
        self.assertEqual(False,self.web.sp_isPicturesPage())
    def test_UploadWithoutLogin(self):
        self.web.driver.implicitly_wait(30)
        uploadButtonNotClickable=False
        try:
            self.web.up_pressFileUploadSubmit().click()
        except ElementNotInteractableException:
            uploadButtonNotClickable=True
            
        self.assertEqual(True,uploadButtonNotClickable)  
    #@unittest.skip('Chrome upload multiple files on input is not working.')
    def test_UploadMoreFiles(self):
        self.web.driver.implicitly_wait(30)   
        self.web.sp_logIn(WEBAPP_VALUE_USER_2_MAIL,WEBAPP_VALUE_USER_2_PWD)
        self.assertEqual(True,self.web.sp_isLoggedIn())
        
        time.sleep(5)
        
        beforeUpload=self.web.sp_getImageCount()
        
        arrayOfImages=[]
        arrayOfImages.append(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_1)
        arrayOfImages.append(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_2)
        arrayOfImages.append(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_3)
        arrayOfImages.append(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_4)
        arrayOfImages.append(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_5)
        
        mapOfDescriptions={}
        mapOfDescriptions[WEBAPP_VALUE_TEST_IMAGE_1]=WEBAPP_VALUE_TEST_DESCRIPTION_1
        mapOfDescriptions[WEBAPP_VALUE_TEST_IMAGE_2]=WEBAPP_VALUE_TEST_DESCRIPTION_2
        mapOfDescriptions[WEBAPP_VALUE_TEST_IMAGE_3]=WEBAPP_VALUE_TEST_DESCRIPTION_3
        mapOfDescriptions[WEBAPP_VALUE_TEST_IMAGE_4]=WEBAPP_VALUE_TEST_DESCRIPTION_4
        mapOfDescriptions[WEBAPP_VALUE_TEST_IMAGE_5]=WEBAPP_VALUE_TEST_DESCRIPTION_5
        
        self.web.up_uploadFiles(arrayOfImages)
        time.sleep(2)
        self.web.up_setDescriptionsForPictures(mapOfDescriptions)
        time.sleep(5)
        self.web.up_pressFileUploadSubmit()
        time.sleep(20)
        self.assertEqual((beforeUpload+5),self.web.sp_getImageCount()) 
        

    @unittest.skip('this test takes a while.')
    def test_deletionAfter200PictureLimit_T12_T24_T6(self):
        self.web.driver.implicitly_wait(30)   
        self.web.sp_logIn(WEBAPP_VALUE_USER_2_MAIL,WEBAPP_VALUE_USER_2_PWD)
        self.assertEqual(True,self.web.sp_isLoggedIn())
        
        time.sleep(5)
        
        beforeUpload=self.web.sp_getImageCount()
        
        arrayOfImages=[]
        mapOfDescriptions={}
        imageCount=201
        counter=0
        while counter<=imageCount:
            # upload 5 files and press button
            arrayOfImages=[]
            mapOfDescriptions={}
            bulkCounter=0
            while bulkCounter<=5 and counter<=imageCount:
                img=str(counter)+".jpg"
                arrayOfImages.append(os.getcwd()+WEBAPP_IMAGES_FOLDER+img)
                mapOfDescriptions[img]=img+"    Description"
                counter=counter+1
                bulkCounter=bulkCounter+1
        
            self.web.up_uploadFiles(arrayOfImages)
            time.sleep(2+int(counter*0.2))
            self.web.up_setDescriptionsForPictures(mapOfDescriptions)
            time.sleep(10)
            self.web.up_pressFileUploadSubmit()
            time.sleep(2+int(counter*0.2))
            
        time.sleep(30) # known issue (203/200)
                
        self.assertEqual(200,self.web.sp_getImageCount()) 
        
    def test_uploadANoneImageFile_T13(self):
        self.web.driver.implicitly_wait(30)   
        self.web.sp_logIn(WEBAPP_VALUE_USER_2_MAIL,WEBAPP_VALUE_USER_2_PWD)
        time.sleep(5)
        self.assertEqual(True,self.web.sp_isLoggedIn())
        self.assertEqual(True,self.web.sp_isUploadPage())
        self.assertEqual(False,self.web.sp_isPicturesPage())
        time.sleep(5)
        # txt file
        beforeUpload=self.web.sp_getImageCount()
        self.web.up_uploadFile(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_INVALID_IMAGE_1)
        time.sleep(2)
        self.web.up_setDescriptionForPicture(WEBAPP_VALUE_TEST_INVALID_IMAGE_DESCRIPTION_1,WEBAPP_VALUE_TEST_INVALID_IMAGE_1)
        time.sleep(2)
        self.web.up_pressFileUploadSubmit()
        time.sleep(10)
        self.assertEqual((beforeUpload),self.web.sp_getImageCount()) 
        # pdf file
        beforeUpload=self.web.sp_getImageCount()
        self.web.up_uploadFile(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_INVALID_IMAGE_2)
        time.sleep(2)
        self.web.up_setDescriptionForPicture(WEBAPP_VALUE_TEST_INVALID_IMAGE_DESCRIPTION_2,WEBAPP_VALUE_TEST_INVALID_IMAGE_2)
        time.sleep(2)
        self.web.up_pressFileUploadSubmit()
        time.sleep(10)
        self.assertEqual((beforeUpload),self.web.sp_getImageCount()) 
    #@unittest.skip("login fails in chrome") 
    def test_LoginAndLogout_T11_A1(self):
        self.web.driver.implicitly_wait(30)   
        self.web.sp_logIn(WEBAPP_VALUE_USER_2_MAIL,WEBAPP_VALUE_USER_2_PWD)
        time.sleep(5)
        self.assertEqual(True,self.web.sp_isLoggedIn())
        self.web.sp_logOut()
        time.sleep(5)
        self.assertEqual(False,self.web.sp_isLoggedIn())
        self.web.driver.implicitly_wait(30)   
        self.web.sp_logInChooseAccount(WEBAPP_VALUE_USER_2_MAIL)
        time.sleep(5)
        self.assertEqual(True,self.web.sp_isLoggedIn())
    #@unittest.skip("skip. login in chrome is not stable#")
    def test_UploadFileWithoutLoginOnIonicApp_T15(self):
        # use account, which was never used for the ionic app
        self.web.driver.implicitly_wait(20)  
        self.web.sp_logInAndconfirmPageUse(WEBAPP_NO_IONIC_USE_VALUE_USER_MAIL,WEBAPP_NO_IONIC_USE_VALUE_USER_PWD)
        time.sleep(5)
        self.assertEqual(True,self.web.sp_isLoggedIn())
        # upload file
        beforeUpload=self.web.sp_getImageCount()
        
        self.web.up_uploadFile(os.getcwd()+WEBAPP_IMAGES_FOLDER+WEBAPP_VALUE_TEST_IMAGE_1)
        time.sleep(2)
        self.web.up_setDescriptionForPicture(WEBAPP_VALUE_TEST_DESCRIPTION_1,WEBAPP_VALUE_TEST_IMAGE_1)
        time.sleep(2)
        self.web.up_pressFileUploadSubmit()
        time.sleep(10)
        self.assertEqual((beforeUpload),self.web.sp_getImageCount())     
   





#---START OF SCRIPT
if __name__ == '__main__':
    # own testsuite, to only test webapp on different browsers.
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser', default='Firefox')
    args = parser.parse_args()   
    
    webapp_browser=args.browser
    print("Testing with: "+webapp_browser)
    
    suite = unittest.TestLoader().loadTestsFromTestCase(WebAppTest)
    unittest.TextTestRunner(verbosity=2).run(suite)