def main():
    print("\033[1m '''This program shows seconds in a year''' \033[0m")

    days_in_year = 365
    hours_in_a_day = 24
    minutes_in_an_hour = 60
    seconds_in_a_minute = 60

    print(f"The seconds in a year = {days_in_year * hours_in_a_day *minutes_in_an_hour * seconds_in_a_minute} seconds")

if __name__ == '__main__':
    main()