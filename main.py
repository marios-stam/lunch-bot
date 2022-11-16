from scrappers.teknikens import TeknikensScrapper
from scrappers.central import CentralScrapper
import scrappers.utils as utils


def scrapeRestaurants():
    teknikens = TeknikensScrapper()
    teknikenMenu = teknikens.scrape()

    central = CentralScrapper()
    centralMenu = central.scrape()

    menus = {}
    menus["Teknikens"] = teknikenMenu
    menus["Central"] = centralMenu

    return menus


def createMenusMessage():
    menus = scrapeRestaurants()

    message = "LTU restaurants menu for today:\n\n"
    for restaurant, menu in menus.items():
        message += "======== "+restaurant+" ========" + "\n"
        for dish in menu:
            message += dish + "\n \n"
        message += "\n"

    print(message)
    return message


if __name__ == "__main__":
    # menus = scrapeRestaurants()

    # print("Teknikens:")
    # utils.printMenu(menus["teknikens"])

    # print("Central":)
    # utils.printMenu(menus["central"])
    createMenusMessage()
