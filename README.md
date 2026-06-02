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
