import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados
df = pd.read_csv(
    #Caminho do dataset
    r'',
    parse_dates=['DATA DA COLETA'],
    dayfirst=True
)

# Filtra dados de gasolina no ano de 2024
df = df[(df['ANO'] == 2024) & (df['PRODUTO'].str.upper() == 'GASOLINA')]

# Agrupa por estado e calcula média
media_estado = df.groupby('ESTADO - SIGLA')['VALOR DE VENDA'].mean().sort_values()

# Plot
plt.figure(figsize=(10, 8))
media_estado.plot(kind='barh', color='steelblue')

plt.title('Preço Médio da Gasolina por Estado – 2024', fontsize=14)
plt.xlabel('Preço Médio (R$)')
plt.ylabel('Estado')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

# Caminho para salvamento da imagem gerada
plt.savefig(r'\Graficos\grafico_gasolina_por_estado_2024.png', dpi=300)
plt.show()
