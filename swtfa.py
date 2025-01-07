import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('sweep_results.csv', encoding='unicode_escape')

last_row = data.iloc[-1]

max_i = int(last_row['i'] + 1)
max_j = int(last_row['j'] + 1)

a = np.zeros((max_i, max_j))

for i in range(max_i):
    for j in range(max_j):
        row = (i  * max_j) + j

        row = data.iloc[row]

        a[i][j] = row['err']

f = plt.figure()
# plt.imshow(a, cmap='hot', interpolation='nearest')
plt.colorbar(plt.pcolor(a))

plt.title("error for data alignment params for adjustments from len = 16.9 and sfc = 33%")

plt.plot(10, 10, 'ro')

plt.ylabel("len")
plt.yticks([v for v in range(max_i)], [int(16.9 * (1 + (v - 10) / 20)) for v in range(max_i)])

plt.xlabel("sfc")
plt.xticks([v for v in range(max_j)], [int(34 * (1 + (v - 10) / 20)) for v in range(max_i)])

f.savefig("foo.pdf", bbox_inches='tight')
