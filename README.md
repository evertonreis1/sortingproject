# Ordenação de Dados

Este é um projeto em trio de ordenação de dados utilizando três estruturas de ordenamento diferentes. O objetivo é aplicar as estruturas e comparar as performances de cada uma delas em relação ao tempo de execução.

## Estruturas de Ordenamento

As estruturas de ordenamento escolhidas para o projeto são:

* QuickSort - implementado em Python por Everton
* TimSort - implementado em JavaScript por Jaiane
* CountingSort - implementado em Java por Lucas

## Dataset

O dataset utilizado para ordenação está disponível em: [Google Play Store Apps - Kaggle](https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps).

## Como Executar

Cada estrutura de ordenamento está implementada em um arquivo separado. Para executar o código em sua própria máquina, siga os seguintes passos:

### QuickSort (Python)

1. Certifique-se de ter o Python 3 instalado em sua máquina
2. No terminal, navegue até o diretório do projeto
3. Execute o comando `python quicksort.py`

### TimSort (JavaScript)

1. Certifique-se de ter o Node.js instalado em sua máquina
2. No terminal, navegue até o diretório do projeto
3. Execute o comando `node timsort.js`

### Counting Sort (Python e Java)

Para executar o arquivo do algoritmo de counting sort (versão em Python):
1. Certifique-se de ter o Python instalado em sua máquina
2. No terminal, navegue até o diretório do projeto
3. Execute o comando `python counting_sort.py`

> **Considerações sobre o código em Python:**
> 
> O programa foi executado através do Google Colaboratory, com imporatação da base de dados pelo Google Drive. Para realizar a execução na sua máquina, certifique sobre a versão do Python instalada e sobre o arquivo da base usado neste projeto, que deve estar no mesmo diretório do projeto.
>
> Para fazer a leitura do CSV corretamente, modifique o código de importação, substituindo a importação do Google Drive para a importação com a biblioteca **pandas**, com os comandos:
> 
> ``` 
> import pandas as pd
> 
> data = pd.read_csv('caminho/Google-Playstore.csv')
> ```
>
> O código [counting_sort.py](counting_sort/counting_sort.py) tem o código de implementação do algoritmo.

> **Considerações sobre o código em Java:**
>
> Em Java, o código foi testado com base em 7 listas de números inteiros gerados aleatoriamente com a classe importada ```Random```, implementada no código 
> da classe [```NumberListGenerator.java```](counting_sort/Java/src/NumberListGenerator.java), que retorna uma lista de inteiros aleatórios dentro de um intervalo definido e uma quantidade de elementos passada.
>
> A implementação do algoritmo de *ordenação em contagem* foi feita de uma forma um pouco diferente do Python, na classe [```CountingSort.java```](counting_sort/Java/src/CountingSort.java), já que feita com base numa lista mais simples. Há, nesse caso, a garantia de que o tamanho da lista de contagem
> será pelo menos igual ao da lista original de análise, além de algumas de diferenças de sintaxe de código.
>
> Foram geradas 7 listas de 1 milhão de elementos cada para testar o algoritmo em 7 intervalos de valores gerados: [0,9], [0,99], [0,999], [0,9999],
> [0,99999], [0,999999] e [0,9999999], criadas na classe principal [**```Main.java```**](counting_sort/Java/src/Main.java).
>
> Após isso, foi utilizado método do sistema ```currentTimeMillis()``` para medir o tempo de execução da ordenação em cada lista, e para garantir
> um tempo médio útil, tal medida foi refeita num loop 1000 vezes, para gerar um tempo médio.
> 
> O tempos médios para cada lista foram colocados no arquivo [```out.txt```](counting_sort/Java/execution/out.txt).
> 
> OBS.: apesar dos valores terem sido gerados de forma média, as limitações no sistema de execução tornam aqueles não confiáveis. 
>
> A conclusão mais precisa possível para esse caso é de que o algoritmo se torna *cada vez menos eficiente conforme a variação do intervalo de valores
> da lista cresce*. 
>
> Ou seja, com uma eficiência **O(n+k)**, onde *n* é o número de elementos da lista e *k* é o intervalo de valores, a velocidade de execução é 
> inversamente proporcional ao valor de k e estática com relação ao valor n.

O texto [exp.md](counting_sort/exp.md) tem algumas explicações e considerações sobre a implementação.

## Resultados

Os resultados de desempenho de cada estrutura de ordenamento são registrados no arquivo `results.txt`. Para cada estrutura, registramos o tempo de execução em segundos.

## Contribuidores

* Everton - QuickSort (Python)
* Jaiane - TimSort (JavaScript)
* Lucas - Counting Sort (Python)
