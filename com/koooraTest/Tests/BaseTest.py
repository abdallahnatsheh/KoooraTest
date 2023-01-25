from time import sleep

from selenium import webdriver

from com.koooraTest.Main.Locators import locator
from com.koooraTest.Main.Pages.Footer import Footer
from com.koooraTest.Main.Pages.Main import Main
from com.koooraTest.Main.Pages.Navigation import Navigation
from com.koooraTest.Main.Utils.Utils import Utils


class BaseTest:
    def __init__(self, driver):
        self.driver = driver

    def setUp(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(locator.Locator.url)


browser = webdriver.Chrome()
test = BaseTest(browser)
test.setUp()
mainPage = Main(browser)
Utils.assert_on_result(mainPage.is_main_page(), True,
                       "error in method is_main_page")
navigation = Navigation(browser)
Utils.assert_on_result(Utils.checkTitle(browser, "كووورة: الموقع العربي الرياضي الأول"), True,
                       "did not match main page title")

todayMatches = navigation.click_today_matches()
Utils.assert_on_result(Utils.checkTitle(browser, "مباريات اليوم"), True,
                       "did not match today matches page title")
league_matches = todayMatches.click_english_league_matches()
Utils.assert_on_result(Utils.checkTitle(browser, locator.Locator.league), True,
                       "did not match  league matches page title")
Utils.scroll_down(browser)
sleep(2)
Utils.scroll_up(browser)
sleep(2)
player_report_list = league_matches.click_goalers_list()
Utils.assert_on_result(Utils.checkTitle(browser, locator.Locator.league), True,
                       "did not match  league matches page title")
Utils.assert_on_result(Utils.isElementExist(player_report_list.get_player_report()), True,
                       "Locating player report text")

navigation = Navigation(browser)
navigation.click_main_page()
sleep(5)
Utils.scroll_down(browser)
sleep(2)
footer = Footer(browser)
copy_right = footer.click_copy_right_link()
Utils.assert_on_result(Utils.checkTitle(browser, "شروط الاستخدام"), True,
                       "did not match copyright page title")