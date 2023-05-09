# creating a function to check
# Palindrome number;
# A number which remain same even after reversing it...
def chkPalindrome(n):

    # to store the reversed number
    revN=''          
    
    # class reversed to take reverse for the number                  
    for i in reversed(str(n)):
        # storing by each digit in reverse order
        revN += i
    # checking for number equal to reverse or not
    if str(n)==revN:
        print("Palindrome Number")
        return True
    print("not a Palindrome Number")
    return False

print("Answer in boolean: ",chkPalindrome(int(input("Enter Number(for, Palindrome condition): "))))