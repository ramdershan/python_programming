# bill = 175.00

# tax = 15

# total_tax = (bill * tax)/ 100.00

# print('total tax', total_tax)

def calc_tax(bill, tax):
    return round(((bill*tax) / 100.00), 2)

print(calc_tax(175.00, 25))
print(calc_tax(164, 23))