from functools import reduce
from math import sqrt, exp

def readFromFile(filename):
    with open(filename, 'r') as f:
        s = f.read()

    a = s.split('\n')

    return [float(e) for e in a]

sample = readFromFile('input33.txt')

size = len(sample)

sampleMean = sum(sample) / size

sampleVariance = reduce(lambda acc, val: acc + val**2, sample)/size - sampleMean**2

eps = 2*sqrt(sampleVariance) / sqrt(size)

def exponential_distribution_CDF(x):
    lambd = 1 / sampleMean
    return 1 - exp(-lambd*x)

# min = 0; max = 2.5

k = [0, 0.3, 0.6, 0.9, 1, 1.2, 1.5, 1.75, 2, 2.3, 2.5]
P_k = [exponential_distribution_CDF(k[i+1]) - exponential_distribution_CDF(k[i]) for i in range(len(k) - 1)]
n_k = [0 for i in range(len(k) - 1)]

for item in sample:
    for i in range(1, len(k)):
        if item <= k[i]:
            n_k[i-1]+=1
            break

chiSquared = 0
for probability, num  in zip(P_k, n_k):
    chiSquared += ((num - size * probability)**2) / (size * probability)

chiSquaredThreshold = 15.5

print(
    f'Размер: {size:d}\n'
    f'Выборочное среднее: {sampleMean:f}\n'
    f'Выборочная дисперсия: {sampleVariance:f}\n'
    f'Доверительный интервал: ({-eps:f}; {eps:f})\n'
    f'Значение Хи-квадрат Пирсона: {chiSquared:f}\n'
    'Гипотеза принята' if chiSquared < chiSquaredThreshold else 'Гипотеза отклонена'
)
