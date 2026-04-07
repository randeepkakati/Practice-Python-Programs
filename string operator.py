# string operator
# palindrome check
def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("madam"))


# Count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


print(count_vowels("hello"))
