 🛡️ Agente Vigilante de Dados: Monitoramento Híbrido Proativo

![Status do Projeto](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![SQL Server](https://img.shields.io/badge/Database-SQL%20Server-red)

## 📝 Sobre o Projeto
Este projeto foi desenvolvido para resolver um problema crítico em operações logísticas e financeiras: a **demora na identificação de anomalias**. Em vez de esperar que um analista abra um dashboard, este **Agente Inteligente** monitora o banco de dados SQL Server em tempo real e dispara alertas imediatos caso as metas de negócio sejam descumpridas.

> "Dados parados não geram ação. Este agente garante que a informação chegue a quem decide, no momento em que o problema ocorre."

---

## 🚀 Funcionalidades Atuais (Fase 1: Motor Python)
- **Vigilância 24/7:** Varredura automática em tabelas de simulação (`tSimulacao_IA`).
- **Regras de Negócio Inteligentes:**
  - 🚨 **Alerta Financeiro:** Identifica quando o Ticket Médio cai abaixo da meta (R$ 100,00).
  - 🚚 **Alerta Logístico:** Detecta custos de frete acima do limite crítico (R$ 4.500,00).
- **Redundância de Comunicação (Omnichannel):**
  - **Telegram Bot:** Envio instantâneo via API (Alta disponibilidade).
  - **WhatsApp:** Interface humana para engajamento rápido da equipe.

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Bibliotecas:** - `Pandas` (Processamento de dados)
  - `SQLAlchemy` (Conexão robusta com Banco de Dados)
  - `PyWhatKit` & `PyAutoGUI` (Automação de mensageria)
  - `Python-Telegram-Bot` (Interface técnica de alertas)
- **Banco de Dados:** SQL Server (Tabelas de Logística Olist)

---

## 📂 Estrutura do Repositório
- `monitor_hibrido.py`: O coração do Agente Vigilante.
- `requirements.txt`: Lista de dependências para replicação do ambiente.
- `.gitignore`: Proteção de dados sensíveis e arquivos de sistema (`venv`, `.env`).
- `*.sql`: (Em breve) Scripts de estruturação de dados.
- `*.pbix`: (Em breve) Dashboard estratégico de suporte.

---

## 📈 Próximos Passos
- [ ] Implementação de Dashboard Executivo no **Power BI**.
- [ ] Migração para **Azure Functions** para execução serverless 24/7.
- [ ] Integração de logs de auditoria no SQL Server.

---

**Desenvolvido por [Guilherme Nicolini](https://github.com/guilherme-nicolini)** *Focado em transformar dados em decisões em tempo real.*
