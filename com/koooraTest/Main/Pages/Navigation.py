from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from com.koooraTest.Main.Locators.locator import Locator
from com.koooraTest.Main.Pages.Today import Today
from com.koooraTest.Main.Utils.Utils import Utils
from selenium.webdriver.support import expected_conditions as EC


class Navigation:

    def __init__(self, driver):
        self.driver = driver
        self.mainPage = Locator.mainPageNavBtn
        self.todayMatches = Locator.todayMatchesBtn

    def get_main_page(self):
        try:
            print("locating main button in navbar .....")
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((self.mainPage['By'], self.mainPage['Value'])))

        except:
            Utils.printError("error locating main button in navbar")

    def get_today_matches(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((self.todayMatches['By'], self.todayMatches['Value'])))
        except:
            Utils.printError("error locating today matches button in navbar")

    def click_main_page(self):
        try:
            print("clicking main page in navbar ....")
            main_page = self.get_main_page()
            main_page.click()
        except:
            Utils.printError("error while trying to click main page in navbar")

    def click_today_matches(self):
        try:
            print("clicking on today matches nav .....")
            today_matches = self.get_today_matches()
            today_matches.click()
            return Today(self.driver)
        except:
            Utils.printError("error while trying to click today matches button in navbar")
