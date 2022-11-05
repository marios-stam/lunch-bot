from datetime import datetime


def getWeekdayIndex():
    return datetime.today().weekday()


if __name__ == "__main__":
    print(getWeekdayIndex())
