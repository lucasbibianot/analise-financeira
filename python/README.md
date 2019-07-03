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

## Análise de APIs para recuperar cotações de ativos:

1. YAHOO Finance: Necessário instalar as dependências: `pip install yahoo-finance` 
2. YAHOO Finance API: Necessário instalar as dependências: `pip install yahoo_finance_api2`
3. GOOGLE Finance: Necessário instalar a dependência: `pip install googlefinance.client`
4. GOOGLE Finance GET: Necessário instalar a dependência (dependente do item 3): `pip install googlefinance.get`

## API do BACEN 
O BACEN disponibiliza dados refentes aos indicadores financeiros, micro e macro economia, as metas informações dos indicadores existentes estão disponíveis em [Séries Temporais](https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries).
Abaixao listamos algumas APIs utéis: 
- CDI a partir de 1986: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json`
- IPCA a partir de 1980: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json`
- Desocupação a partir de 2012: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.24369/dados?formato=json`
- SELIC a partir de 1986: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json`
- Dólar comercial: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.7831/dados?formato=json`

