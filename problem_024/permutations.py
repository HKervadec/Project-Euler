from time import time

def gen_permutations(l):
    if len(l) == 1:
        yield l

    for i in range(len(l)):
        ll = l[:]
        del ll[i]

        for sp in gen_permutations(ll):
            yield [l[i]] + sp

def gen_permutations_2(l):
    if len(l) == 1:
        yield l

    for i in range(len(l)):
        ll = l[:i] + l[i+1:]

        for sp in gen_permutations(ll):
            yield [l[i]] + sp


def heap_gen(n, A):
    if n == 1:
        yield(A)
    else:
        for i in range(1, n+1):
            heap_gen(n - 1, A)

            j = i
            if n % 2:
                j = 1

            A[j], A[n] = A[n], A[j]


def evaluate_func(f):
    i = 0

    start_time = time()
    for perm in f(list("0123456789")):
        i += 1

        if i == 1000000:
            print(''.join(perm))
            break

    print(time() - start_time)


if __name__ == "__main__":
    # test = [1,2,3]
    #
    # gen = gen_permutations(test)
    #
    # for perm in gen:
    #     print(perm)

    evaluate_func(gen_permutations)
    evaluate_func(gen_permutations_2)

