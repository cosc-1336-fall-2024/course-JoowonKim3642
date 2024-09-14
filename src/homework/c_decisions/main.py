#main get_options_ratio and get_faculty_rating

import decisions

def main():

    option = int(input("Enter option: "))
    total = int(input("Enter total: "))

    try:
        result1 = decisions.get_options_ratio(option, total)
        result2 = decisions.get_faculty_rating(result1)
        print("Ratio: ", result1)
        print("Rating: ", result2)
    except ZeroDivisionError:
        print("Total cannot be 0")
  
main()