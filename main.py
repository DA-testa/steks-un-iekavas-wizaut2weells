# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
                        opening_brackets_stack.append(Bracket(next,i+1))
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
    if opening_brackets_stack:
        return opening_brackets_stack[-1].position
        opening_brackets_stack.pop()
    return "Success"

def main():
    is_file = input("File(F) or Input(I)")
    if is_file == 'I':
        text = input()
        mismatch = find_mismatch(text)
    # Printing answer, write your code here
        print(mismatch)
    else:
        pass
if __name__ == "__main__":
    main()
