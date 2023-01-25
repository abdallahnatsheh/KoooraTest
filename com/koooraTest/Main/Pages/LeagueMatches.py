from selenium.webdriver.common.by import By

from com.koooraTest.Main.Locators.locator import Locator
from com.koooraTest.Main.Pages.PlayerReport import PlayerReport
from com.koooraTest.Main.Utils.Utils import Utils


class LeagueMatches:

    def __init__(self, driver):
        self.driver = driver
        self.goaler_list = driver.find_element(By.XPATH, Locator.goalersListText)

    def get_goaler_list(self):
        try:
            print("locating main button in navbar .....")
            return self.goaler_list
        except:
            Utils.printError(" error locating goaler list in page")

    def click_goalers_list(self):
        try:
            print("clicking on english league matches text ....")
            goalers_list = self.get_goaler_list()
            goalers_list.click()
            return PlayerReport(self.driver)
        except:
            Utils.printError("error while trying to click goaler list")
