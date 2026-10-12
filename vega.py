from languageIdentifier import languageIdentifier
from spamDetection import spamDetection
def main():
    userInput = ""

    print("Welcome to VEGA")
    print("Version: 0.0.0\n")
    print("VEGA serves as a place for me to learn about machine learning and Nueral Networks. The VEGA project will grow in proportion to my knowledge")
    print("Type -help for a list of commands\n")

    while(userInput != "quit"):
        userInput = input("\nVEGA > ")

        words = userInput.split()

        # for word in words:
        #     print(word)

        if words[0] == "quit":
            break
        if words[0] == "-help":
            print("\nlangId [-str] [target string]")
            print("     -> finds probability of language of string\n")
            print("genLang [-l] [-s] [starting string]")
            print("     -> generates string of -l length")
            print("     -> -s is optional")


            continue
        if words[0] == "langId":
            if words[1] == "-s":
                userInput = " ".join(userInput.split()[2:])
                languageIdentifier(userInput)
                continue
        if words[0] == "genLang":
            if words[1] == "-l":
                length = words[2]
                if words[3] == "-s":
                    return
        if words[0] == "isSpam":
            userInput = " ".join(userInput.split()[1:])
            spamDetection(userInput)
            continue


            

        print("Unknown Command:", userInput)
main()