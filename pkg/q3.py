print(6 + 8 / 2 - 1)
# divides 8 by 2 first and then minus the one at the end

print(1 + 1 - 1 + 2 / 2)
# again the divide comes first

print(1.1 + 5/2)
# same again

print(9.2/3)
# gives a long floating point unless you specify

print(9.2 % 3)
print("{0:.2f}".format(9.2%3))

print(1 * 2 + 3 * 5 % 4)
# floor divide happens first then multiplication then the addition

print(1 + 8 % 3 * 2 - 9)
# floor divide = 2 then * 3 minus 9 and plus 1

print(6 + (24 % (16-11)))
