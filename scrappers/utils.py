from datetime import datetime


def getWeekdayIndex():
    return datetime.today().weekday()


def translateSwedish(text, translator):
    # translate swedish to english
    translation = translator.translate(text, dest='en')

    return translation.text


def getDateYYMMDD():
    return datetime.today().strftime("%Y-%m-%d")


if __name__ == "__main__":
    print(getWeekdayIndex())
