from basic_calculations import *
from templates import *
from input_and_output import *



def main():
    greatings()
    print()
    while True:
        topics()
        choise = input_()
        if choise == '1':
            while True:
                basic_calculation()
                choise = input_()
                if choise == '1':
                    number = numbers()
                    result = add(number[0], number[1])
                    score(result)
                 
                if choise == '2':
                    number = numbers()
                    result = subtract(number[0], number[1])
                    score(result)

                if choise == '3':
                    number = numbers()
                    result = multiplication(number[0], number[1])
                    score(result)
                    
                if choise == '4':
                    number = numbers()
                    result = division(number[0], number[1])
                    score(result)
                    
                if choise == '5':
                    number = numbers()
                    result = exponentiation(number[0], number[1])
                    score(result)
                    
                if choise == '6':
                    number = numbers()
                    result = modulo(number[0], number[1])
                    score(result)
                    
                if choise == '7':
                    number = numbers()
                    result = excellence(number[0], number[1])
                    score(result)
                    
                if choise == '8':
                    number = numbers()
                    result = element(number[0], number[1])
                    score(result)
                    
                if choise == '9':
                    choise = '0'
                    break
        if choise == '2':
            bmi_calculator()

        if choise == '3':
            pass
        if choise == '4':
            pass
        if choise == '5':
            pass
        if choise == '6':
            pass
        if choise == '7':
            pass
        if choise == '8':
            pass
        if choise == '9':
            exit()
            break




if __name__ == '__main__':
    main()
