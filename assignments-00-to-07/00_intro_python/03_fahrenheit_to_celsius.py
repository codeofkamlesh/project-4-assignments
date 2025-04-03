def main():
    print("This program converts Temperature of Fahrenheit into celsius")

    fahrenheit_temp = float(input("\033[1;3m Enter temperature in Fahrenheit: \033[0m"))

    degrees_celsius = (fahrenheit_temp - 32) * 5.0/9.0

    print(f"Temperature: {fahrenheit_temp}F = {degrees_celsius}C")

if __name__ == '__main__':
    main()
