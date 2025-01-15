import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('new_sweep_results.csv', encoding='unicode_escape')

last_row = data.iloc[-1]

max_i = int(last_row['i'] + 1)
max_j = int(last_row['j'] + 1)
range_i = max_i / 2
range_j = max_j / 2

a = np.zeros((max_i, max_j))

for i in range(max_i):
    for j in range(max_j):
        row = (i  * max_j) + j

        row = data.iloc[row]

        a[i][j] = row['err']

f = plt.figure()
plt.imshow(a, cmap='jet', origin='lower')
plt.colorbar()

plt.title("error for data alignment params for adjustments from len = 17.1 and sfc = 34%")

plt.plot(range_i, range_j, 'ro')

plt.ylabel("len (mm)")
plt.yticks(
    [v for v in range(max_i)], [round(16.9 * (1 + (v - range_i) / max_i), 2) for v in range(max_i)]
)
plt.tick_params(axis='y', labelsize=3)

plt.xlabel("sfc (%)")
plt.xticks(
    [v for v in range(max_j)], [round(34 * (1 + (v - range_j) / max_j), 2) for v in range(max_j)],
    rotation=270,
)
plt.tick_params(axis='x', labelsize=3)

f.savefig("foo.pdf", bbox_inches='tight')
