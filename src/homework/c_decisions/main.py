#main get_options_ratio and get_faculty_rating

import decisions

def main():

    option = int(input("Enter option: "))
    total = int(input("Enter total: "))

    result1 = decisions.get_options_ratio(option, total)
    result2 = decisions.get_faculty_rating(result1)
    print("Rating: ", result2)
  
main()

#solving errors ver
    #try:
        #result1 = decisions.get_options_ratio(option, total)
        #result2 = decisions.get_faculty_rating(result1)
        #print("Rating: ", result2)
    #except ZeroDivisionError:
        #print("Total cannot be 0")
#need to solve
#if ratio is over or equals 1, result of get_faculty_rating is very good