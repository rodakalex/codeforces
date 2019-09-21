ignore = input()
args = list(map(int, input().split()))

def addition(*args):
    temp = 0
    for arg in args:
        temp += arg
    return "HARD" if temp else "EASY"

print(addition(*args))

assert addition(0, 0, 1) == "HARD"
assert addition(0) == "EASY"
