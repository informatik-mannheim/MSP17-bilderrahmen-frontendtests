#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.common.exceptions import *
import time
class Fullscreen:
    # ionic testing requires a xpath selecting. Only buttons are selectable with id.
    dom_xpath_getCurrentPage="(//ng-component[@class='app-root']/ion-nav/page-slides)[last()]"
    dom_xpath_getImageName="//ion-slide[contains(@class,'swiper-slide-active')]/div/img"
    dom_xpath_getImageDescription="./ion-content/div/h1"
    dom_id_masterButton="MasterButton" # class master wenn master
    dom_id_imageGalleryButton="GalleryButton"
    dom_xpath_onlyOnFullScreenPage="//div/img"
    dom_id_settingsButton="SettingsButton"
    dom_xpath_isMaster="//button[@id='MasterButton']/span/ion-icon[@ng-reflect-name='unlock']"
    def getCurrentFullscreen(self,webdriver):        
        # ionic creates the content several times (history) with different z-index in the dom. The Last page-slide (the fullscreen page with slider) is the current page.
        return webdriver.find_element_by_xpath(self.dom_xpath_getCurrentPage)
    def isFullscreen(self,webdriver):
        result=True
        try:
            webdriver.find_element_by_xpath(self.dom_xpath_getCurrentPage)
        except NoSuchElementException:
            result=False
        time.sleep(5)
        return result
    def swipeRight(self,webdriver):
        '''swipe left: swipe from right to left'''
        webdriver.switch_to.context("NATIVE_APP")
        window_size = webdriver.get_window_size()
        max_width = window_size["width"] - 1
        max_height = window_size["height"] - 1 
        
        startx=int(max_width*0.9)
        endx=int(max_width*0.1)    
        starty=int(max_height/2)
        webdriver.swipe(start_x=startx, start_y=starty, end_x=endx, end_y=starty, duration=800)
        time.sleep(5)
        webdriver.switch_to.context("WEBVIEW_de.hsmannheim.bilderrahmen")
    def swipeLeft(self,webdriver):
        '''swipe right: swipe from left to right'''
        webdriver.switch_to.context("NATIVE_APP")
        time.sleep(5)
        window_size = webdriver.get_window_size()
        max_width = window_size["width"] - 1
        max_height = window_size["height"] - 1 
        
        endx=int(max_width*0.9)
        startx=int(max_width*0.1)    
        starty=int(max_height/2)
        webdriver.swipe(start_x=startx, start_y=starty, end_x=endx, end_y=starty, duration=800)
        time.sleep(5)
        webdriver.switch_to.context("WEBVIEW_de.hsmannheim.bilderrahmen")
    def selectMaster(self,webdriver):
        '''check if master, then press master button'''
        if not self.isMaster(webdriver):
            try:
                webdriver.find_element_by_id(self.dom_id_masterButton).click()
            except NoSuchElementException:
                #retry master selection
                time.sleep(2)
                webdriver.find_element_by_id(self.dom_id_masterButton).click()
    def isMaster(self,webdriver):
        '''check if master'''
        result=True
        try:
            webdriver.find_element_by_xpath(self.dom_xpath_isMaster)
        except NoSuchElementException:
            result=False
        return result
    def getImageDescription(self,webdriver):
        result=""
        page=self.getCurrentFullscreen(webdriver)
        try:
            elem=page.find_element_by_xpath(self.dom_xpath_getImageDescription)
            print(elem)
            result=elem.text
        except:
            print("no description set")
        return result
    def getImageName(self,webdriver):
        time.sleep(5)
        page=self.getCurrentFullscreen(webdriver)
        elem=page.find_element_by_xpath(self.dom_xpath_getImageName)
        result=elem.get_attribute("data-img-name").split('_') 
        return result[len(result)-1]
    def switchToImageGallery(self,webdriver):
        webdriver.find_element_by_id(self.dom_id_imageGalleryButton).click()
    def switchToSettings(self,webdriver):
        webdriver.find_element_by_id(self.dom_id_settingsButton).click()
    def getImageInformations(self,webdriver):
        desc=self.getImageDescription(webdriver)
        name=self.getImageName(webdriver)
        result={}
        result[name]=desc
        return result
        
        
        