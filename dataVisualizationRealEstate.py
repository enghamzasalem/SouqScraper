import matplotlib.pyplot as plt
import pandas as pd
# Look at index 4 and 6, which demonstrate overlapping cases.

sam = pd.read_csv("OpenSouqRealEstate.csv").sort_values('km')

#sab = sam.set_index(["name", "type"]).count(level="type")
marg = sam[sam.address == 'عمان مرج الحمام']
marg = marg[marg.price < '150000']
marg = marg[marg.km < '250']
khalda= sam[sam.address == 'عمان خلدا']
khalda = khalda[khalda.price < '150000']
khalda = khalda[khalda.km < '250']
plt.plot(marg.km, marg.price, 'o')
plt.plot(khalda.km, khalda.price, 'ro')
plt.plot()
plt.xlabel("price")
plt.ylabel("Sq")
plt.title("Bar Chart Example")
plt.legend(["مرج الحمام","خلدا"])
plt.show()