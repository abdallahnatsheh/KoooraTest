from selenium.webdriver.common.by import By


class Locator(object):
    # Locators for Koora Home Page
    league = "الدوري الألماني الدرجة الأولى"
    url = "https://www.kooora.com/"
    # navbar
    mainPageNavBtn = {
        'By': By.XPATH,
        'Value': "//a[@class='nav_li_link'][contains(text(),'الرئيسية')]"
    }
    todayMatchesBtn = {
        'By': By.XPATH,
        'Value': "//a[@class='nav_li_link'][contains(text(),'اليوم')]"
    }
    # home page
    importantMatchesTxt = {
        'By': By.XPATH,
        'Value': "//h3[@class='sideTitle']//a[contains(text(),'أهم المباريات')]"
    }
    featuredNewsId = {
        'By': By.ID,
        'Value': "featuredNews"
    }

    # Locators for today's matches page
    englishLeagueText = {
        'By': By.XPATH,
        'Value': f'//a[contains(text(),"{league}")]'
    }

    # League matches page
    goalersListText = {
        'By': By.XPATH,
        'Value':  "//a[contains(text(),'قائمة الهدافين')]"
    }

    # Player report list page
    playerReportListText = {
        'By': By.XPATH,
        'Value': f'//span[contains(text(),"{league}")]'
    }

    # Footer
    copyRight = {
        'By': By.LINK_TEXT,
        'Value':  "سياسة الاستخدام"
    }
