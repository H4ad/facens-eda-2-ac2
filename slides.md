---
# try also 'default' to start simple
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1050&q=80
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# some information about the slides, markdown enabled
---

# Trabalho de AC2

## Um trabalho sobre a implementação do algoritmo de Ford-Fulkerson

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 p-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
   Aperte espaço para ir para a próxima página <carbon:arrow-right class="inline"/>
  </span>
</div>

---

# Algoritmo

```markdown {9-21|9|10|11|1|2|3|4|5|6|7|12|13|14|15|16|17|18|19|20|15-20|12-20|21}
função Atualiza-Grafo-Residual(G, f)
    Para cada aresta a(u,v) em G, , com u,v∈N
           Se f(a) < ca então
               insira aR(u,v) com caR=(ca - f(a))
           Se f(a) > 0 então
               insira aR(v,u) com caR=f(a)
     Retorna(GR)

função Ford-Fulkerson(G, s, t)
   Inicia f(a)=0 para cada aresta a de G
   Defina GR = Atualiza-Grafo-Residual(G, f)
   Enquanto existir caminho de aumento de s para t em GR
        Seja P um caminho de aumento s-t em GR
        Defina cP = min{caR : aR∈P}
        Para cada aresta aR em P
            Se aR tem direção s-t então
                 faça [f(a) → f(a) + cP] em G
           Caso contrário
                faça [f(a) → f(a) - cP] em G
        GR = Atualiza-Grafo-Residual(G, f)
  Retorna (f)
```

<!--
- [9-21]: A função que irá processar o grafo G para obter o fluxo máximo.
- [9]: Na linha 9, começamos pegando os parametros G, que é o grafo, s, que é o vertice inicial e t que é o vertice final.
- [10]: Na linha 10, criamos uma variável que irá guardar, para cada aresta, a sua capacidade.
- [11]: Na linha 11, chamamos a função Atualiza-Grafo-Residual criamos um grafo residual inicial.
- [1]: Na linha 1, temos o método Atualiza-Grafo-Residual que recebe dois parâmetros, o Grafo e a variável com a aresta e sua capacidade.
- [2]: Na linha 2, passamos por cada aresta em G, temos o ponto inicial u e final v, sendo ambos pertencentes a N
- [3]: Na linha 3, caso a capacidade da aresta armazenada em f seja menor que a capacidade da aresta
- [4]: Se for, inserimos então na aresta residual (u,v) uma capacidade residual sendo a capacidade de a menos a capacidade armazenada em f.
- [5]: Na linha 5, verificamos se a capacidade de f na aresta a é maior que zero.
- [6]: Se for, inserimos então na aresta residual (v,u) uma capacidade residual sendo a capacidade armazenada em f.
- [7]: E por fim, terminamos e retornamos o grafo residual resultante.
- [12]: Na linha 12, após atualizar o grafo residual, entramos no looping de: enquanto existir um caminho de aumento de s para t no grafo residual, vamos realizar as seguintes operações:
- [13]: Primeiro, obtemos o caminho de aumento do ponto s até o t do grafo residual, pode ser feito utilizando BFS ou DFS.
- [14]: Depois, obtemos a menor capacidade contida no caminho de aumento P.
- [15]: E aí, rodamos um looping para passar por cada aresta residual em P.
- [16]: Na linha 16, se aresta residual tem direção em s-t, então realizamos a seguinte operação:
- [17]: Definimos que a aresta a em f vai ser a soma da capacidade armazenada em f e a menor capacidade obtida do caminho P.
- [18]: Na linha 18, se a aresta residual não tem direção em s-t, então realizamos a seguinte operação:
- [19]: Definimos que a aresta a em f vai ser a subtração da menor capacidade em P sobre o valor armazenado em f.
- [20]: Depois, chamamos Atualiza-Grafo-Residual novamente para atualizar o GR com os novos valores setados ao passar pelo caminho P de GR.
- [15-20]: E agora, continuamos esse looping até passemos por todas as arestas.
- [12-20]: E assim, continuamos até que não exista mais nenhum caminho de aumento.
- [21]: E por fim, retornamos a variável f que contém a capacidade de fluxo máximo de cada aresta do gráfico, e se quisermos saber o fluxo máximo do grafo, basta somar todos os valores armazenados para cada aresta.
-->

---
theme: seriph
background: https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1050&q=80
class: 'text-center'
highlighter: shiki
---

# Demo

## Agora, iremos visualizar como é o algoritmo rodando sobre um grafo qualquer.

<div class="pt-12">
  <a href="https://www-m9.ma.tum.de/graph-algorithms/flow-ford-fulkerson/index_en.html" target="_blank" class="px-2 p-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
   Clique aqui para abrir a demonstração <carbon:arrow-right class="inline"/>
  </a>
</div>

---

# Implementação

```python
class FordFulkerson:
  def __init__(self, graph):
      self.visitedToken = 1
      self.graph = graph
      
  def run(self, source, sink):
      self.visitedToken = 1
      n = len(self.graph)
      visited = [0]*n
      maxFlow = 0

      while True:
        flow = self.dfs(self.graph.copy(), visited, source, sink, 10**100)
        self.visitedToken += 1
        maxFlow += flow

        if flow == 0:
            return maxFlow

  def dfs(self, graph, visited, node, sink, flow):
      if node == sink:
          return flow

      cap = graph[node]
      visited[node] = self.visitedToken

      for i, capacity in enumerate(cap):
        if visited[i] != self.visitedToken and capacity > 0:
          if capacity < flow:
            flow = capacity

          dfsFlow = self.dfs(graph, visited, i, sink, flow)

          if dfsFlow > 0:
            graph[node][i] -= dfsFlow
            graph[i][node] += dfsFlow

            return dfsFlow

      return 0

graph = [
  [0, 2, 4, 0],
  [0, 0, 3, 1],
  [0, 0, 0, 5],
  [0, 0, 0, 0]
]

ford = FordFulkerson(graph)

graphMaxFlow = ford.run(0, 3)

print('Max Flow: ', graphMaxFlow)
```

<style>
.shiki-container {
  overflow-y: auto;
  max-height: 60vh;
}

span {
  font-size: 8px;
}
</style>

---

# Obrigado!

- Vinícius Lourenço Claro Cardoso (180618)
- Maria Alice dos Santos Lucio (180453)
