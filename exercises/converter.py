# this program converts from fahreneheit to celsius
# the formula is celsius = fahrenheit - 32 * 5 / 9

# get the user input in F
f = int(input("Enter the temperature in Fahrenehit "))
# do the conversion
c = round((f - 32) * 5 / 9, 3)
# display output
print(f, 'to celsius =',  c)