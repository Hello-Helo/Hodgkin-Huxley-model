# EP1 - Hodgkin-Huxley model

O modelo de Hodgkin-Huxley utiliza circuítos elétricos para caracterizar o
potencial de ação das células nervosas.
Ele foi desenvolvido sem o uso de computadores modernos e foi premiado com o
Nobel de medicina em 1963.

Os pulsos nervosos nas células são modelados aproximando a membrana celular pr
um capacitor, separando as cargas iônicas, os canais inônicos são aproximados
por resistores e o podencial de deslocamento dos íons são geradores.
Os canais de sódio e potássio são dependentes da voltagem, e o canal leak não.

![Esquema do circuíto](figures/circuit.png)

A partir disso, a corrente elétrica pode ser descrita com a seguinte equação
diferencial:

![Equação Da corrente total](https://latex.codecogs.com/png.image?\dpi{110}&space;I_{total}&space;=&space;C_m&space;\frac{dV_m}{dt}&space;&plus;&space;g_K&space;(V_m-V_K)&space;&plus;&space;g_{Na}(V_m-V_{Na})&space;&plus;&space;g_L(V_m-V_L))
