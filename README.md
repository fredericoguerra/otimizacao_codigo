# Otimização de código utilizando saltos condicionais

Foram realizados 4 testes a fim de avaliar a otimização de saltos condicionais dentro de dois laços aninhados para operação com matrizes.
O código original está contido no *arquivo otimizacao_condicional_original.py*, enquanto a versão otimizada para avaliação está no arquivo *arquivo otimizacao_condicional.py*.

A versão original é composta pelo seguinte código:
```python
n = 200
a = []
b = []
d = []
c = np.ones((n,n))

for i in range(0,n):
        a.append(i*5.3)
        b.append(i+0.8)
        d.append(i+0.1)

    for i in range(0,n):
        for j in range(0,n):
            c[i][j] = i*0.3

    for k in range(0,n):
        if a[k]>b[k]:
            for i in range(0,n):
                for j in range(0,n):
                    c[i][j] += k + (b[k] * a[k])/(j + 1)
        else:
            for i in range(0,n):
                for j in range(0,n):
                    c[i][j] += k + (b[k] * a[k])/(j + 1)
```

A versão avaliada após a otimização consiste na substituição da linha 18, que verifica se cada elemento do vetor a é maior que o elemento na posição correspondente do vetor b, por um vetor auxiliar booleano com valores verdadeiros paras as instâncias de a maiores que a do vetor b e falso para o contrário. A seguir pode ser vista versão otimizada.

``` python
n = 200
a = []
b = []
d = []
c = np.ones((n,n))
maior = []

for i in range(0,n):
        a.append(i*5.3)
        b.append(i+0.8)
        d.append(i+0.1)
        maior.append(a[i]<=b[i])

    for i in range(0,n):
        for j in range(0,n):
            c[i][j] = i*0.3

    for k in range(0,n):
        if maior[k]:
            for i in range(0,n):
                for j in range(0,n):
                    c[i][j] += k + (b[k] * a[k])/(j + 1)
        else:
            for i in range(0,n):
                for j in range(0,n):
                    c[i][j] += k + (b[k] * a[k])/(j + 1)
```

Por fim, as versões invertidas trocam o sinal de > por <= na condicional de comparação entre os elementos de a e b. A tabela abaixo mostram que houve uma redução de 7.23% no tempo de execução da versão otimizada em relação à original.

| Versão  |  Tempo (s)  | Otimização Relativa |
| ------------------- | ------------------- | ------------------- |
|  Original |  5.58545 | - |
|  **Após otimização** |   **5.17865** | **- 7.23 %** |
|  Original Invertida |  5.57677 | - 0.15 % |
|  Após otimização Invertida |  8.51751| 52.49% |
