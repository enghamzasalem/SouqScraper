import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

sam = pd.read_csv("OpenSouq.csv").sort_values(['price', 'year'])


#sab = sam.set_index(["name", "type"]).count(level="type")
# print(sab)
kia = sam[sam.type == 'كيا']
kia = kia[kia.year > '2008']
kia = kia[kia.year < '2012']

honday = sam[sam.type == 'هيونداي']
honday = honday[honday.year > '2008']
honday = honday[honday.year < '2012']
#ys = sam.price.apply(lambda x: x.replace(',', '')).astype(int)
ys = kia.price.astype(int)
x = kia.year
honday_ys = honday.price.astype(int)
honday_x = honday.year
plt.plot(x, ys,)
plt.plot(honday_x, honday_ys,)
#plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Sample Visualization")
plt.legend(['Kia', 'Hoyndai'])
plt.show()
