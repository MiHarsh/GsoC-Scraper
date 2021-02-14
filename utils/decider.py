import json

class Decider:
    
    def __init__(self,counts,tech):
        
        self.category         = None
        self.counts           = counts
        self.tech             = tech
        self.count_only       = []
        self.tech_stacks_only = []
        self.combined         = []
        
    def apply_filter(self):
        
        try:
            with open('categories.json') as f:
                self.category = json.load(f)
            
            for keys in self.category.keys():
                for sup_keys in self.category[keys].keys():
                    c1 = 0;c2 =0;
                    if len(self.category[keys][sup_keys]['years']) >= self.counts:
                        self.count_only.append(sup_keys)
                        c1 = 1
                    for kw in self.tech:
                        if kw in self.category[keys][sup_keys]['tech']:
                            self.tech_stacks_only.append(sup_keys)
                            c2 = 1
                            break
                    if c1+c2 ==2:
                        self.combined.append(sup_keys)
            
            with open('filter_apply.txt','a+') as f:
                f.writelines("#"*40 + "\n\n")
                f.writelines(f"Count : {self.counts} ")
                f.writelines(f"Tech Stacks : {', '.join(self.tech)}\n\n")
                f.writelines(f"Available options combined filter : {', '.join(self.combined)}\n\n")
                f.writelines(f"Available options tech stacks only : {', '.join(self.tech_stacks_only)}\n\n")
                f.writelines(f"Available options on the basis of count : {', '.join(self.count_only)}\n\n")
            
        except:
            print("Looks like you haven't scraped the data, please scrape first \n")
        