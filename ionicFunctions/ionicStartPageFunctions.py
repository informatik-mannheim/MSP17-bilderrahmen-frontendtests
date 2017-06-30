'''
Start Page is the oauth dialog. Chose an google account.
The device needs the Google Account to be selectable. It is not possible to add a existing Google Account to the app within the app or create one.

Use of native context.
'''
from selenium.common.exceptions import *
import time
class StartPage:
    id_selectable_google_accounts='com.google.android.gms:id/account_name'
   

    def useGoogleAccount(self,webdriver,mail,pwd):

        webdriver.switch_to.context("NATIVE_APP")
        time.sleep(5) 
        accounts=webdriver.find_elements_by_id(self.id_selectable_google_accounts)
        for i in accounts:
            try:
                if i.text==mail:
                    i.click() 
                    webdriver.switch_to.context("WEBVIEW_de.hsmannheim.bilderrahmen")
                    time.sleep(5)
                    return
            except:
                print("text konnte nicht gelesen werden.")
                webdriver.switch_to.context("WEBVIEW_de.hsmannheim.bilderrahmen")
                time.sleep(5)
        webdriver.switch_to.context("WEBVIEW_de.hsmannheim.bilderrahmen")
        time.sleep(5)
    def isStartPage(self,webdriver):
        webdriver.switch_to.context("NATIVE_APP")
        result=True
        try:
            webdriver.find_element_by_id(self.id_selectable_google_accounts)
        except NoSuchElementException:
            result=False
        webdriver.switch_to.context("WEBVIEW_de.hsmannheim.bilderrahmen")
        return result
        