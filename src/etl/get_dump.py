import requests
from bs4 import BeautifulSoup
from src.libcode import list_to_txt, txt_to_list
import io
import wikipediaapi # in terminal "pip3 install wikipedia-api"
import nltk
import nltk.data
nltk.download('punkt')
import pandas as pd
import datefinder # pip install datefinder

## NEED TO DEBUG
## ReadTimeout: HTTPSConnectionPool(host='en.wikipedia.org', port=443): Read timed out. (read timeout=10.0)
## See Cami3.ipynb for code development
def get_full_text():
    '''
    Given a list of Wikipedia articles, get the full current text. 
    The delimiter ^^^_ indicates a new article.
    :return: a txt file
    '''
    path = 'src/data/artnames.txt'
    art_lst = txt_to_list("artnames.txt")
    f = open("src/data/fulltext.txt","w+")
    for i in art_lst:
        enwiki = wikipediaapi.Wikipedia('en')
        f.write("^^^_" + i + "\n")
        f.write(enwiki.page(i).text + "\n")
    f.close()

def get_date(s1):
    '''
    Helper function for get_talk
    '''
    dates = datefinder.find_dates(s1, index = True)
    res = []
    find = []
    for d in dates:
        find = d
    if find != []:
        res.append(find[0])
        res.append(s1[0:find[1][0]])
    return res

def get_user(c, tl):
    '''
    Helper function for get_talk
    '''
    for u in tl:
        if u in c:
            return u
    return "N/A"

def get_list(soup):
    '''
    Helper function for get_talk
    '''
    hi = soup.find(id="pagehistory")
    ul = hi.find_all("li")
    li = []
    for u in ul:
        u0 = u.find(attrs={"class": "history-user"})
        u1 = u0.find("bdi")
        if type(u1) == type(None):
            li.append('N/A')
        else:
            li.append(u1.string)
    return li

## NEED TO FIX
## Currently makes a csv file for each article and puts them in the outermost directory.
## Need to consolidate to one csv and move to src/data.
## Look into empty csv for first article
def get_talk():
    '''
    Given a list of Wikipedia articles, get data from the talk/discussion page. 
    :return: a csv file
    '''
    path = 'src/data/artnames.txt'
    art_lst = txt_to_list("artnames.txt")
    wiki = wikipediaapi.Wikipedia('en')
    for article in art_lst[:2]: ## Testing; remove [:2] to run on all articles
        page = wiki.page("Talk:" + article)
        sections = page.sections
        sen_det = nltk.data.load("tokenizers/punkt/english.pickle")
        df = pd.DataFrame([],columns=[article,'Section','Comment','User','Datetime'])
        n=0
        th = BeautifulSoup(requests.get("https://en.wikipedia.org/w/index.php?title=" + "Talk:" + article + "&offset=&limit=500&action=history").content, features="html.parser")
        tl = get_list(th)
        for sec in sections:
            title = sec.title
            comments = sec.text.splitlines()
            for comment in comments:
                sents = sen_det.tokenize(comment)
                if len(sents) > 1:
                    met = sents[-1]
                else:
                    met = comment
                if '...' in met:
                    met = met.split('...')[-1]
                d = get_date(met)
                if d == []:
                    d.append('N/A')
                u = get_user(comment, tl)
                df = pd.concat([df,pd.DataFrame({'Section':title,'Comment':comment,'User':u,'Datetime':d[0]}, index = [n])])
                n = n+1
        on = article + "_comments.csv"
        out = open(on, "x")
        df.to_csv(path_or_buf=out)