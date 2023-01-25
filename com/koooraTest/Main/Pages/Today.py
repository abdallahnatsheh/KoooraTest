from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from com.koooraTest.Main.Locators.locator import Locator
from com.koooraTest.Main.Pages.LeagueMatches import LeagueMatches
from com.koooraTest.Main.Utils.Utils import Utils


class Today:
    def __init__(self, driver):
        self.driver = driver
        self.english_league = Locator.englishLeagueText

    def get_english_league_matches(self):
        print("getting english league matches text ...")
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((self.english_league['By'], self.english_league['Value'])))

        except:
            Utils.printError("error getting english league matches text")

    def click_english_league_matches(self):
        try:
            print("clicking on english league matches text ....")
            english_league_matches = self.get_english_league_matches()
            english_league_matches.click()
            return LeagueMatches(self.driver)
        except:
            Utils.printError("error while trying to click today matches button in navbar")
