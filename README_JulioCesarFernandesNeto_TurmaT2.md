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

## Transformações e Limpeza

-As colunas 10 até 13 do DataFrame foram excluídas pois estavam totalmente vazias e sequer tinha título.

-Para otimizar recursos, a coluna de filhos foi convertida para int8.

-Foi feita remoção de linhas duplicadas.

-A coluna de data, originalmente em string, foi convertida para o formato brasileiro.

-As colunas 3, 6 e 8 foram convertidas para tipos categórigos.

-A coluna 4 originalmente armazena números que representam o estado civil. Então, os números foram trocados pelo estado civil e a coluna 5 foi convertida em tipo categórico.

## Conclusões