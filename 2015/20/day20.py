import math

input = 29000000

def factors(n):
    factors = []
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n // i == n / i:
            if i not in factors: factors.append(i)
            if n // i not in factors: factors.append(n//i)
    return factors

def sum(n):
    sum = 0
    for i in n:
        sum += i
    return sum

house_presents = []

while len(house_presents) == 0 or house_presents[-1] < input:
    house_no = len(house_presents) + 1
    house_presents.append(sum(factors(house_no)) * 10)

print("Part 1 solution:", len(house_presents))

factor_tracker = {}

def modif_sum(n):
    sum = 0
    for i in n:
        if i not in factor_tracker:
            factor_tracker[i] = 0
        if factor_tracker[i] < 50:
            sum += i
            factor_tracker[i] += 1
    return sum

house_presents = []

while len(house_presents) == 0 or house_presents[-1] < input:
    house_no = len(house_presents) + 1
    house_presents.append(modif_sum(factors(house_no)) * 11)

print("Part 2 solution:", len(house_presents))