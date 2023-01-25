from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from com.koooraTest.Main.Locators.locator import Locator
from com.koooraTest.Main.Pages.CopyRight import CopyRight
from com.koooraTest.Main.Utils.Utils import Utils


class Footer:
    def __init__(self, driver):
        self.driver = driver
        self.copy_right = Locator.copyRight

    def get_copy_right_link(self):
        print("getting copyright link  ...")
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((self.copy_right['By'], self.copy_right['Value'])))

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

