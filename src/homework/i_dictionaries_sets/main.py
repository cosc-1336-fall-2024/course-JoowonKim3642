#main

from dictionary import get_p_distance_matrix

def get_total_list():
    num = int(input("how many list will enter? "))
    index = 0
    total_list = []

    while(index < num):
        input_list = input("please enter a comma-separated list: ")
        s_list = input_list.split(",")
        s_list = [value.strip() for value in s_list]
        total_list.append(s_list)
        index += 1

    return total_list


def main():
    while True:
        print("MENU\n1-Get p distance matrix\n2-Exit")

        option = input("Select 1 or 2: ")
        result = []

        if option == "1":
            result0 = get_total_list()
            result = get_p_distance_matrix(result0)
            for row in result:
                print(" ".join(f"{dist:.3f}" for dist in row))

        elif option == "2":
            print("Exit")
            break

        else:
            print("Invalid option")

main()