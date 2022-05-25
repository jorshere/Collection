def is_palindrome(temp):
    if temp == temp[::-1]:
        print(f"Your string '{temp}' is palindrome ")
    else:
        print(f"Your string '{temp}' is not palindrome")

entry= input("enter a string to check whether its palindrome or not : ")
is_palindrome(entry)
