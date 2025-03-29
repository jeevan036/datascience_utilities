print("Updated")
def is_perfect_square(n):
    if n < 0:
        return False
    
    root = int(n ** 0.5)
    
    return root * root == n


for num in test_numbers:
    if is_perfect_square(num):
        print(f"{num} is a perfect square")
    else:
        print(f"{num} is not a perfect square")
