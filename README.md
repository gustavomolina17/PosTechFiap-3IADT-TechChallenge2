<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

# <p align="center">PosTechFiap-3IADT-TechChallenge2 - Jan / 25 </p>

# <p align="center">Case de Solução para o Problema do Caixeiro Viajante com Cidades Brasileiras </p>

<b>Contexto do Problema</b>

Uma empresa de logística está expandindo suas operações no Brasil e busca otimizar as rotas de transporte entre seus principais centros de distribuição nas capitais estratégicas do país.<b> O objetivo é determinar a rota mais curta para um caminhão de entregas que parta de uma cidade inicial específica — neste caso, São Paulo —</b>, percorra todas as outras capitais (pontos de entrega) uma única vez e, ao final, retorne à cidade de origem.

Com o aumento no número de cidades envolvidas, calcular manualmente a rota mais eficiente se torna uma tarefa extremamente demorada. A empresa precisa de uma solução baseada em algoritmos de otimização que permita encontrar essa rota de maneira rápida e eficiente, reduzindo custos com combustível, tempo de entrega e desgaste dos veículos.

Esse desafio é <b>um exemplo clássico do Problema do Caixeiro Viajante (TSP - Travelling Salesman Problem)</b>, no qual é necessário encontrar a rota mais curta entre um conjunto de cidades, garantindo que o motorista visite cada uma apenas uma vez e retorne ao ponto de partida.

<b>Objetivo do Projeto</b>

O projeto tem como principal objetivo implementar uma solução computacional que resolva o problema do caixeiro viajante para 5 cidades principais do Brasil, tendo São Paulo como ponto de Partida, representando centros logísticos de grande relevância para a empresa:
<ul>
<li>São Paulo (SP)</li>
<li>Brasília (DF)</li>
<li>Rio de Janeiro (RJ)</li>
<li>Salvador (BA)</li>
<li>Porto Alegre (RS)</li>
<li>Curitiba (PR)</li>
<li>Fortaleza (CE)</li>
<li>Recife (PE)</li>
</ul>

A solução deve calcular a distância entre essas cidades e fornecer a rota mais curta possível que o caminhão deve percorrer, considerando as coordenadas geográficas das cidades. O foco está em otimizar os custos de transporte da empresa ao minimizar a distância percorrida.

<b>Desafios</b>

<b>Otimização de Rota:</b> Encontrar a rota com a distância mais curta entre as cidades exige uma abordagem eficiente, já que o número de possíveis rotas cresce rapidamente com o número de cidades. A solução deve considerar todas as rotas possíveis e retornar a rota com a distância total mais curta.

<b>Distâncias Reais:</b> A solução precisa calcular as distâncias reais entre as cidades, levando em consideração a curvatura da Terra, para garantir que os resultados sejam precisos.

<b>Escalabilidade:</b> Embora o problema seja resolvido inicialmente para 5 cidades, a solução deve ser escalável para lidar com mais centros de distribuição no futuro.

<b>Proposta de Solução</b>

Duas abordagens serão implementadas no algoritmo: ,<b>a força bruta</b>, que consiste em testar todas as rotas possíveis e calcular a distância total de cada uma, selecionando ao final a rota mais curta, e a utilização de <b>algoritmos genéticos</b> que são uma técnica de otimização inspirada na teoria da evolução natural. Com isso, será possível comparar os resultados de ambas as técnicas e avaliar qual delas oferece uma melhor solução para o problema proposto.

<b>Etapas do Projeto</b>:

<b>Coleta de Dados:</b> Utilizar as coordenadas geográficas (latitude e longitude) das cidades escolhidas para calcular as distâncias entre elas.

<b>Cálculo das Distâncias:</b> Implementar a fórmula de Haversine, que leva em consideração a curvatura da Terra, para calcular a distância real entre duas cidades com base nas suas coordenadas geográficas.

Algoritmo de Solução:
    Gerar todas as permutações possíveis das cidades (exceto a cidade inicial, que será fixa).
    Para cada permutação, calcular a distância total da rota.
    Retornar a permutação que tiver a menor distância total como a rota mais curta.

Visualização e Relatório: Apresentar a rota mais curta encontrada pelo algoritmo, incluindo a distância total percorrida e a ordem das cidades a serem visitadas. Se necessário, também poderá ser gerada uma visualização gráfica do percurso.

Resultados Esperados

A solução deve apresentar uma rota otimizada, permitindo à empresa de logística:

Redução de Custos Operacionais: Minimização da quilometragem percorrida e, consequentemente, dos custos com combustível e manutenção.
Otimização do Tempo de Entrega: A rota mais curta também implica menor tempo nas estradas, melhorando a eficiência da entrega.
Melhor Alocação de Recursos: Com a rota otimizada, a empresa poderá planejar melhor sua frota de veículos e as equipes envolvidas nas entregas.

# Autor

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/70485830?v=4" width=115><br>Gustavo Molina](https://github.com/gustavomolina17)
| :---: | 


