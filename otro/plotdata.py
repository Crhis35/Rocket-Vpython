import matplotlib.pyplot as plt
import pandas as pd

cohete = pd.read_csv("data.csv",sep=',',decimal='.')
tiempo = cohete["Tiempo"]
distancia = cohete["Distancia"]

plt.figure(figsize=(10,8))
plt.plot(tiempo,distancia,alpha=1,linewidth=2.5,color='red')
plt.show()