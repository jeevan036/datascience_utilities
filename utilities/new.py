print("Updated")
def is_perfect_square(n):
    if n < 0:
        return False
    
    root = int(n ** 0.5)
    
    return root * root == n

test_numbers = [0, 1, 4, 9, 16, 25, 36, 49, 5, 100, -4]

for num in test_numbers:
    if is_perfect_square(num):
        print(f"{num} is a perfect square")
    else:
        print(f"{num} is not a perfect square")
