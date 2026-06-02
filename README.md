# SCTECMiniProjetoAvaliativo01
SCTEC - Mini-Projeto Avaliativo - Módulo 01 - Semana 07

Este é o primeiro projeto avaliativo da "Trilha Análise de Dados > Manipulação de Dados com Python e SQL" no SCTEC. Usou como fonte de dados a Base Varejo, disponível no Kaggle.

Base Varejo: https://www.kaggle.com/datasets/namespaiva/base-varejo/data

## Requisitos
Python 3.12.3  
Pandas 3.0.3

## Árvore do projeto

<pre>
├── data
│   ├── processed
│   │   └── Base_Varejo_Limpa.csv
│   └── raw
│       └── Base Varejo.csv
├── notebooks
│   └── MiniProjetoAvaliativo.ipynb
├── outputs
│   ├── charts
│   └── reports
├── README_JulioCesarFernandesNeto_TurmaT2.md
└── src
    ├── __pycache__
    │   └── utils.cpython-313.pyc
    └── utils.py

10 directories, 6 files
</pre>

## Instruções

Abra o arquivo MiniProjetoAvaliativo.ipynb no VS Code e execute todas as células em sequência. Repare que o arquivo já vem com as saídas pertinentes.

## Dicionário de datos Base_Varejo_Limpa.csv

0. DATA: Data da compra;
1. CO_ID: Identificação do número de compra (número da nota fiscal);
2. CL_ID: Identificação do cliente (número do cliente);
3. CL_GENERO: Sexo biológico informado pelo cliente;
4. CL_EC: Estado civil do cliente: Casado ou união estával; Divorciado; Separado; Solteiro; Viúvo.
5. CL_FHL: Número de filhos do cliente;
6. CL_SEG: Segmentação econômica do cliente (classe A, B ou C);
7. PR_ID: Código do produto (SKU) adquirido;
8. PR_CAT: Categoria do produto adquirido;
9. PR_NOME: Nome do produto adquirido.

# Transformações e Limpeza

-As colunas 10 até 13 do DataFrame foram excluídas pois estavam totalmente vazias e sequer tinha título.

-Para otimizar recursos, a coluna de filhos foi convertida para int8.

-Foi feita remoção de linhas duplicadas.

-A coluna de data, originalmente em string, foi convertida para o formato brasileiro.

-As colunas 3, 6 e 8 foram convertidas para tipos categórigos.

-A coluna 4 originalmente armazena números que representam o estado civil. Então, os números foram trocados pelo estado civil e a coluna 5 foi convertida em tipo categórico.

## Conclusões

Na separação dos clientes por gênero, 52,05% são mulheres e 47,95% são homens.

O máximo de filhos por cliente é 4.

A maioria dos clientes possui estado civil "SEPARADO".

"ALIMENTOS", "HIGIENE" e "LIMPEZA" são as categorias que mais vendem. As porcentagens são, respectivamente, 52,38%, 18,77% e 17,54%. As demais categorias somadas correspondem a 11,3%.

Quando separamos as vendas por classe social, a ordem das categorias mais vendidas não se altera. Além disso, as porcentagens também variam pouco.

Quando separamos as vendas totais por anos (entre 2019 e 2022), vemos um crescimento das vendas ano a ano, menos quando chega em 2022, quando uma queda é registrada, ficando abaixo de 2019, o primeiro ano do registro.

Quando separamos cinco produtos mais vendidos por estado civil, notamos que presunto cozido é o produto mais vendido em todas as categorias. É digno de nota que solteiros compram papinha infantil, casados ou em união estável compram preservativo e separados compram chupeta. Esses aspectos merecem uma investigação mais aprofundada.
