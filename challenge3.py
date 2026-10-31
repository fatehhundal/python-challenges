mean1 = 38
wrong_num = 36
correct_num = 56
total = 40
print("The original mean is", mean1)
sum1 = mean1 * total
print("The original sum of the 40 numbers is", sum1)

sum2 = sum1 - (wrong_num - correct_num)
print("The new sum is", sum2)

mean2 = sum2 / total
print("The new mean is", mean2)