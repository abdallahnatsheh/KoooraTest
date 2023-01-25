class Utils:

    def isElementExist(self):
        if self is not None:
            return True
        return False

    def checkTitle(driver, exptcted_title):
        return driver.title == exptcted_title

    def assert_on_result(actual_result, expected_result, info_on_failed_match):
        try:
            assert actual_result == expected_result
        except:
            Utils.printError(info_on_failed_match)

    def scroll_down(driver):
        try:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        except:
            print("ERROR IN SCROLLING DOWN PAGE")

    def scroll_up(driver):
        try:
            driver.execute_script("window.scrollTo(0,-document.body.scrollTop)")
        except:
            Utils.printError("ERROR IN SCROLLING UP PAGE")

    def printError(error):
        print("FAILED  :: " + error.upper())
