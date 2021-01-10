import requests
from bs4 import BeautifulSoup
import os

def scrape(fname="artnames.txt"):
    # request social and political philosophy index
    spp_resp = requests.get("https://en.wikipedia.org/wiki/Index_of_social_and_political_philosophy_articles")
    # request political index
    pol_resp = requests.get("https://en.wikipedia.org/wiki/Index_of_politics_articles")
    # soupify
    spp_soup = BeautifulSoup(spp_resp.text)
    pol_soup = BeautifulSoup(pol_resp.text)

    # make a combined list of article names
    fin_list = []

    # the bs4 part is hardcoded and quite arbitrary, if wikipedia structure changes this code won't work
    for i in spp_soup.find_all("ul")[1:26]:
        for j in i.find_all("a"):
            fin_list.append(j.get("title"))
            
    for i in pol_soup.find_all("p")[1:]:
        for j in i.find_all("a"):
            fin_list.append(j.get("title"))
       
    # remove duplicates     
    fin_list = list(set(fin_list))

    # write to file
    with open("src/data/"+fname, "w") as wfile:
        for i in fin_list[:-1]:
            try:
                wfile.write('%s~!~' % i)
            except:
                print(i + " was not included.") 
         
    try:
        wfile.write(fin_list[-1])
    except:
        print(i + " was not included.")

    return fname

def retrieve(fname="artnames.txt"):
    with open("src/data/" + fname, "r") as rfile:
        fullstr = rfile.read()
    artnames = fullstr.split("~!~")
    return artnames