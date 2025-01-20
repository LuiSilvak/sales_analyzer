# Analisador de Dados de Vendas

Este programa realiza uma análise simples dos dados de vendas de produtos contidos em um arquivo CSV. Ele calcula o total de vendas, a média de vendas e identifica o produto mais vendido e o mais rentável.

## Funcionalidades

- Calcula o total de vendas.
- Calcula a média de vendas.
- Identifica o produto mais vendido.
- Identifica o produto mais rentável.

## Requisitos

- Python 3.x
- Biblioteca `pandas`

## Como Usar

1. Clone o repositório:
   
```bash
    git clone https://github.com/LuiSilvak/sales_analyzer.git
    cd sales_analyzer
```

2. Instale a biblioteca pandas:

```bash
    pip install pandas
```

3. Crie um arquivo vendas.csv com os dados de vendas no formato:

```bash
    Produto,Quantidade,Preço Unitário
    Produto A,100,10.50
    Produto B,150,8.75
    Produto C,200,12.30
```

4. Execute o programa:

```bash
    python sales_analyzer.py
```

5. O programa exibirá a análise dos dados de vendas.

## Exemplo de Execução

Entrada (vendas.csv):

```bash
    Produto,Quantidade,Preço Unitário
    Produto 001,100,10.50
    Produto 002,150,8.75
    Produto 003,200,12.30
    .
    .
    .
```

Saída:

```bash
    Análise de Dados de Vendas
    ===========================
    Total de Vendas: R$4615.00
    Média de Vendas: R$1153.75
    Produto Mais Vendido: Produto C
    Produto Mais Rentável: Produto C
```


## Melhorias Futuras

- Análise de vendas por período (mensal, anual, etc.).
- Gráficos para visualização das vendas.
- Suporte para leitura de outros formatos de dados (Excel, JSON).


## Licença

Este projeto está licenciado sob a MIT License.