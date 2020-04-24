import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

sam = pd.read_csv("OpenSouq.csv").sort_values('year')


#sab = sam.set_index(["name", "type"]).count(level="type")
# print(sab)
kia = sam[sam.type == 'كيا']
kia = kia[kia.year > '2000']
kia = kia[kia.year < '2020']
kia = kia[kia.price < '40000']

honday = sam[sam.type == 'هيونداي']
honday = honday[honday.year > '2000']
honday = honday[honday.year < '2020']
honday = honday[honday.price < '40000']
#ys = kia.price.apply(lambda x: x.replace('.', '')).astype(int)
ys = kia.price.astype(float)
x = kia.year
honday_ys = honday.price.astype(int)
honday_x = honday.year
plt.plot(x, ys, 'o')
plt.plot(honday_x, honday_ys, 'ro')
#plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Sample Visualization")
plt.legend(['Kia', 'Hoyndai'])
plt.show()
