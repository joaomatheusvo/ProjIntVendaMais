# ADR-002: Estratégia de Armazenamento de Dados 
### (Juliana)

**Status:** Aceito  |  **Data:** 2026-04-06  |  **Autores:** Equipe VendaMais

## Contexto

A solução da VendaMais necessita armazenar dados provenientes do ERP de forma estruturada, garantindo rastreabilidade, histórico e suporte a análises de negócio.

De acordo com o SOW, a arquitetura prevê a utilização de duas camadas de armazenamento: uma camada de dados brutos e uma camada de dados tratados, utilizando serviços da plataforma Azure.

A solução deve permitir consultas eficientes, integração com ferramentas de Business Intelligence e escalabilidade conforme o crescimento do volume de dados.

## Decisão

Foi adotada uma estratégia de armazenamento baseada em Azure Blob Storage e Azure SQL Database.

O Azure Blob Storage será utilizado para armazenar os dados brutos e processados, organizados por data de ingestão, garantindo rastreabilidade e histórico.

O Azure SQL Database será utilizado como banco de dados relacional para armazenar os dados tratados, servindo como fonte única de verdade para consultas e integração com o Power BI.

## Consequências

(+) Alta escalabilidade e disponibilidade dos dados  
(+) Separação entre dados brutos e dados tratados, aumentando rastreabilidade  
(+) Integração direta com ferramentas de análise como Power BI  

(-) Custo contínuo associado ao uso dos serviços cloud  
(-) Dependência do ecossistema Azure  

## Alternativas rejeitadas

- PostgreSQL: rejeitado por não estar totalmente integrado ao ecossistema Azure proposto no SOW  

- SQLite: rejeitado devido à limitação de escalabilidade e suporte a múltiplos acessos concorrentes  

- Banco NoSQL (MongoDB): rejeitado por não atender adequadamente às necessidades de consultas relacionais e analíticas  

## Links

- Relacionado: ADR-001 (Estratégia de Ingestão)