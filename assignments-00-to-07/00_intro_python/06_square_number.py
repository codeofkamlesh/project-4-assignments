def main():
    print("This program calculate the square of a number")

    num = float(input("\033[1;3m Type a number to see its square: \033[0m"))

    square : float = num**2

    print(f"Square of {num} is =  {square}")

if __name__ == '__main__':
    main()