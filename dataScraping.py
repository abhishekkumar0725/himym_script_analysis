from bs4 import BeautifulSoup
import urllib.request

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

    for scriptLink in scripts:

    
scriptLinks()