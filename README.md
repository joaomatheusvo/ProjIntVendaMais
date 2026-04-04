# Plataforma de Inteligência Operacional — VendaMais

## 📌 Descrição

Este projeto tem como objetivo desenvolver uma plataforma de inteligência operacional para a empresa VendaMais Distribuidora Ltda.

A solução automatiza a coleta, processamento e análise de dados do ERP, disponibilizando dashboards no Power BI com defasagem máxima de 24 horas.

---

## 👥 Integrantes

- João Matheus — https://github.com/joaomatheusvo
- Integrante 2

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
