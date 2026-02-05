def to_roman(num):
    # turn number into a list
    num_lst = [int(digit) for digit in str(num)]
    num_lst.reverse()

    # turn list into place values
    def place_finder(num_lst):
        place_values = []
        multiplier = 1

        for i in num_lst:
            n = i * multiplier
            place_values.append(n)
            multiplier *= 10
            
        return place_values

    place_lst = place_finder(num_lst)
    place_lst.reverse()
    
    # Create dictionary of number roman numeral pairs
    numeral_dict = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40:"XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",   
    }

    roman_numeral_lst = []
    for item in place_lst:
        if item <= 3:
            roman_numeral_lst.append(numeral_dict.get(1) * item)

        elif item == 4:
            roman_numeral_lst.append(numeral_dict.get(4))
        
        elif item == 5:
            roman_numeral_lst.append(numeral_dict.get(5))

        elif item == 9:
            roman_numeral_lst.append(numeral_dict.get(9))

        elif item >= 10 and item < 40:
            multplier = item // 10
            roman_numeral_lst.append(numeral_dict.get(10) * multplier)

        elif item == 40:
            roman_numeral_lst.append(numeral_dict.get(40))

        elif item == 50:
            roman_numeral_lst.append(numeral_dict.get(50))

        elif item == 90:
            roman_numeral_lst.append(numeral_dict.get(90))

        elif item >= 100 and item < 400:
            multplier = item // 100
            roman_numeral_lst.append(numeral_dict.get(100) * multplier)

        elif item == 400:
            roman_numeral_lst.append(numeral_dict.get(400))

        elif item == 500:
            roman_numeral_lst.append(numeral_dict.get(500))

        elif item == 900:
            roman_numeral_lst.append(numeral_dict.get(900))

        elif item >= 1000:
            multplier = item // 1000
            roman_numeral_lst.append(numeral_dict.get(1000) * multplier)

    roman_numerals = "".join(roman_numeral_lst)

    
    return roman_numerals
    
   #return ""

print(to_roman(3922))
print(to_roman(2754))
print(to_roman(944))
