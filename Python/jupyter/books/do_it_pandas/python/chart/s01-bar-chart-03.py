# bar chart

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print(plt.style.available)

#%%

# plt.style.use('_mpl-gallery')
# plt.style.use('seaborn-v0_8-dark-palette')
# plt.style.use('ggplot')
# plt.style.use('bmh')
plt.style.use('Solarize_Light2')

# make data:
# ox = 0.5 + np.arange(8) # 0.5부터 1씩 증가, 총 8 개 요소
ox = list(range(8))
oy = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

df = pd.DataFrame({ 'x': ox, 'y': oy })

df['x'] = df['x'] + 0.5

x = df['x'] # x축의 시리즈
y = df['y'] # y축의 시리즈

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()