import json
import sys

class Parser:
    """
    """
    def __init__(self, split_words):
        self.split_words = split_words

    def parser(self):
        """
        Put a JSON stopwords list into an exploitable python list
        """
        path = "ressources/fr-split/fr.json"
        with open(path, encoding='utf-8') as french:
            words = json.load(french) #JSON to list

        return words

    def compare(self, words):
        """
        Compare every stop words with list of words and attribute
        them a value, mix of both create a dictionnary
        """
        i = 0
        ponct = ["!", ".", "?"]
        li = []
        values = []
        dictionary = {}
        x = (len(self.split_words))
        y = 0
        if x == 2 or x == 1:
                values.append(self.split_words[i])
        if self.split_words[0][0].isupper:
                li.append(0)
        while i != len(self.split_words):
            temp = words.count(f"{(self.split_words[i])}") #count stop words
            temp2 = ponct.count(f"{(self.split_words[i])}") #count ponctuation char
            if i != 0 and self.split_words[i][0].isupper(): #City/Place
                values.append(self.split_words[i])
                li.append(3)
            elif temp >= 1: #Stop words
                li.append(1)
            elif temp2 == 1: #Ponctuation
                li.append(2)
            elif temp == 0 and i != 0: #Ignored
                li.append(0)
            i = i + 1
        dictionary = dict(zip(self.split_words, li))
        z = len(values) - 1 #number of last word
        for i in values[z]:
            if i == "." or i =="!" or i =="?":
                values[z] = values[z][:-1] #remove last character
        city = ' '.join([str(elem) for elem in values])
        print(city)

        return dictionary, city