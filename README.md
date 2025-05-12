# EDA - Combustíveis Automotivos

Este repositório contém o projeto de Análise Exploratória de Dados (EDA) desenvolvido como Trabalho de Conclusão de Curso (TCC) com base na série histórica de preços de combustíveis automotivos no Brasil, disponibilizada pela ANP por meio do portal [dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp).

## 🎯 Objetivo

O objetivo do projeto é explorar os dados públicos da ANP entre 2004 e 2024, identificar padrões temporais, variações regionais e impactos de eventos históricos sobre os preços da gasolina, etanol e diesel no Brasil.
Este projeto é de caráter acadêmico e tem como base o uso de dados abertos públicos com fins educativos.

## 🛠️ Requisitos

- Python 3.10+
- Bibliotecas indicadas no `requirements.txt`

Após clonar o repositório entre dentro da pasta 'Codigos/':
```bash
cd Codigos
```

Via terminal execute o seguinte comando para ativar o ambiente virtual:
```bash
python -m venv venv
```

Para instalar as dependências, agora dentro do ambiente virtual, rode o comando:
```bash
pip install -r requirements.txt
```

## 🚀 Como executar
### ⬇️ Download
- Faça o download dos arquivos da ANP disponibilizaos no site oficial.

- Os arquivos devem seguir o padrão de nome ca-AAAA-SS.csv. Exemplo: ca-2022-01.csv.

- Coloque todos os arquivos baixados em uma mesma pasta.

### 🛣️ Edição dos Caminhos

- **Importante**: os caminhos de entrada e saída dos arquivos e imagens estão definidos diretamente nos scripts Python com diretórios locais.

- Para executar corretamente os scripts em sua máquina, você deverá editar os caminhos dos arquivos manualmente em cada script (main.py, *.py).

### ⚙️ Execução
- Execute main.py para gerar o dataset consolidado.

- Execute os demais scripts conforme desejar para gerar os gráficos. As imagens serão salvas automaticamente na pasta Graficos.
