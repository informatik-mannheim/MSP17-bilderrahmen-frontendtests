#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import selenium
import logging
import time

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC

class PicturesPage:
    
    dom_css_images='.thumbnail-div'
    dom_css_delete='.close'
    #dom_id_confirm_delete_button='delete_button'
    
    
    def deleteFiles(self,webdriver):
        pict=webdriver.find_elements_by_css_selector(self.dom_css_delete)
        for p in pict:
            hover = ActionChains(webdriver).move_to_element(p).click()
            hover.perform()
            #WebDriverWait(webdriver, 10).until(wait_modal_is_visible((By.ID, 'myid'), "wait for modal"))
            #p.click()
            #time.sleep(15)
            #driver.switchTo().activeElement();
            #webdriver.find_element_by_id(self.dom_id_confirm_delete_button).click()
            time.sleep(5)
    def getImagePreviewCount(self,webdriver):
        return len(webdriver.find_elements_by_css_selector(self.dom_css_images))
        
        