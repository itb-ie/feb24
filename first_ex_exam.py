def sum_div(a, b):
    # validate the numbers:
    try:
        a = int(a)
        b = int(b)
    except:
        print("At least one of the parameters was not a number!!")
        return
    if (a <= 0) or (b <= 0):
        print("At least one of the numbers is not positive")
        return
    # validation is now done!
    prod = a * b
    sum_div = 1 + prod
    for i in range(2, prod//2 +1):
        if prod % i == 0:
            sum_div += i
    return sum_div

print(sum_div(3,7))
print(sum_div(-2, 2))
