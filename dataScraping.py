from bs4 import BeautifulSoup
import urllib.request
import requests
import os


def links():
    directory =  'http://transcripts.foreverdreaming.org/viewforum.php?f=177&start='
    urls= []

    for i in range(9):
        urls.append(directory + str(25*i))
    return urls
    
def scriptLinks():
    pages = links()
    parser = 'html.parser'
    baseURL = 'http://transcripts.foreverdreaming.org'

    scripts = []
    for page in pages:
        resp = urllib.request.urlopen(page)
        soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
        for link in soup.find_all('a', href=True):
            if '&t=' in link['href']:
                scripts.append(baseURL + link['href'][1:])
    
    return scripts

def retrieveScripts():
    scripts = scriptLinks()
    parser = 'html.parser'

    for scriptLink in scripts:
        resp = urllib.request.urlopen(scriptLink)
        soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
        episodeTitle = soup.find_all('h2')[0].get_text()
        if 'Online Store' in episodeTitle or 'Board Update' in episodeTitle:
            continue

        season = episodeTitle[:2]
        episodeNum = episodeTitle[3:5]
        print(season)
        print(episodeNum)
        path = '/Users/abhishekkumar/Documents/programming/himym/data/Season-' + season + '/Episode-' + episodeNum + '.txt'
        with open(path,'w') as out:
            for p in soup.find_all('p')[1:len(soup.find_all('p'))-3]:
                out.write(p.get_text()+'\n')

retrieveScripts()