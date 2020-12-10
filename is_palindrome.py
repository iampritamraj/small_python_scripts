text =input("Enter text or phrase to check palindrome:")
is_palindrome = lambda phrase: phrase == phrase[::-1] #one line logic to palindrome
print(is_palindrome(text))