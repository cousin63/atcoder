import itertools


def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def solve2(left,right):
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        #print(perm)
        sol = dict(zip(letters, perm))
        if ((left[0][0], 0) not in sol.items())==True and ((left[1][0], 0) not in sol.items())==True and ((right[0], 0) not in sol.items())==True:
            if sum(get_value(word, sol) for word in left) == get_value(right, sol):
                print(*list(str(get_value(word, sol)) for word in left))
                print(get_value(right, sol))


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    s3 = input()
    solve2([s1,s2],s3)