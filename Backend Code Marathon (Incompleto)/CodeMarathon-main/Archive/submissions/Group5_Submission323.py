import json
import time 
from random import randint


def search_keyword(keyword):
    urls = searchUrlsByWord(keyword)
    return {"urls" : urls}


def getUrlNumber():
    url_num = getUrlNum()
    return {"url_num" : url_num}
    
    
def createNewShortUrl(url):
    
    maybeExtension = generateToken()
    while maybeExtension in data.values():
        maybeExtension = generateToken()
        
    data["urlToToken"][url] = maybeExtension
    data["tokenToUrl"][maybeExtension] = url
    
    return {"shortUrl": baseDomain + maybeExtension}


def getLeaderboard():
    leaderboard = showLeaderboard()
    return {"leaderboard" : leaderboard}


baseDomain = "https://shortyurl.ss/" # FIXME maybe mudar?
maxLen = 30 - len(baseDomain)
allowedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_~"

data = {
    
    "urlToToken": {},
    "tokenToUrl": {}
    
    
}
keywordsStats = {}

"""
Exemplo da variável data:
data = {
    
    "urlToToken": { 
        "google.com": "awdahwud",
        "facebook.com": "a2131c"
    },      
    "tokenToUrl": { 
        "awdahwud": "google.com",
        "a2131c: "facebook.com"
    },      
    "nrUrls": "69",
    "keywordsStats" : {
        "albino" : "1", 
        "hey_people" : "2"
    }
    
}

[{"keyword": "ola", "nr_procuras":"5"}, {"keyword": "boas", "nr_procuras":"3"}, {}]


"""


"""
Given an url, generates the url to be appended to the base domain.
"""
def generateToken():
    url = ""
    for i in range(maxLen):
        index = randint(0, 64)
        url += allowedChars[index]
    return url

"""
@app.route('/searchKeyword/', ['POST'])
def search_keyword():
    request.json["keyword"]
    transformar(url)#get_urls 
    return {"url": url}
"""



def extractTokenGivenUrl(shortUrl):
    # Verifies if the url is valid
    if not shortUrl.startswith(baseDomain):
        return -1
    # Returns the token
    return shortUrl[len(baseDomain):]
 
    
"""
@app.route('/createNewShortUrl/', ['POST'])
def createNewShortUrl(url):
    url = request.json["url"]
    
    maybeExtension = generateToken()
    while maybeExtension in data.values():
        maybeExtension = generateToken()
        
    data["urlToToken"][url] = maybeExtension
    data["tokenToUrl"][maybeExtension] = url
    
return {"shortUrl": baseDomain + maybeExtension}
"""


def getBothUrls(shortUrl):
    token = extractTokenGivenUrl(shortUrl)
    url = getUrl(token)
    return {"shortUrl": shortUrl, "url": url} 


def getUrl(token):
    return data["tokenToUrl"][token]

    
def getToken(url):
    return data["urlToToken"][url]
    

def searchUrlsByWord(word):
    pairs = []
    urls = list(data["urlToToken"])
    for url in urls:
        pair = {}
        if word in url:
            
            pair["url"] = url
            pair["shortUrl"] = baseDomain + data["urlToToken"][url] 
            pairs += pair
            
    return pairs
   
   
def updateUrl(oldUrl, newUrl):
    
    token = data["urlToToken"][oldUrl]
    
    del data["urlToToken"][oldUrl]
    
    data["urlToToken"][newUrl] = token
    data["tokenToUrl"][token] = newUrl
    

def save_data():
    with open('data.json', 'w') as fp:
        json.dump(data, fp)


def load_data():
    with open('data.json', 'r') as fp:
        d = json.load(fp)
    return d


def addToLeaderboard(key_word):
    if key_word not in keywordsStats:
        data["keywordsStats"][key_word] = 1
    else:
        data["keywordsStats"][key_word] += 1


def showLeaderboard():
    sortedList = []
    
    for i in sorted(data["keywordsStats"], key = data["keywordsStats"].get, reverse=True):
        par = {"nrProcuras": data["keywordsStats"][i], "palavra": i}
        sortedList.append(par)

    return sortedList 
    

def getUrlNum():
    return int(data[nrUrls])

def main():
    save_data()
    
    """start_time = time()
    while True:
        if int(time()) % 5 == 0:
            save_data() """

    while True:
        a = input("Qual operacao desejas executar:\n1 - encurtar URL\n2 - Ver Leaderboard\n3 - pesquisa por palavras-chave\n4 - ver N# total de urls guardados\nIntroduza o numero da operacao: ")
        if a == '1':
            url = input("introduza o URL:")
            print("O url reduzido é", createNewShortUrl(url)["shortUrl"])
            save_data()           
        elif a == "2":
            print(showLeaderboard())
            
        
        elif a == "3":
            shortURL = input("introduza o shortURL:")
            print("O url associado é ", getBothUrls(shortURL))

        elif a == "4":
            print(getUrlNum())

        
        
    

if __name__ == "__main__":
    main()