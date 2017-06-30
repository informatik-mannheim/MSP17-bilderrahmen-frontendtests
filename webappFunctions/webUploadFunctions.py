#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import selenium
import logging
import time

class UploadPage:
    dom_id_upload_submit_button='upload-submit'
    dom_id_images_upload_input='upload-files'
    dom_css_upload_type_file='input[type=file]'

    def uploadFile(self,webdriver,path):
        webdriver.find_element_by_css_selector(self.dom_css_upload_type_file).send_keys(path)
    def setDescriptionForPicture(self,webdriver,description,picture):
        webdriver.find_element_by_id(picture).send_keys(description)
    def setDescriptionsForPictures(self,webdriver,descriptionsAndPictures):
        for k in descriptionsAndPictures.keys():
            self.setDescriptionForPicture(webdriver,descriptionsAndPictures[k],k) 
    def getImagesAndDescriptions(self,webdriver):
        pass
    def uploadFiles(self,webdriver,paths):
        for i in paths:
            self.uploadFile(webdriver,i)
    def pressFileUploadSubmit(self,webdriver):
        webdriver.find_element_by_id(self.dom_id_upload_submit_button).click()