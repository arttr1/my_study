def ArmstrongNumber(number):
    string_num = str(number)
    n = len(string_num)

    result = lambda digits: sum(int(digit)**n for digit in digits)
    
    sum_of_powers = result(string_num)
    return sum_of_powers == number

print(ArmstrongNumber(1634))