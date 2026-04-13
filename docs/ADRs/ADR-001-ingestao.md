# ADR-001: Estratégia de Ingestão de Dados 
### (Juliana)

**Status:** Aceito  |  **Data:** 2026-04-06  |  **Autores:** Equipe VendaMais

## Contexto

A plataforma de Inteligência Operacional da VendaMais requer a extração automatizada de dados do ERP, com baixa intervenção manual e atualização periódica.

Conforme definido no Statement of Work, a arquitetura da solução segue um pipeline de dados em camadas (Ingestão → Armazenamento → Transformação → Consumo), utilizando serviços da plataforma Microsoft Azure.

A camada de ingestão deve ser capaz de executar processos agendados, integrar-se ao ERP e escalar conforme o volume de dados, garantindo eficiência operacional e redução de custos.

## Decisão

Foi adotado o uso de Azure Functions no modelo serverless para implementar a camada de ingestão de dados.

A solução consiste em funções escritas em Python, acionadas por gatilhos de tempo, responsáveis por extrair os dados do ERP e armazená-los no Azure Blob Storage na camada de dados brutos.

## Consequências

(+) Escalabilidade automática conforme demanda  
(+) Modelo de cobrança sob demanda (pay-per-use), reduzindo custos operacionais  
(+) Integração nativa com serviços do ecossistema Azure  

(-) Dependência de ambiente cloud (vendor lock-in)  
(-) Maior complexidade inicial de configuração e monitoramento  

## Alternativas rejeitadas

- API REST com Flask: rejeitada por exigir gerenciamento manual de infraestrutura e menor capacidade de escalabilidade automática  

- Máquina Virtual: rejeitada devido ao custo fixo e necessidade de manutenção contínua do ambiente  

- Processamento via filas: rejeitado por introduzir complexidade arquitetural desnecessária para o escopo atual  

## Links

- Relacionado: ADR-002 (Estratégia de Armazenamento)