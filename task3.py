def check_brackets(expression):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return "Несиметрично"

    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"


test_cases = [
    "( ){[ ]( ) ( ) { } }",
    "( 23 ( 2 - 3);",
    "( 11 }"
]


def main():
    for test_case in test_cases:
        print(check_brackets(test_case))


if __name__ == "__main__":
    main()
