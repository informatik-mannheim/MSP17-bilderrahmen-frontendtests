#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common import keys
from selenium.common.exceptions import *
from appium.webdriver.common.touch_action import TouchAction
class Settings:    
    dom_css_modal_is_present='.show-page'
    dom_xpath_auto_start_checkbox="//ion-toggle/button[@role='checkbox']" 
    dom_xpath_is_auto_start_checkbox="//ion-toggle[contains(@class,'toggle-checked')]" 
    dom_xpath_server_address_input="//input[@name='ServerIpTextfield']"
    dom_xpath_save_button="//button/span[contains(text(),'Speichern')]/parent::*"
    dom_css_server_address_input=".input-cover"
    
    def isSettings(self,webdriver):
        result=True
        try:
            webdriver.find_element_by_css_selector(self.dom_css_modal_is_present)
        except NoSuchElementException:
            result=False
        return result
    def setAutoStart(self,webdriver,value):
        ''' select no auto start '''
        if (not self.isAutoStart(webdriver) and value) or (self.isAutoStart(webdriver) and not value):
            webdriver.find_element_by_xpath(self.dom_xpath_auto_start_checkbox).click()
    def isAutoStart(self,webdriver):
        time.sleep(5)
        result=True
        try:
            elem= webdriver.find_element_by_xpath(self.dom_xpath_is_auto_start_checkbox)
        except NoSuchElementException:
            result=False
        return result
    def setServerAdress(self,webdriver,server):
        ''' set server adress'''
        webdriver.find_element_by_css_selector(self.dom_css_server_address_input).click()
        time.sleep(2)
       
        try:  
            webdriver.find_element_by_xpath(self.dom_xpath_is_auto_start_checkbox).send_keys(server)
        except WebDriverException:
            print(WebDriverException)
        time.sleep(2)
    def getServerAdress(self,webdriver):
        return webdriver.find_element_by_xpath(self.dom_xpath_is_auto_start_checkbox).text
    def saveSettings(self,webdriver):
        webdriver.find_element_by_xpath(self.dom_xpath_save_button).click()
        