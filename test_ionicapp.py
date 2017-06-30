#!/usr/bin/python3
# -*- coding: utf-8 -*-   
"""
TEstfälle für einen Android Client (1 Client)

Hier werden die Grundfunktionen der IonicApp getestet (feingranularer als die testfälle).
"""

import unittest, time, os,sys
from appium import webdriver
from time import sleep
from ionicFunctions.ionicApp import AndroidApp
from testValues import *
from testEnvironmentValues import *
import logging

class IonicAppTest(unittest.TestCase):
    def setUp(self):
        # use existing accoutn with uploaded pictures in webapp (no tear up upload)
        device1_desired_caps['noReset']=False
        self.client= AndroidApp('http://localhost:'+APPIUM_PORT1+'/wd/hub',device1_desired_caps)     
        
        self.client.driver.implicitly_wait(25)        
        self.client.driver.switch_to.context("WEBVIEW_de.hsmannheim.bilderrahmen")
        time.sleep(25)
        # login needed if capabilitie noReset auf false (defualt). see testEnvironmentValues.py
        self.client.sp_useGoogleAccount(WEBAPP_VALUE_USER_1_MAIL,WEBAPP_VALUE_USER_1_PWD)
        self.client.driver.implicitly_wait(30)
        # use default settings
        self.client.s_saveSettings()
        time.sleep(10)
            
        
    def tearDown(self):
        self.client.driver.switch_to.context("NATIVE_APP")
        time.sleep(10)
        self.client.driver.quit()
    def test_swiping(self):
        self.client.driver.implicitly_wait(5)
        time.sleep(5)
        #self.assertEqual(False,self.client.fp_isMaster()) 
        self.client.fp_selectMaster()
        time.sleep(5)
        self.assertEqual(True,self.client.fp_isMaster())
        self.client.fp_swipeRight()
        time.sleep(5)
        print(self.client.fp_getImageDescription())
        self.client.fp_swipeRight()
        time.sleep(5)
        print(self.client.fp_getImageDescription())
        self.client.fp_swipeLeft() 
        time.sleep(5)
        print(self.client.fp_getImageDescription())
    def test_selectImageFromGallery(self):
        self.client.driver.implicitly_wait(5)
        #self.assertEqual(False,self.client.fp_isMaster()) 
        self.client.fp_selectMaster()
        time.sleep(2)
        print(self.client.fp_getImageDescription())
        print(self.client.fp_getImageName())
        time.sleep(2)
        self.client.fp_switchToImageGallery()
        time.sleep(5)
        
        # das hier funktioniert nicht. im dom sind die seiten permals vorhanden (page-home und page-slides), jeweils mit verschiedenen z-index en
        #self.assertEqual(False,self.client.fp_isFullscreen())
        print(self.client.igp_getImageCount())
        self.client.igp_selectImageFromIndex("2")
        time.sleep(5)
        print(self.client.fp_getImageDescription())
        
        print(self.client.fp_getImageName())
    def test_settingsMenu(self):
        # settings ist auf fullscreen...
        #self.assertEqual(False,self.client.s_isSettings())
        #self.assertEqual(True,self.client.fp_isFullscreen())
        
        self.client.driver.implicitly_wait(5)
        time.sleep(5)
        #self.assertEqual(False,self.client.fp_isMaster()) 
        self.client.fp_selectMaster()
        time.sleep(5)
        
        self.client.fp_switchToSettings()
        time.sleep(5)
        #self.assertEqual(False,self.client.s_isAutoStart())
        #time.sleep(2)
        self.client.s_setAutoStart(True)
        time.sleep(2)
        self.assertEqual(True,self.client.s_isAutoStart())
        time.sleep(2)
        #self.client.s_setAutoStart(False)
        #time.sleep(2)
        #self.assertEqual(False,self.client.s_isAutoStart())
        #time.sleep(2)
        #self.assertEqual(IONIC_APP_SETTINGS_SERVER_ADRESSE,self.client.s_getServerAdress())
        time.sleep(2)
        print(self.client.s_getServerAdress())
        time.sleep(2)
        self.client.s_setServerAdress(IONIC_APP_SETTINGS_SERVER_ADRESSE)
        time.sleep(2)
        #print(self.client.s_getServerAdress()) 
        self.client.s_saveSettings()
        time.sleep(10)
        #self.assertEqual(IONIC_APP_SETTINGS_SERVER_ADRESSE,self.client.s_getServerAdress())
        time.sleep(5)       
        
        
    #---START OF SCRIPT
if __name__ == '__main__':    
    suite = unittest.TestLoader().loadTestsFromTestCase(IonicAppTest)
    unittest.TextTestRunner(verbosity=2).run(suite)