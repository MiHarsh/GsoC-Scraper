import requests ,bs4 ,re ,os
import json

from utils.maintainer import CategoryMaintainer
from utils.Loop import LoopThrough
from utils.extractor import LinkExtractor, GsocExtractor

os.system('clear')
print("#"*40)
print()

inp_year = input("Enter the years you want to scrape: ")
print()

print("The available categories are : ")
print('1)  web')
print('2)  science_and_medicine')
print('3)  end_user_applications')
print('4)  languages')
print('5)  other')
print('6)  cloud')
print('7)  graphics')
print('8)  security')
print('9)  operating_systems')
print('10) social_communications')
print('11) data_and_databases')
print()

inp_cat = input("Enter the categories you want to scrape: ")
print()

years      = [int(yr) for yr in inp_year.split(" ")]
categories = [cat for cat in inp_cat.split(" ")]

print("#"*40)
print()


lpt = LoopThrough(years,categories)
lpt.start_scraping()
