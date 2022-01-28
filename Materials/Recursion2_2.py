input = input()


def is_palindrome(string):
    if string[::-1] == string:
        return True
    elif string[::-1] != string:
        return False


print(is_palindrome(input))