def main():
    mass_in_kg = float(input("\033[1;3m Enter kilos of mass: \033[0m"))
    C = 299792458
    print("e = m * C^2")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")

    e = mass_in_kg*(C**2)
    print(f"{e} joules of energy")

if __name__ == '__main__':
    main()