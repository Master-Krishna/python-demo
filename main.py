def longest_incresing(L):
    max = 0
    inc = []
    for x in L:
        if x > max:
            max = x
            inc += [x]

    return len(inc),inc

print(longest_incresing(L = [3, 10, 2, 1, 20]))
