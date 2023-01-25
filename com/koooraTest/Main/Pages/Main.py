from selenium.webdriver.common.by import By

from com.koooraTest.Main.Locators.locator import Locator
from com.koooraTest.Main.Pages.Navigation import Navigation
from com.koooraTest.Main.Utils.Utils import Utils


class Main:

    def __init__(self, driver):
        self.driver = driver
        self.importantMatches = driver.find_element(By.XPATH, Locator.importantMatchesTxt)
        self.featuredNews = driver.find_element(By.ID, Locator.featuredNewsId)
        self.nav = Navigation(driver)

    def get_important_matches(self):
        try:
            print("getting important matches ....")
            return self.importantMatches
        except:
            Utils.printError("error getting important matches")

    def get_featured_news(self):
        try:
            print("getting featured news ...")
            return self.featuredNews
        except:
            Utils.printError("error getting featured news")

    def is_main_page(self):
        print("check if main page is shown ....")
        try:
            if Utils.isElementExist(self.get_featured_news()) and Utils.isElementExist(
                    self.get_important_matches()) and Utils.isElementExist(
                    self.nav.get_main_page()) and Utils.isElementExist(self.nav.get_today_matches()):
                return True
            return False
        except:
            Utils.printError("error in checking we are in main page")
            return False
