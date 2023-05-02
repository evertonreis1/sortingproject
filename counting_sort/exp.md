## Counting sort

Os algoritmos de *counting sort* usados foram:

> **Python**:
> ```
> def counting_sort(l):
>    counting_values = [0] * (max(l) + 1)
>    for number in l:
>        counting_values[number] += 1
>
>    positions = [0] * len(l)
>    current = 0
>
>    for index, value in enumerate(counting_values):
>        for pos in range(value):
>            positions[current] = index
>            current += 1
>
>   return positions
> ```
> #### Análise de código:
> 
> Considere **```n```** como o tamanho da lista **```l```**, que é parâmetro da função.
> 
> Na linha 2, deste trecho, tem-se:
> 
> ```counting_values = [0] * (max(l) + 1)```
> 
> A quantidade de passos é determinada pelo tamanho da lista, ou seja, n passos.
>
> Em sequência, tem-se:
> ```
> for number in l:
>    counting_values[number] += 1
> ```
> 
> Aqui, para cada número em l, faz se umaz soma, totalizando também n passos.
> 
> Depois, outra atribuição semelhante, de n passos:
> 
> ```
> positions = [0] * len(l)
> current = 0
> ```
>
> Por fim, tem-se:
> 
> ```
> for index, value in enumerate(counting_values):
>    for pos in range(value):
>        positions[current] = index
>        current += 1
> ```
> 
> Aqui, para cada *len(n)* operações, são realizdas k operações, onde k é o número do intervalo de valores da lista.
>
> Como o algoritmo depende apenas das duas contagens, sua complexidade é **O(n+k)**.



> Java:


---

#### Especificações de execução:
- Sistema: Windows 7 Pro
- Tipo SO: 64 bits
- RAM: 2 GB
- Ambientes: Google Colaboratory © 2023 & Intellij IDEA 2022.2
- Linguagens: Python 3 & Java 8
- Análise de código: Manual
- Tempo de execução total médio da função: 23s (Python) & 0.006s (Java) 
