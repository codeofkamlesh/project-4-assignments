def main():
    print("\033[1m This program is used to Devide two numbers and get the result with remainder \033[0m")

    first_num = int(input("\033[1;3m Please enter an integer to be divided: \033[0m"))

    second_num = int(input("\033[1;3m Please enter an integer to divide by: \033[0m"))

    Result = first_num//second_num

    Remainder = first_num % second_num

    print(f"The result of this division is {Result} with a remainder of {Remainder}")

if __name__ == '__main__':
    main()