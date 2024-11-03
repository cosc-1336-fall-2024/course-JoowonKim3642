#main

from lists import get_lowest_list_value, get_highest_list_value

def main():
    while True:
        print("MENU\n1-Show the list low /high values\n2-Exit")

        option = input("Select 1 or 2: ")

        if option == "1":
            numbers = []
            while True:  
                num = int(input("please enter a integer value: "))
                numbers.append(num)

                if len(numbers) > 2:
                    answer = input("Do you want to enter another value? y/n ").upper()
                    if answer == "Y":
                        continue
                    elif answer == "N":
                        break

            lowest = get_lowest_list_value(numbers)
            highest = get_highest_list_value(numbers)
            
            print(f"The lowest number in the list is: {lowest}")
            print(f"The highest number in the list is: {highest}")

        elif option == "2":
            print("Exit")
            break

        else:
            print("Invalid option")

main()
