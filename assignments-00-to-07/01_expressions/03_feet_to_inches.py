def main():
    print("This program converts feet into inches")

    feet = float(input("\033[1;3m Enter the value of feet: \033[0m"))

    inches = feet * 12

    print(f"{feet} feet = {inches} inches ")

if __name__ == '__main__':
    main()
