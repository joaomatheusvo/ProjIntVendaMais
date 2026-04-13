# Plataforma de Inteligência Operacional — VendaMais

## 📌 Descrição

Este projeto tem como objetivo desenvolver uma plataforma de inteligência operacional para a empresa VendaMais Distribuidora Ltda.

A solução automatiza a coleta, processamento e análise de dados do ERP, disponibilizando dashboards no Power BI com defasagem máxima de 24 horas.

---

## 👥 Integrantes

- João Matheus — https://github.com/joaomatheusvo
- Juliana Kruger — https://github.com/Julianakruger

---

## 🏗️ Arquitetura

Ingestão → Armazenamento → Transformação → Consumo

A solução é composta pelos seguintes componentes:

- Ingestão → Azure Functions 
- Armazenamento bruto → Azure Blob Storage 
- Transformação → Azure Functions 
- Banco de dados → Azure SQL Database 
- Consumo → Power BI 

---

##  Objetivos

- Automatizar a extração de dados do ERP  
- Centralizar o armazenamento em banco estruturado  
- Garantir qualidade e consistência dos dados  
- Disponibilizar informações para análise e tomada de decisão 

---

## 📂 Estrutura do Repositório

```bash
vendamais-arquitetura/
│
├── app
│   └── app.py
├── docs
│   ├── adr
│   │   ├── ADR-001.md
│   │   └── ADR-002.md
│   └── c4
│       ├── 01-context.md
│       └── 02-container.md
├── README.md
```

---

## 📖 Como navegar

- C4 Nível 1: visão geral do sistema
- C4 Nível 2: detalhamento dos containers
- ADRs: decisões arquiteturais documentadas

---

## ⚙️ Tecnologias

- Azure Functions (Python)
- Azure Blob Storage
- Azure SQL Database
- Power BI
- Python

---

## 🚫 Segurança

Nenhuma credencial sensível é armazenada no repositório.

## Como executar

```bash
pip install -r requirements.txt
python src/app.py
```

##  Processo de Desenvolvimento

O projeto foi desenvolvido utilizando boas práticas de versionamento com Git:

Commits com mensagens descritivas
Sem Branches ou Pull Requests no momento por bug, mas foi tudo revisado

A implementação da API utilizando Flask foi utilizada como uma simulação da camada de ingestão definida na arquitetura. No cenário real, conforme descrito nas ADRs, essa camada seria implementada utilizando Azure Functions no modelo serverless.