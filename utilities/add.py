def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == reverse_string(s)

# Example usage
input_string = "racecar"
reversed_string = reverse_string(input_string)
print(f"Reversed String: {reversed_string}")

if is_palindrome(input_string):
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string '{input_string}' is not a palindrome.")
