# roman to arabic
x = str(input("input a roman number :"))
# for dictionary use {}
convert_to_arabic = {"I":1, "V":5, "X":10}
result = 0
for i in range(len(x)):
    if(i > 0 and convert_to_arabic[x[i]] > convert_to_arabic[x[i-1]]):
        result += convert_to_arabic[x[i]] - 2 * convert_to_arabic[x[i-1]]
    else:
        result += convert_to_arabic[x[i]]
print(result)

# arabic to roman
def roman_to_arabic(y):
    roman = {"I":1, "V":5, "X":10}
    previous = 0
    current = 0
    total = 0
    for i in range(len(y)):
        current = roman[y[i]]
        if(current > previous):
            total = total + current - 2 * previous
        else:
            total += current
        previous = current
    return total
y = str(input("input an arabic number :"))
print(roman_to_arabic(y))



