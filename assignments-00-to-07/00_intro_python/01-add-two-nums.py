
def main():
    print("This program is for addition of two numbers.")
    num1 : str = input("Enter first number: ")
    num1 : int = int(num1)
    num2  : str = input("Enter second number: ")
    num2 : int = int(num2)
    total : int = num1 + num2
    print(f"Sum of {num1} and {num2} is = {total} .")

if __name__ == '__main__':
    main()