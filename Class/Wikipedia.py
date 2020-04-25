import requests
import json
import sys

class Wikipedia:
    def __init__(self, city):
        self.city = city

    def title(self):
        """
        Capitalize first letter from a place/city and after
        every space.
        ie: new york => New York 
        """
        info = 0
        temp1 = ""
        temp2 = []

        for i in self.city:
            if info == 1:
                i = i.capitalize()
                info = 0
            if i == " ":
                i = "_"
                info = 1
            temp2.append(i)
        if temp2[0].upper() != temp2[0]:
            temp2[0] = temp2[0].capitalize()
        wikititle = temp1.join(temp2)
        
        return wikititle

    def wikipage(self):
        """
        Call wikipedia API with city/place as parameter and report the first title
        result from wikipedia
        """
        url = "https://fr.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": f"{self.city}",
            "formatversion": "2",
            "format": "json"
        }
        req = requests.get(url, params)
        extracted = json.loads(req.content.decode('UTF-8'))
        title = extracted['query']['search'][0]['title']

        return title

    def wikiextract(self, title):
        """
        Call wikipedia API with title result from wikipage() return
        Function extract the text from the wikipedia page and
        return the first two sentences inside strings (html friendly format).
        """
        i = 0
        x = 0
        y = 0
        temp1 = []
        temp2 = ""
        url = "https://fr.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "prop": "extracts",
            "titles": f"{title}",
            "explaintext": 1,
            "formatversion": "2",
            "format": "json"
        }
        req = requests.get(url, params)
        extracted = json.loads(req.content.decode('UTF-8'))
        #indent = json.dumps(extracted, indent = 4)
        #print(extracted)
        temp = extracted["query"]["pages"][0]["extract"]
        extracted2 = temp.split('=')
        wikitext = extracted2[0]
        for i in wikitext:
            if x != 2:
                if i == ".":
                    x = x + 1
                    temp1.append(i)
                    temp1.append("<br>")
                else:
                    temp1.append(i)              
        wikitext = temp2.join(temp1)

        return wikitext