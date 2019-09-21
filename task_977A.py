n, k = input().split()

def f(n, k):
    n = [int(i) for i in list(str(n))]
    while k != 0:
        if n[-1] == 0:
            n.pop()
            k -= 1
        else:
            n[-1] = n[-1] - 1
            k -= 1
    return ''.join([str(i) for i in n])

print(f(n, int(k)))

assert f(512, 4) == '50'
assert f(1000000000, 9) == '1'

