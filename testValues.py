#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

WEBAPP_IMAGES_FOLDER=os.sep+'testImages'+os.sep
WEBAPP_VALUE_TEST_IMAGE_1 = "1.jpg"
WEBAPP_VALUE_TEST_DESCRIPTION_1=WEBAPP_VALUE_TEST_IMAGE_1 + " Description"

WEBAPP_VALUE_TEST_IMAGE_2 = "2.jpg"
WEBAPP_VALUE_TEST_DESCRIPTION_2=WEBAPP_VALUE_TEST_IMAGE_2 + " Description"

WEBAPP_VALUE_TEST_IMAGE_3 = "3.jpg"
WEBAPP_VALUE_TEST_DESCRIPTION_3=WEBAPP_VALUE_TEST_IMAGE_3 + " Description"

WEBAPP_VALUE_TEST_IMAGE_4 = "3.jpg"
WEBAPP_VALUE_TEST_DESCRIPTION_4=WEBAPP_VALUE_TEST_IMAGE_4 + " Description"

WEBAPP_VALUE_TEST_IMAGE_5 = "5.jpg"
WEBAPP_VALUE_TEST_DESCRIPTION_5=WEBAPP_VALUE_TEST_IMAGE_5 + " Description"

WEBAPP_VALUE_TEST_IMAGE_BIG="big.jpg"
WEBAPP_VALUE_TEST_DESCRIPTION_BIG=WEBAPP_VALUE_TEST_IMAGE_BIG + " Description"

WEBAPP_VALUE_TEST_INVALID_IMAGE_1="1.txt"
WEBAPP_VALUE_TEST_INVALID_IMAGE_DESCRIPTION_1=WEBAPP_VALUE_TEST_INVALID_IMAGE_1 + " Description"

WEBAPP_VALUE_TEST_INVALID_IMAGE_2="1.pdf"
WEBAPP_VALUE_TEST_INVALID_IMAGE_DESCRIPTION_2=WEBAPP_VALUE_TEST_INVALID_IMAGE_2 + " Description"