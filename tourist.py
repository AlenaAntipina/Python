import math
import random


def distant_district(p, q):
    d = 0
    for i in range(len(p)):
        d += math.fabs(p[i] - q[i + 1])
    return (d)


def max(N, num):
    max_n = N[0]
    ind = 0
    for i in range(len(N)):
        if max_n < N[i]:
            max_n = N[i]
            ind = i
    if max_n > num:
        N[ind] = num
    return (N)


M = random.randint(5, 10)
N = random.randint(2, M - 1)

alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
            'Ц']

dimensions = random.randint(2, 10)
coords = []
for j in range(dimensions):
    coords.append(random.randint(0, 10000))

sub = []
for i in range(M):
    sub.append([alphabet[i]])
    for j in range(dimensions):
        sub[i].append(random.randint(0, 10000))

k = []
for i in range(M):
    k.append([distant_district(coords, sub[i]), sub[i][0]])

end = []
for i in range(N):
    end.append(k[i])

for i in range(M - N):
    end = max(end, k[i + N])

end.sort()

for i in range(len(end)):
    print(end[i][1], end=' ')




