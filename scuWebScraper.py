import requests
from bs4 import BeautifulSoup

def scuwebscrpr(url):
    page = requests.get(url) 
    soup = BeautifulSoup(page.content,"html.parser")
    text = soup.findAll("div", {"class":"field-content"})
    
    for i in text: print i
    
    newtext = text[4].findAll("a")[0].get_text()
    time = text[5].findAll("div",{"class":"field-content"})[0].get_text()
    print newtext
    print text[5]
    
    #print time
    
scuwebscrpr("http://scupresents.org/")
