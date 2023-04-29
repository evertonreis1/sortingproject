# Ordenação de Dados

Este é um projeto em trio de ordenação de dados utilizando três estruturas de ordenamento diferentes. O objetivo é aplicar as estruturas e comparar as performances de cada uma delas em relação ao tempo de execução.

## Estruturas de Ordenamento

As estruturas de ordenamento escolhidas para o projeto são:

* QuickSort - implementado em Python por Everton
* TimSort - implementado em JavaScript por Jaiane
* CountingSort - implementado em Java por Lucas

## Dataset

O dataset utilizado para ordenação está disponível em: `https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps`

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

### Counting Sort (Python)

1. Certifique-se de ter o Python ou superior instalado em sua máquina
2. No terminal, navegue até o diretório do projeto
3. Execute o comando `python counting_sort.py`

OBS: 
> O programa foi executado através do Google Colaboratory, com imporatação da base de dados pelo Google Drive. Para realizar a execução na sua máquina, certifique sobre a versão do Python instalada e sobre o arquivo da base usado neste projeto, que deve estar no mesmo diretório do projeto.
>
> Para fazer a leitura do CSV corretamente, modifique o código de importação, substituindo a importação do Google Drive para a importação com a biblioteca **pandas**, com os comandos:
> 
> ``` 
> import pandas as pd
> 
> data = pd.read_csv('caminho/Google-Playstore.csv')
> ```

Nos códigos [Counting_sort.ipynb](counting_sort/Counting_sort.ipynb) (que tem uma descrição detalhada) e [counting_sort.py](counting_sort/counting_sort.py) 
(que tem o apenas o código), isso é descrito de forma melhor.

## Resultados

Os resultados de desempenho de cada estrutura de ordenamento são registrados no arquivo `results.txt`. Para cada estrutura, registramos o tempo de execução em segundos.

## Contribuidores

* Everton - QuickSort (Python)
* Jaiane - TimSort (JavaScript)
* Lucas - Counting Sort (Python)
