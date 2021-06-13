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

![Equação da corrente total I](https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;I_{total}&space;=&space;C_m&space;\frac{dV_m}{dt}&space;&plus;&space;g_K&space;[V_m-V_K]&space;&plus;&space;g_{Na}[V_m-V_{Na}]&space;&plus;&space;g_L[V_m-V_L])

Como os canais dependentes da voltagem não ficam num mesmo estado ao decorrer
do tempo, temos que o valor da resistência (g<sub>n</sub>) pode ser descrito
a partir de um valor máximo e a proporção de canais abertos, que em si é dado
por Alpha e Beta dependente da voltagem.

![Equação da corrente total II](https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;I_{total}=C_m\frac{dV_m}{dt}&plus;\overline{g_K}n^4[V_m-V_K]&plus;\overline{g_{Na}}m^3h[V_m-V_{Na}]&plus;g_L[V_m-V_L])

![m](https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\frac{dn}{dt}&space;=&space;\alpha_n(V_m)[1-n]&space;-&space;\beta_n(V_m)[n])
![n](https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\frac{dm}{dt}&space;=&space;\alpha_m(V_m)[1-m]&space;-&space;\beta_m(V_m)[m])
![h](https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\frac{dh}{dt}&space;=&space;\alpha_h(V_m)[1-h]&space;-&space;\beta_h(V_m)[h])
