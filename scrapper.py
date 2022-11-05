"""This script will search each LTU restaurany's menu and parse it"""

import requests
from bs4 import BeautifulSoup

# URL to the Teknikens restaurant's menu
urlTeknikens = "https://www.teknikenshus.se/restaurang"

headers = {"User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}

# Parse the HTML
pageTeknikens = requests.get(urlTeknikens, headers=headers)
soupTeknikens = BeautifulSoup(pageTeknikens.content, 'html.parser')

# Find the menu by class
menuTeknikens = soupTeknikens.find("strong", class_='matochmat-wrap__day-heading')

monday = soupTeknikens.find("Fredag")
print(monday)

# Print the menu
print(menuTeknikens)
