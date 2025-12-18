# q1 return even numbers
def get_even():
    nums = list(map(int, input("Enter numbers: ").split()))
    even = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
    return even


# q2 return character count
def char_count():
    s = input("Enter a string: ")
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d


# q3 return palindrome result
def is_palindrome():
    n = input("Enter a number: ")
    if n == n[::-1]:
        return True
    else:
        return False


# q4 return average using *args
def average():
    nums = list(map(int, input("Enter numbers: ").split()))
    total = 0
    for i in nums:
        total += i
    return total / len(nums)


# q5 return common elements
def common_elements():
    l1 = list(map(int, input("Enter first list: ").split()))
    l2 = list(map(int, input("Enter second list: ").split()))
    common = []

    for i in l1:
        if i in l2 and i not in common:
            common.append(i)

    return common


# Calling Functions
print("Even numbers are:", get_even())
print()

print("Character count is:", char_count())
print()

res = is_palindrome()
if res:
    print("Palindrome is True")
else:
    print("Palindrome is False")
print()

print("Average is:", average())
print()

print("Common elements are:", common_elements())