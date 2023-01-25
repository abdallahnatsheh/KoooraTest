from selenium.webdriver.common.by import By

from com.koooraTest.Main.Locators.locator import Locator
from com.koooraTest.Main.Pages.CopyRight import CopyRight
from com.koooraTest.Main.Utils.Utils import Utils


class Footer:
    def __init__(self, driver):
        self.driver = driver
        self.copy_right = driver.find_element(By.LINK_TEXT, Locator.copyRight)

    def get_copy_right_link(self):
        print("getting copyright link  ...")
        try:
            return self.copy_right
        except:
            Utils.printError("error getting copy right link in footer")

    def click_copy_right_link(self):
        try:
            print("clicking on copy right link ....")
            copy_right_link = self.get_copy_right_link()
            copy_right_link.click()
            return CopyRight(self.driver)
        except:
            Utils.printError("error while trying to click copyright link in footer")

