from functools import reduce

def readFromFile(filename):
    with open(filename, 'r') as f:
        s = f.read()

    a = s.split('\n')

    return [float(e) for e in a]

sample = readFromFile('input33.txt')

size = len(sample)

sampleMean = sum(sample) / size

sampleVariance = reduce(lambda acc, val: acc + ((val - sampleMean)**2), sample) / size
