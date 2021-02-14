import requests ,bs4 ,re
import json
from utils.extractor import LinkExtractor, GsocExtractor
from utils.maintainer import CategoryMaintainer


cm = CategoryMaintainer() 

class LoopThrough:
    
    def __init__(self,year,categories):
        
        self.years         = year
        self.categories    = categories
        
        try:
            with open('scraped.txt','r+') as f:
                check_open = f.readlines()
            self.early_scraped = check_open[0].split(" ")
            f.close()
        except:
            self.early_scraped = []
        
        
    def start_scraping(self):
        
        for year in self.years:
            for cat in self.categories:
                if self.early_scraped != []:
                    if str(year)+cat not in self.early_scraped:
                        le = LinkExtractor(year,cat)
                        sub_list = le.get_orgs()
                        gs = GsocExtractor(sub_list,year)
                        temp_dicts = gs.extract_sublinks()
                        cm.update(temp_dicts,cat)
                        self.early_scraped.append(str(year)+cat)
                    else:
                        print(f"Skipping, year {year} category {cat} already scraped !!")
                        print()
                else:
                    le = LinkExtractor(year,cat)
                    sub_list = le.get_orgs()
                    gs = GsocExtractor(sub_list,year)
                    temp_dicts = gs.extract_sublinks()
                    cm.update(temp_dicts,cat)
                    self.early_scraped.append(str(year)+cat)
                    
                with open('scraped.txt','w+') as f:
                    f.writelines(" ".join(self.early_scraped))
                f.close()
                
        print("Successfully Scraped")
        print("Run the filters.py to apply filters and view the results")
        print()
