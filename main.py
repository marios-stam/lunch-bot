from scrappers.teknikens import TeknikensScrapper
from scrappers.central import CentralScrapper
from scrappers import utils


def scrapeRestaurants():
    teknikens = TeknikensScrapper()
    teknikenMenu = teknikens.scrape()

    central = CentralScrapper()
    centralMenu = central.scrape()

    menus = {}
    menus["teknikens"] = teknikenMenu
    menus["central"] = centralMenu

    return menus


if __name__ == "__main__":
    menus = scrapeRestaurants()

    print("Teknikens:")
    utils.printMenu(menus["teknikens"])

    print("Central":)
    utils.printMenu(menus["central"])
