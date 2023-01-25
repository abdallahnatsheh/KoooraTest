from selenium.webdriver.common.by import By

from com.koooraTest.Main.Locators.locator import Locator


class PlayerReport:
    def __init__(self, driver):
        self.driver = driver
        self.player_report_list = driver.find_element(By.XPATH, Locator.playerReportListText)

    def get_player_report(self):
        print("getting player report list  text ...")
        try:
            return self.player_report_list
        except:
            print("error getting english league matches text")