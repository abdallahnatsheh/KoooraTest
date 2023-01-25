class Locator(object):
    # Locators for Koora Home Page
    league = "الدوري الألماني الدرجة الأولى"
    # navbar
    mainPageNavBtn = "//a[@class='nav_li_link'][contains(text(),'الرئيسية')]"
    todayMatchesBtn = "//a[@class='nav_li_link'][contains(text(),'اليوم')]"
    # home page
    importantMatchesTxt = "//h3[@class='sideTitle']//a[contains(text(),'أهم المباريات')]"
    featuredNewsId = "featuredNews"

    # Locators for today's matches page
    englishLeagueText = f'//a[contains(text(),"{league}")]'

    # League matches page
    goalersListText = "//a[contains(text(),'قائمة الهدافين')]"

    # Player report list page
    playerReportListText = f'//span[contains(text(),"{league}")]'

    # Footer
    copyRight = "سياسة الاستخدام"
