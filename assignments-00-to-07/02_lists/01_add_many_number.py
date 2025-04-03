def sum_numbers(numbers):

    return sum(numbers)

print("\033[1;3m '''This program takes list of integers from you and give the sum of all those integers''' \033[0m")
numbers_list = list(map(int, input("Enter numbers separated by space: ").split()))

result = sum_numbers(numbers_list)

def main():
    print("list of numbers: ", numbers_list)
    print("Sum:", result)

if __name__ == '__main__':
    main()