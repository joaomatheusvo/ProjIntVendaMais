# Plataforma de Inteligência Operacional — VendaMais

## 📌 Descrição

Este projeto tem como objetivo desenvolver uma plataforma de inteligência operacional para a empresa VendaMais Distribuidora Ltda.

A solução automatiza a coleta, processamento e análise de dados do ERP, disponibilizando dashboards no Power BI com defasagem máxima de 24 horas.

---

## 👥 Integrantes

- João Matheus — https://github.com/joaomatheusvo
- Juliana Kruger - 

---

## 🏗️ Arquitetura

A arquitetura segue o modelo de pipeline de dados:

ERP → Azure Functions → Blob Storage → Azure SQL → Power BI

---

## 📂 Estrutura do Repositório

```bash
vendamais-arquitetura/
│
├── docs/
│   ├── c4/
│   │   ├── 01-context.md
│   │   └── 02-container.md
│   │
│   └── adr/
│       ├── ADR-001.md
│       └── ADR-002.md
│
└── README.md
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

---

## 🚫 Segurança

Nenhuma credencial sensível é armazenada no repositório.
