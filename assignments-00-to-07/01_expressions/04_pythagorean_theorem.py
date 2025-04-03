import math
def main():
    print("\033[1m This program is used to solve the pythagoras theorem Hypotenuse^2 = Base^2 + Perpendicular^2 \033[0m")

    Base = float(input("\033[1;3m Enter the length of Base: \033[0m"))

    Perpendicular = float(input("\033[1;3m Enter the length of Perpendicular: \033[0m"))

    Hypotenuse = math.sqrt((Base**2 + Perpendicular**2))

    print(f"The length of Hypotenuse = {Hypotenuse}")
if __name__ == '__main__':
    main()