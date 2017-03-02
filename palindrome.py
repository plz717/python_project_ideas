def reverse_string(s):
    print("input string is:", s)
    a = ''
    for i in range(len(s) - 1, -1, -1):
        a = a + s[i]
    return a


s = input("input a string:")
reversed_s = reverse_string(s)
for i in range(0, len(s)):
    if s[i] == reversed_s[i]:
        print("is palindrome")
    elif abs(ord(s[i]) - ord(reversed_s[i])) == 32:
        print("is palindrome")
    else:
        print("is not palindrome")
        break
