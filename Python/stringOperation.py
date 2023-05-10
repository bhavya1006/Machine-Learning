# String Operations:
string = 'Hello World'
string1 = 'this is another example for string'
space = ' '
spaces_string = '-------Hello-------'



# .lower() ==> converts each charater to lowercase
print("\nString in lower case: ",string.lower())

# .upper() ==> converts each charater to uppercase
print("\nString in upper case: ",string.upper())

# .title() ==> converts the first word in string to capital else small
print("\nString in title case: ",string1.title())

# .capitalize() ==> converts the first world capital else all small
print("\nString in capitalize case: ",string.capitalize())


# .islower() ==> boolean checks for all lower case
print("\nChecking String in lower case: ",string1.islower())

# .isupper() ==> boolean checks for all upper case
print("\nChecking String in upper case: ",string.isupper())

# .isspace() ==> boolean checks for only space
print("\nChecking String for only space: ",space.isspace())


# .split() ==> returns the list of string, element identify as space to next character
print("\nSplitting String: ",string1.split())

# .split(argu) ==> returns the list of string on the basis of splitting by argument given
print("\nSplitting String: ",string1.split('e'))

# .lstrip() ==> removes extra space from left
print("\n Taking '-' as whitespace and giving in argument for checking it works")
print("\nRemoved spaces from left of String:",spaces_string.lstrip('-'))

# .rstrip() ==> removes extra space from right
print("\nRemoved spaces from right of String:",spaces_string.rstrip('-'))

# .strip() ==> removes extra space from both left and right
print("\nRemoved spaces from both side of String:",spaces_string.strip('-'))

# .replace('substring to be replaced','substring which will replace')
print("\nReplacing 'World' by 'User!!'")
print("String as follows: ",string.replace('World','User!!'))