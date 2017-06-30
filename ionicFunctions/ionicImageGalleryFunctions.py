#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains

class ImageGallery:
    xpath_dom_currentPpage="(//ng-component[@class='app-root']/ion-nav/page-slides)[last()]"
    xpath_dom_SelectImageName_start="/img[@class='thumbnail' and contains(@src,'"
    xpath_dom_SelectImageName_end="')]"
    xpath_dom_images="//ion-grid/ion-row/ion-col/img"
    def isImageGallery(self,webdriver):
        return (self.getImageCount(webdriver)>1)
    def selectImageFromIndex(self,webdriver,index):
        '''select picutre by index'''  
        page=webdriver.find_element_by_xpath(self.xpath_dom_currentPpage)
        page.find_element_by_xpath("("+self.xpath_dom_images+")["+index+"]").click()        
    def selectImageViaName(self,webdriver,name):
        '''select picture by name'''  
        page=webdriver.find_element_by_xpath(self.xpath_dom_currentPpage)
        page.find_element_by_xpath(self.xpath_dom_SelectImageName_start+index+self.xpath_dom_SelectImageName_end).click()  
    def getImageCount(self,webdriver):
        ''' Get the count of images'''
        page=webdriver.find_element_by_xpath(self.xpath_dom_currentPpage)
        return len(page.find_elements_by_xpath(self.xpath_dom_images))