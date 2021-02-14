import json

class CategoryMaintainer:
    
    def __init__(self):
        
        try:
            with open('categories.json') as f:
                self.categories = json.load(f)
        except:
            self.categories =  {   'web':dict(),
                            'science_and_medicine':dict(),
                            'end_user_applications':dict(),
                            'languages':dict(),
                            'other':dict(),
                            'cloud':dict(),
                            'graphics':dict(),
                            'security':dict(),
                            'operating_systems':dict(),
                            'social_communications':dict(),
                            'data_and_databases':dict()
            }
        
    def update(self,temp_dict,category):
        for keys in temp_dict.keys():
            if keys in self.categories[category].keys():
                self.categories[category][keys]['years'].append(temp_dict[keys]['years'][0])
            else:
                self.categories[category][keys] = temp_dict[keys]
                
        with open('categories.json', 'w+') as f:
            json.dump(self.categories, f)
        