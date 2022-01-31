# Android environment
import unittest

import self as self
from Tools.scripts.win_add2path import PATH
from appium import webdriver


def launchApp():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7.0',
        'automationName': 'uiautomator2',
        'deviceName': 'HI5HGUSS99999999',
        'app': 'F:/All Desktop/MobileAutomation/src_main_resources/mocafi-irc.apk'
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    '''el = self.driver.find_element_by_accessibility_id('item')
    el.click()'''


launchApp()
