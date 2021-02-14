import requests ,bs4 ,re
import json

def get_soup(url):
    req  = requests.get(url)
    soup = bs4.BeautifulSoup(req.text,'lxml')
    return soup

def get_dictionary(title,link,desc,tech,topics,year):
    '''
    title : title of the organisation
    link  : link of the organisation
    desc  : description about the organisation
    tech  : technologies used
    topics : topic tags
    
    '''

    temp = {}
    temp['link']  = link
    temp['description']  = desc
    temp['tech'] = tech
    temp['topics'] = topics
    temp['years'] = [year]
    
    return {title:temp}

class LinkExtractor:
    
    def __init__(self,year,category):
        
        self.year     = year
        self.category = category
        self.sub_links = []
        
    def get_orgs(self):
        
        base_url = "https://summerofcode.withgoogle.com/archive/"
        soup = get_soup(base_url + f'{self.year}/organizations/?category={self.category}')
        out = soup.find_all('a', href=True)
        for o in out:
            if re.search(r'/archive/\d{4}/organizations/\d+/',o['href']):
                self.sub_links.append('https://summerofcode.withgoogle.com' + o['href'])
        print(f"A total of {len(self.sub_links)} orgs were selected with {self.category} category in year {self.year}")
    
        return self.sub_links

    
class GsocExtractor:
    
    def __init__(self,sub_links,year):
        
        self.sub_links = sub_links
        self.year      = year
        
    def extract_sublinks(self):
        
        temp_dict = {}
        
        for link in self.sub_links:
            soup = get_soup(link)
            
            title = "".join(re.split(r'<h3 class="banner__title">|</h3>',str(soup.find_all('h3',{'class':'banner__title'})[0])))
            link  = re.split(r'href="|" target',str(soup.find_all('a',{'class':'org__link'})[0]))[1]
            desc = re.split(r'<p>+?|</p>?|\]|\[',str(soup.find_all('p')[1:]))
            desc = "".join(desc)

            tech = soup.find_all('li',{'class':'organization__tag organization__tag--technology'})
            tech = "".join(re.split(r'<li class="organization__tag organization__tag--technology">|</li>|\]|\[',str(tech)))

            topics = soup.find_all('li',{'class':'organization__tag organization__tag--topic'})
            topics = "".join(re.split(r'<li class="organization__tag organization__tag--topic">|</li>|\]|\[',str(topics)))
            
            dcs = get_dictionary(title,link,desc,tech,topics,self.year)
            temp_dict.update(dcs)
            
        return temp_dict