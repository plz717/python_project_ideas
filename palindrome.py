def reverse_string(s):
    print("input string is:", s)
    a = ''
    for i in range(len(s) - 1, -1, -1):
        a = a + s[i]
    return a


def is_palindrome(s):

    reversed_s = reverse_string(s)
    for i in range(0, len(s)):
        if s[i] == reversed_s[i] or abs(ord(s[i]) - ord(reversed_s[i])) == 32:
            print("is palindrome")
            return 1
        else:
            print("is not palindrome")
            return 0
            break
        
if __name__=='__main__':
    s = input("input a string:")
    is_palindrome=is_palindrome(s)
    print(is_palindrome)
