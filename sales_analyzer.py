# Analisador de Dados de Vendas

import pandas as pd

class AnalisadorVendas:
    def __init__(self, arquivo):
        self.df = pd.read_csv(arquivo)

    def total_vendas(self):
        """Calcula o total de vendas (Quantidade * Preço Unitário)"""
        self.df['Total'] = self.df['Quantidade'] * self.df['Preço Unitário']
        total = self.df['Total'].sum()
        return total
    
    def media_vendas(self):
        """Calcula a média de vendas"""
        media = self.df['Total'].mean()
        return media
    
    def produto_mais_vendido(self):
        """Identifica o produto mais vendido (com maior quantidade)"""
        produto = self.df.loc[self.df['Quantidade'].idxmax(), 'Produto']
        return produto
    
    def produto_mais_rentavel(self):
        """Identifica o produto mais rentável (com maior valor total de vendas)"""
        produto = self.df.loc[self.df['Total'].idxmax(), 'Produto']
        return produto

def main():
    arquivo = 'vendas.csv'
    analisador = AnalisadorVendas(arquivo) 

    print("Análise de Dados de Vendas")
    print("==========================")
    print(f"Total de Vendas: R${analisador.total_vendas():.2f}")
    print(f"Média de Vendas: R${analisador.media_vendas():.2f}")
    print(f"Produto Mais Vendido: {analisador.produto_mais_vendido()}")
    print(f"Produto Mais Rentável: {analisador.produto_mais_rentavel()}")

if __name__ == "__main__":
    main()
