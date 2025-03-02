from operators import *

def main():

    operators_list = [addition, subtraction, multiply, division, exponention, root]
    calculation = True

 
    while calculation == True:
        print_menu()
        try:
            chosen_operator = operators_list[(int(input("Choose your operator: "))-1)]
            if 'result' in locals():
                first_integer = result
            else:
                first_integer = float(input("Enter the first integer: "))

            second_integer = float(input("Enter the second integer: "))
            result = chosen_operator(first_integer, second_integer)
            calculation_input = input(f"\nThe result is: {result}.\nDo you want to continue (y/n)?")

            if calculation_input == "n":
                calculation = False

        except (IndexError, NameError, ValueError, ZeroDivisionError):
            print("Please enter a valid value")

if __name__ == "__main__":
    main()

