from selenium.webdriver.support.wait import WebDriverWait

from com.koooraTest.Main.Locators.locator import Locator
from selenium.webdriver.support import expected_conditions as EC


class PlayerReport:
    def __init__(self, driver):
        self.driver = driver
        self.player_report_list = Locator.playerReportListText

    def get_player_report(self):
        print("getting player report list  text ...")
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((self.player_report_list['By'], self.player_report_list['Value'])))

        except:
            print("error getting english league matches text")