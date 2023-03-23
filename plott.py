import matplotlib.pyplot as plt
import pandas as pd

sted="./ResonansData"

data=pd.read_excel(sted)

verdier=data.values
frekvens=verdier[:,0]
kvadrert=verdier[:,3]
u_kvadrert=verdier[:,4]

plt.plot(frekvens,kvadrert)
plt.errorbar(frekvens,kvadrert,u_kvadrert,fmt="o")
plt.title("effektresonanskurve uten tillegsmasse")
plt.xlabel("frekvens [Hz]")
plt.ylabel("kvadratet av (fA) [Hz*mm^2]")
plt.grid()
plt.show()
