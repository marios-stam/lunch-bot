import time

# import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from googletrans import Translator
import utils
# from google_trans_new import google_translator


class CentralScrapper:

    def __init__(self) -> None:
        self.url = "https://www.foodandco.se/restauranger/restauranger/centrumrestaurangen/"

    def scrape(self):
        date = utils.getDateYYMMDD()
        print(date)
        date = "2022-11-04"

        self.getDayText(date)
        self.splitDay()
        self.day = self.translateDay(self.day)

        for dish in self.day:
            print(dish)

        return self.day

    def getDayText(self, date):
        # start by defining the options
        options = webdriver.ChromeOptions()
        options.headless = True  # it's more scalable to work in headless mode
        # normally, selenium waits for all resources to download
        # we don't need it as the page also populated with the running javascript code.
        options.page_load_strategy = 'none'
        # this returns the path web driver downloaded
        chrome_path = ChromeDriverManager().install()
        chrome_service = Service(chrome_path)
        # pass the defined options and service objects to initialize the web driver
        driver = Chrome(options=options, service=chrome_service)
        driver.implicitly_wait(5)

        url = "https://www.foodandco.se/restauranger/restauranger/centrumrestaurangen/"

        driver.get(url)
        time.sleep(10)

        # content = driver.find_element(By.CSS_SELECTOR, "div[class*='ItemsGridWithPostAtcRecommendations'")
        # breads = content.find_elements(By.TAG_NAME, "li")

        day = driver.find_elements(By.ID, date)
        day = day[0].get_attribute("innerHTML")

        self.dayText = day

    def splitDay(self):
        day = self.dayText.split("<strong>")[1:]
        for i, dish in enumerate(day):
            # dish = dish.split("</strong>")[0]
            dish = self.removeTags(dish)
            day[i] = dish

        self.day = day

    def translateDay(self, day, translator=None):
        # translate swedish to english
        if translator is None:
            translator = Translator(service_urls=['translate.googleapis.com'])
        # translator = google_translator()

        for i, dish in enumerate(day):
            translatedDish = utils.translateSwedish(dish, translator)
            day[i] = translatedDish

        return day

    def removeTags(self, day):
        day = day.replace("</strong>", "")
        day = day.replace("<br>", "")

        if "</p>" in day:
            day = day.split("</p>")[0]

        return day


def loadDayText():
    # laod text from file
    with open("day.txt", "r") as f:
        day = f.read()

    return day


if __name__ == "__main__":

    central = CentralScrapper()
    central.scrape()
