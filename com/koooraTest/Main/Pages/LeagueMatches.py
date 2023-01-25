from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.koooraTest.Main.Locators.locator import Locator
from com.koooraTest.Main.Pages.PlayerReport import PlayerReport
from com.koooraTest.Main.Utils.Utils import Utils


class LeagueMatches:

    def __init__(self, driver):
        self.driver = driver
        self.goaler_list = Locator.goalersListText

    def get_goaler_list(self):
        try:
            print("locating main button in navbar .....")
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((self.goaler_list['By'], self.goaler_list['Value'])))

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
