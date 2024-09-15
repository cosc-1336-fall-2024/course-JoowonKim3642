#main get_options_ratio and get_faculty_rating

import decisions

def main():
    #get option and total
    option = float(input("Enter option: "))
    total = float(input("Enter total: "))

    try:
        result1 = decisions.get_options_ratio(option, total)
        result2 = decisions.get_faculty_rating(result1)

        #added small number to round off, not round to nearest even
        print("Ratio: ", round(result1 + 0.00000001, 2))
        print("Rating: ", result2)
    except ZeroDivisionError: 
        print("Total cannot be 0")
  
main()