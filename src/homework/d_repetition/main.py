#main

from repetition import get_factorial, sum_odd_numbers

def main():
    while True:
        print("Homework 3 Menu")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")

        option = input("Select 1, 2, or 3: ")

        if option == "1":
            num = int(input("Enter a number (0 < num < 10): "))
            while num <= 0 or num >= 10:
                print("Invalid input")
                num = int(input("Enter a number (0 < num < 10): "))
            result = get_factorial(num)
            print(f"The factorial of {num} is {result}.")

        elif option == "2":
            num = int(input("Enter a number (0 < num < 100): "))
            while num <= 0 or num >= 100:
                print("Invalid input")
                num = int(input("Enter a number (0 < num < 100): "))
            result = sum_odd_numbers(num)
            print(f"The sum of odd numbers up to {num} is {result}")

        elif option == "3":
            print("Exit")

        else:
            print("Invalid option")

        exit_choice = input("Do you want to exit? (Y/N): ").lower()
        if exit_choice == 'y':
            print("Exiting the program.")
            break
main()