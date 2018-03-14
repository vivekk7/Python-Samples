import requests
from bs4 import BeautifulSoup

def webscrpr1(url):
    page = requests.get(url) 
    soup = BeautifulSoup(page.content,"html.parser")
    text = soup.findAll("table")
    #print text
    newtext = text[0].findAll("td")
    print newtext
    
    newlist = []
    for i in range(len(newtext)):
        newdict = {}
        
        newdict["day_and_date"] = newtext[i].findAll("h3")[0].get_text()
        newdict["max_temp"] = newtext[i].findAll("span",{"class":"large-temp"})[0].get_text()
        newdict["min_temp"] = newtext[i].findAll("span",{"class":"small-temp"})[0].get_text()
        newdict["weather condition"] = newtext[i].findAll("div",{"class":"cond"})[0].get_text()
        newdict["historical_high"] = newtext[i].findAll("span",{"class":"temp"})[0].get_text()
        newdict["average"] = newtext[i].findAll("span",{"class":"lo"})[0].get_text()
        newlist.append(newdict)
    
    
    for i in newlist: print i

webscrpr1("http://www.accuweather.com/en/us/briarcliff-manor-ny/10510/may-weather/2146224")
