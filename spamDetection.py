def normalizeText(text):
    text = text.lower()
    text = " ".join(text.split())

    text = text.split()
    return text

def spamDetection(msg: str):
    with open('trainingData/spam.txt', 'r', encoding='utf-8') as file:
        spamTxt = normalizeText(file.read())
        # print(spamTxt)
    with open('trainingData/normal.txt', 'r', encoding='utf-8') as file:
        normalTxt = normalizeText(file.read())
        # print(normalTxt)


    # POPULATE DICTONARIES ------------------
    spamDict = {}
    normalDict = {}

    spamCount = 0
    normalCount = 0

    for word in spamTxt:
        if word not in spamDict:
            spamDict[word] = 1
            spamCount = spamCount + 1
        else:
            spamDict[word] += 1
            spamCount = spamCount + 1

    for word in normalTxt:
        if word not in normalDict:
            normalDict[word] = 1
            normalCount = normalCount + 1
        else:
            normalDict[word] += 1
            normalCount = normalCount + 1

    # msg = "Free money! click me!"
    msg = msg.split()

    pSpam = spamCount / (spamCount + normalCount)
    pNormal = normalCount / (spamCount + normalCount)

    # CALCULATING P(MSG|SPAM) AND P(MSG|NORMAL)------------------------
    pMsgSpam = 1
    pMsgNormal = 1

    vocabSize = len(set(spamDict) | set(normalDict))

    for word in msg:

        pMsgSpam = pMsgSpam * ((spamDict.get(word, 0) + 1) / (spamCount + vocabSize))

        pMsgNormal = pMsgNormal * ((normalDict.get(word, 0) + 1) / (normalCount + vocabSize))


    # CALCULATING P(MSG)
    pMsg = pMsgSpam * pSpam + pMsgNormal * pNormal

    # PROB THAT MSG IS SPAM CALC
    pSpamMsg = (pMsgSpam * pSpam) / pMsg



    print("Probability of Spam", str(int(pSpamMsg * 100)) + "%")

# spamDetection()