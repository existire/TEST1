"""
Decimal list
Lukasz Szulc
lukasz.szulc@op.pl

The function gets 3 variables:
x = start number in float format
y = end number in float format
z = the interval in float format
and output the list in decimal format with a declared interval.
"""


from decimal import Decimal, ROUND_HALF_UP


def decimal_list(x, y, z):
    d_list = []
    a = (Decimal(Decimal(x).quantize(Decimal('.1'), rounding=ROUND_HALF_UP)))
    b = (Decimal(Decimal(y).quantize(Decimal('.1'), rounding=ROUND_HALF_UP)))
    c = (Decimal(Decimal(z).quantize(Decimal('.1'), rounding=ROUND_HALF_UP)))
    if (b > a) and (a % c == 0) and (b % c == 0):
        multiply = int((b - a) / c + 1)
        for i in range(multiply):
            d_list.append(a)
            a = a + c
        print(d_list)
    else:
        print("Input the proper variables into function, please.")


decimal_list(2.0, 5.5, 0.5)