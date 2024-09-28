from collections import deque


def is_palindrome(input_string):
    cleaned_string = ''.join(input_string.split()).lower()

    char_queue = deque(cleaned_string)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True


def main():
    print(is_palindrome("A man a plan a canal Panama"))  # True
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("Hello World"))  # False
    print(is_palindrome("Able was I ere I saw Elba"))  # True
    print(is_palindrome("А роза упала на лапу Азора"))  # True


if __name__ == "__main__":
    main()