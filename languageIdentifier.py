import csv
import math

def getNgrams(word: str):
    ngrams = []

    if len(word) < 3:
        ngrams.append(word)
        return ngrams

    i = 0
    while(i + 3 <= len(word)):
        ngrams.append(word[i:i+3])
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



def languageIdentifier(phrase: str):
    with open('english.txt', 'r', encoding='utf-8') as file:
        englishTxt = file.read()
        # print(englishTxt)

    with open('spanish.txt', 'r', encoding='utf-8') as file:
        spanishTxt = file.read()
        # print(spanishTxt)

    with open('french.txt', 'r', encoding='utf-8') as file:
        frenchTxt = file.read()
        # print(frenchTxt)

    # with open('english.csv', mode='r', newline='') as file:
    #     reader = csv.DictReader(file)
    #     english = {row['ngram']: int(row['count']) for row in reader}

    # print(english)
    englishNgrams = getNgrams(englishTxt)
    spanishNgrams = getNgrams(spanishTxt)
    frenchNgrams = getNgrams(frenchTxt)

    english = {}
    spanish = {}
    french = {}

    english = populateDict(englishNgrams, english)
    spanish = populateDict(spanishNgrams, spanish)
    french = populateDict(frenchNgrams, french)

    englishTotal = 0
    spanishTotal = 0
    frenchTotal = 0

    for value in english.values():
        englishTotal = englishTotal + value

    for value in spanish.values():
        spanishTotal = spanishTotal + value

    for value in french.values():
        frenchTotal = frenchTotal + value

    ngrams = getNgrams(phrase)

    englishScore = 0
    spanishScore = 0
    frenchScore = 0

    for ngram in ngrams:
        count = english.get(ngram, 0)
        probability = (count + 1) / (englishTotal + len(english))
        englishScore += math.log(probability)

    for ngram in ngrams:
        count = spanish.get(ngram, 0)
        probability = (count + 1) / (spanishTotal + len(spanish))
        spanishScore += math.log(probability)

    for ngram in ngrams:
        count = french.get(ngram, 0)
        probability = (count + 1) / (frenchTotal + len(french))
        frenchScore += math.log(probability)
        max_score = max(englishScore, spanishScore, frenchScore)

    english_exp = math.exp(englishScore - max_score)
    spanish_exp = math.exp(spanishScore - max_score)
    french_exp = math.exp(frenchScore - max_score)


    total = english_exp + spanish_exp + french_exp

    english_probability = int(english_exp / total * 100)
    spanish_probability = int(spanish_exp / total * 100)
    french_probability = int(french_exp / total * 100)

    print(f"English: {english_probability}%")
    print(f"Spanish: {spanish_probability}%")
    print(f"French: {french_probability}%")

    # for key, value in english.items():
    #     print(f"{key}: {value}")


    # with open('english.csv', mode='w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['ngram', 'count'])
    #     writer.writerows(english.items())

# languageIdentifier()
