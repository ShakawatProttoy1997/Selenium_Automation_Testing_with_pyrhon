
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from openpyxl import load_workbook  # For Excel
import pandas as pd
from selenium.webdriver.common.keys import Keys
# Set up WebDriver (e.g., Chrome)
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from openpyxl import load_workbook

# Taking input from user
search_string = input("Input the URL or string you want to search for:")

search_string = search_string.replace(' ', '+')

browser = webdriver.Chrome()
elements = requests.get("https://www.google.com/search?q=" +
                                   search_string)
soup = BeautifulSoup(elements.text, 'html.parser')
result = soup.select('.cOl4Id a')

for path in result[:2]:
    print(path, "/n")
for i in range(1):
    matched_elements = browser.get("https://www.google.com/search?q=" +
                                   search_string + "&start=" + str(i))
    soup = BeautifulSoup.BeautifulSoup(matched_elements)
    f = open('excel.xlsx', 'w')
    f.write('Longest Option,Shortest Option')







