print("Enter a number (numerator): ")
numnume = int(input())
print("Enter a number (denominator): ")
numdeno = int(input())

if numnume % numdeno == 0:
    print("\n" + str(numnume) + " is divisible by " + str(numdeno))
else:
    print("\n" + str(numnume) + " is not divisible by " + str(numdeno))