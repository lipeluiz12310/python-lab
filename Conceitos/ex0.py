#Ex 1, gerar e plotar uma senoide de duração de 1 segundo, com frequência de 5 Hz e amplitude de 1. A amostragem deve ser de 1000 Hz.

import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,1,1000) #tempo de 0 a 1 segundo, com 1000 amostras
f=5 #frequência de 5 Hz
a=1 #amplitude de 1
y=a*np.sin(2*np.pi*f*t) #gerando a senoide
plt.plot(t,y,color='red', linestyle='--', label='Senoide de 5Hz') #plotando a senoide
plt.title('Exercício 1')
plt.xlabel('Tempo (s)')
plt.ylabel('Senoide')
plt.grid(True)
plt.legend(loc='upper right') #posicionamento da legenda
plt.show()