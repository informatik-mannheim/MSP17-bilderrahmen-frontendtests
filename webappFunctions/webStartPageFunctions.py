#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
import selenium
import logging
import time
class StartPage:
    dom_id_sign_in_button='signin-button'
    dom_id_sign_out_button='signout-button'    
    
    dom_xpath_o_auth_i_frame='//body/iframe'
    dom_id_o_auth_another_account_button='identifierLink'
    dom_id_o_auth_mail_input='identifierId'
    dom_id_o_auth_mail_confirm_button='identifierNext'
    dom_xpath_o_auth_select_account_start="//div[@role='button']/div/p[@data-email='"
    dom_xpath_o_auth_select_account_end="']"
    dom_xpath_o_auth_pwd_input="//div[@id='password']/div/div/div/input[@type='password']"
    dom_id_o_auth_pwd_next_button='passwordNext'
    
    dom_id_picture_count='piccount'
    dom_xpath_link_to_pictures_page="//li/a[text()='Bilder löschen']"    
    dom_xpath_link_to_upload_page="//li/a[text()='Bilder hochladen']"
    dom_id_confirm_page_usage="submit_approve_access"
    
    attribute_selected_tab="aria-expanded"
    attribute_source="src"
    attribute_style="style"
    attribute_value_is_visible="display: none;"
    attirbute_value_title_o_auth_window="Log in"
    
    split_value_image_count_drive='/'
    
    def confirmPageUsage(self,webdriver,mail,pwd):
        if self.isLoggedIn(webdriver)==False:
            webdriver.find_element_by_id(self.dom_id_sign_in_button).click()   
            time.sleep(2)
            '''OAuth authentication needs new webdriver'''
            url = webdriver.find_element_by_xpath(self.dom_xpath_o_auth_i_frame).get_attribute("src")
            
            time.sleep(2)
            self.switchToOOutWindow(webdriver)
            time.sleep(5)
            # Fill in values            
            self.fillOAuthValues(webdriver,mail,pwd)
            time.sleep(2)        
            webdriver.find_element_by_id(self.dom_id_confirm_page_usage).click()
            time.sleep(2)   
            webdriver.switch_to_window(webdriver.window_handles[-1])
    
    def isPictures(self,webdriver):   
        if webdriver.find_element_by_xpath(self.dom_xpath_link_to_pictures_page).get_attribute(self.attribute_selected_tab)=="true":
            return True
        return False
    def isUpload(self,webdriver):     
        if webdriver.find_element_by_xpath(self.dom_xpath_link_to_upload_page).get_attribute(self.attribute_selected_tab)=="true":
            return True
        return False
    def switchToUploadPage(self,webdriver):
        webdriver.find_element_by_xpath(self.dom_xpath_link_to_upload_page).click()
    def switchToPicturesPage(self,webdriver):
        webdriver.find_element_by_xpath(self.dom_xpath_link_to_pictures_page).click()    
    def logOut(self,webdriver):
        if self.isLoggedIn(webdriver)==True:
            webdriver.find_element_by_id(self.dom_id_sign_out_button).click()            
    def logIn(self,webdriver,mail,pwd):
        if self.isLoggedIn(webdriver)==False:
            webdriver.find_element_by_id(self.dom_id_sign_in_button).click()   
            time.sleep(2)
            '''OAuth authentication needs new webdriver'''
            url = webdriver.find_element_by_xpath(self.dom_xpath_o_auth_i_frame).get_attribute(self.attribute_source)
            
            time.sleep(2)
            self.switchToOOutWindow(webdriver)
            time.sleep(5)
            # Fill in values            
            self.fillOAuthValues(webdriver,mail,pwd)
            time.sleep(2)
            webdriver.switch_to_window(webdriver.window_handles[-1])
    def logInChooseAccount(self,webdriver,mail):
        if self.isLoggedIn(webdriver)==False:
            webdriver.find_element_by_id(self.dom_id_sign_in_button).click()   
            time.sleep(2)
            '''OAuth authentication needs new webdriver'''
            url = webdriver.find_element_by_xpath(self.dom_xpath_o_auth_i_frame).get_attribute(self.attribute_source)
            
            time.sleep(2)
            self.switchToOOutWindow(webdriver)
            time.sleep(5)            
            webdriver.find_element_by_xpath(self.dom_xpath_o_auth_select_account_start+mail+self.dom_xpath_o_auth_select_account_end).click()
            
            time.sleep(2)
            webdriver.switch_to_window(webdriver.window_handles[-1])
            
    def switchToOOutWindow(self,webdriver):
        for handle in webdriver.window_handles:
            webdriver.switch_to_window(handle);
            elem = webdriver.title
            if self.attirbute_value_title_o_auth_window in elem:
                return
    def fillOAuthValues(self,webdriver,mail,pwd):        
        webdriver.find_element_by_id(self.dom_id_o_auth_mail_input).send_keys(mail)
        webdriver.find_element_by_id(self.dom_id_o_auth_mail_confirm_button).click()
        time.sleep(2)
        webdriver.find_element_by_xpath(self.dom_xpath_o_auth_pwd_input).send_keys(pwd)
        webdriver.find_element_by_id(self.dom_id_o_auth_pwd_next_button).click()
    def isLoggedIn(self,webdriver):
        try:
            visible=webdriver.find_element_by_id(self.dom_id_sign_in_button).get_attribute(self.attribute_style)
            if self.attribute_value_is_visible in visible: 
                return True
            else:
                return False
        except NoSuchElementException:
            return False
        return True
    def getImageCount(self,webdriver):
        value= webdriver.find_element_by_id(self.dom_id_picture_count).text
        value=value.split(self.split_value_image_count_drive,1)
        return int(value[0])
        