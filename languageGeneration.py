import random
import os

def normalizeText(text):
    text = text.lower()
    text = " ".join(text.split())
    return text

def getNgrams(word: str, num: int):
    ngrams = []

    if len(word) < num:
        ngrams.append(word)
        return ngrams

    i = 0
    while(i + num <= len(word)):
        ngrams.append(word[i:i+num])
        i = i + 1
    
    return ngrams

def populateDict(ngrams: list, dictonary: dict) -> dict:
    english = dictonary

    for ngram in ngrams:
        if ngram not in english:
            english[ngram] = 1
        else:
            english[ngram] = english[ngram] + 1

    return english

def findChar(canidates: dict) -> str:
    randomKey = random.choice(list(canidates.keys()))
    return randomKey



def generateLanguage():
    with open('shakespeare.txt', 'r', encoding='utf-8') as file:
        englishTxt = normalizeText(file.read())
        # print(englishTxt)

    englishNgrams = getNgrams(englishTxt, 6)

    english = {}
    english = populateDict(englishNgrams, english)

    phrase = "to be or "
    bigram = phrase[-5:]
    #print(bigram)
    length = 500

    i = len(phrase)
    while(i < length):
        canidates = {}
        for key, value in english.items():
            if key.startswith(bigram):
                canidates[key[-1]] = value

        os.system("clear")
        print(phrase)
        phrase = phrase + findChar(canidates)

        bigram = phrase[-5:]
        i = i + 1





    # print(english)

    # print("hello world")

generateLanguage()