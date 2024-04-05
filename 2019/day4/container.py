def get_first_digit(input):
    while input > 10:
        input = input / 10
    return int(input)

def get_digits(input):
    digits = []
    while input :
        n = input % 10
        digits.append(n)
        input = int(input/10)
    digits.reverse()
    return digits

def increasing_digits(digits):
    index = 0
    for d in digits:
        #print(index, d, digits[index+1])
        if index+1 < len(digits) and d > digits[index+1]:
            return False
        index += 1
    return True

def adjacent_equal_digits(digits):
    i = 0
    g = []
    while i < len(digits):
        n = 1
        while i+1 < len(digits) and digits[i+1] == digits[i]:
            n += 1
            i += 1
        if n != 0:
            g.append(n)
        #print(i, d)
        """
        if i+1 < len(digits) and d == digits[i+1]:
            if i+2 < len(digits) and d == digits[i+2]:
                print(digits)
                return False
            return True
        """
        i += 1
    #print(digits)
    print(g)
    if 2 in g:
        return True
    else:
        return False

def respects_criteria(input):
    digits = get_digits(input)
    return increasing_digits(digits) and adjacent_equal_digits(digits)
        

#print(get_digits(123456789))
print(respects_criteria(112233))
print(respects_criteria(123444))
print(respects_criteria(111122))


nb = 0
for pws in range(240920, 789857):
    if respects_criteria(pws):
        #        print(pws)
        nb += 1
    else:
        pass
        #print(pws)

print(nb)

