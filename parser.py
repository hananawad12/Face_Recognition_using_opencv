import requests
from bs4 import BeautifulSoup
import webbrowser

#Get info from  official websites

#Get the data from the url
def parse(url):
    data={}
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser") 
    divs=soup.find_all("div", class_="person person__table")
    for d in divs:
        name=d.find('div', attrs={'class': 'person__name'}).text.replace("\n", "").replace("\r", "").replace("\t","").strip()
        position=d.find('div', attrs={'class': 'person__post'}).text.replace("\n", "").replace("\r", "").strip()
        link=d.find('a').get('href')
        data[name]=[position,link]
        
        
    return data


#get the personal information for one person
def find_info(url,names):
    flag=0
    data=parse(url)
    for name in names:
        for k,v in data.items():
            splitted_name=[n.lower() for n in k.split()]
            if name.lower() in splitted_name:
                flag=1
                print("Personal Information:")
                print(k,'\n',v[0])
                webbrowser.open(v[1])
    return flag
    
    
    
    



