from languageIdentifier import languageIdentifier
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

        word = words[0]
        if word == "quit":
            break
        if word == "langId":
            if words[1] == "-s":
                userInput = " ".join(userInput.split()[2:])
                languageIdentifier(userInput)
                continue
            

        print("Unknown Command:", userInput)
main()