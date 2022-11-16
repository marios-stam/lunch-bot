import time

# import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from googletrans import Translator
import scrappers.utils as utils
# from google_trans_new import google_translator


class TeknikensScrapper:

    def __init__(self) -> None:
        self.url = "https://www.teknikenshus.se/restaurang"

    def scrape(self):
        self.getWeekText()
        # self.weekText = loadWeekText()
        self.splitWeekText()

        # Select today's menu
        currentDay = utils.getWeekdayIndex()
        # currentDay = 3  # for testing
        dayMenu = self.selectDay(currentDay)

        # Translate today's menu
        dayMenu = self.translateDay(dayMenu)

        # for dish in dayMenu:
        #     print(dish)

        return dayMenu

    def getWeekText(self):
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

        url = self.url

        driver.get(url)
        time.sleep(10)

        # content = driver.find_element(By.CSS_SELECTOR, "div[class*='ItemsGridWithPostAtcRecommendations'")
        # breads = content.find_elements(By.TAG_NAME, "li")

        week = driver.find_elements(By.CLASS_NAME, "matochmat-wrap")
        week = week[0].text

        self.weekText = week

    def splitWeekText(self):
        weekText = self.weekText

        # split text into days
        weekMenu = []

        days = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag"]
        for i, day in enumerate(days):

            if i == len(days) - 1:
                dayMenu = weekText.split(day)[1]
            else:
                dayMenu = weekText.split(day)[1].split(days[i+1])[0]

            # remove first line (day and date)
            dayMenu = dayMenu.splitlines()[1:]

            # remove empty lines
            dayMenu = [line for line in dayMenu if line.strip() != ""]

            weekMenu.append(dayMenu)

        self.weekMenu = weekMenu

    def selectDay(self, dayIndex):
        # select day
        day = self.weekMenu[dayIndex]
        if dayIndex == 4:
            # discard last 4 lines
            day = day[:-4]

        return day

    def translateDay(self, day, translator=None):
        # translate swedish to english
        if translator is None:
            translator = Translator(service_urls=['translate.googleapis.com'])
        # translator = google_translator()

        for i, dish in enumerate(day):
            translatedDish = utils.translateSwedish(dish, translator)
            day[i] = translatedDish

        return day


def loadWeekText():
    # laod text from file
    with open("week.txt", "r") as f:
        week = f.read()

    return week


if __name__ == "__main__":
    teknikens = TeknikensScrapper()

    menu = teknikens.scrape()

    for dish in menu:
        print(dish)
