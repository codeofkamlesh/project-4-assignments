def main():

    print("\033[1m '''Let's have some fun''' \033[0m")

    Sentence_start = "This is just a funny sentence. 'The programming is like"

    Adjective = (input("\033[1;3m Please type an adjective and press enter:  \033[0m"))

    Noun = (input("\033[1;3m Please type a noun and press enter:  \033[0m"))

    Verb = (input("\033[1;3m Please type a verb and press enter:  \033[0m"))

    print(f"{Sentence_start} {Adjective} {Noun} {Verb}'. ")

if __name__ == '__main__':
    main()
