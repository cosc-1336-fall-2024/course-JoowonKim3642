#main

import strings

def main():
    option = 0

    try:

        while True:

            print("----MENU----\n1-Hamming Distance\n2-Dna Complement\n3-Exit")
            option = int(input("PLEASE ENTER YOUR SELECTION: "))
        
            if option == 1:
                dna1 = input("please enter DNA#1: ")
                dna2 = input("please enter DNA#2: ")
                result1 = strings.get_hamming_distance(dna1, dna2)
                print("result: ", result1)

            elif option == 2:
                dna = input("please enter DNA: ")
                result2 = strings.get_dna_complement(dna)
                print("result: ", result2)

            elif option == 3:
                print("Exit")
                break

            else:
                print("Invalid option")
    except ValueError:
        print("Invalid value")

main()