import math


def poisson_distribution(u, max_of_k):
    p = []
    for k in range(1, max_of_k + 1):
        temp_p = pow(u, k) / math.factorial(k) * pow(math.e, 0 - u)
        p.append(temp_p)
    return p


if __name__ == '__main__':
    p = poisson_distribution(15, 12)
    sum = 0
    for item in p:
        sum += item
    print(sum)


