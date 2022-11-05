from scrapperTeknikens import TeknikensScrapper


def scrapeRestaurants():
    teknikens = TeknikensScrapper()
    teknikenMenu = teknikens.scrape()

    menus = {}
    menus["teknikens"] = teknikenMenu

    return menus


if __name__ == "__main__":
    menus = scrapeRestaurants()
    print(menus["teknikens"])
