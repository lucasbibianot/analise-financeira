# Analise-financeira

## Objetivo
Recuperar indicadores financeiros para auxiliar na tomada de decisão na compra ou venda de ativos do mercado variável.
Até o momento mapeamos os seguintes indicadores:
- Histórico de cotações de ativos
- Histórico de SELIC
- Histórico de IPCA
- Historico BOVESPA
- Histórico desemprego
- Histórico S&P500
- Histórico dolar x real

## Etapas
1. Realizar provas de conceito para tentar obter os indicadores em APIs existentes ou realizando scraping de sites especializados
2. Desenvolver análise estatística sobre os dados históricos, para definir correlação entre eles. Devemos nos atentar que a existência de correlação, pode não siginificar "Nada"
3. Elaborar um modelo de regressão que possibilite aplicar as variáveis correlatas para realizar a tentativa de prever os seus valores, para um curto prazo

## Criar o virtual ENV: 
- conda create -n analise-financeira python=3.7

## Instalar as dependências:
- pip install requests
- pip install pandas
- pip install bs4
- pip install scikit_learn 