print("checking palindrome")

word = "mom"
if word == word[::-1]:  # Check if the word is equal to its reverse
    print("Palindrome")
else:
    print("Not a palindrome")