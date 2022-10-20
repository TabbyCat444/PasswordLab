# Finish reading another word and an integer into variables.
# Output all the values on a single line
favorite_color = str(input("Please enter a color: "))
favorite_flower = str(input("Please enter a flower: "))
favorite_number = str(input("Please enter a number: "))

print('You entered: ' + favorite_color + ' ' + favorite_flower + ' ' + favorite_number)


# Output two password options
password1 = favorite_color + '_' + favorite_flower
password2 = favorite_number + favorite_color + favorite_number
print('\nFirst password: ' + password1)
print('Second password: ' + password2)


# Output the length of the two password options
print('\nNumber of characters in', password1 + ':', len(password1))
print('Number of characters in', password2 + ':', len(password2))
