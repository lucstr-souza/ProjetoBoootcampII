
# 💊 MediReminder — Gerenciador de Medicamentos

[![CI](https://github.com/lucstr-souza/ProjetoBoootcampII/actions/workflows/ci.yml/badge.svg)](https://github.com/lucstr-souza/ProjetoBoootcampII/actions)

> Aplicação CLI para gerenciamento de medicamentos e horários,
> com integração à API ViaCEP e banco de dados Supabase.

## 🚀 Aplicação publicada
🔗 [Acesse aqui](https://projeto-boootcamp-ii--luisa04castro.replit.app)

---

## 👥 Integrantes do Grupo

| Nome | GitHub |
|---|---|
| Luísa Castro Souza | [@lucstr-souza](https://github.com/lucstr-souza) |
| Maria Eduarda Campelo | [@dudacampelo](https://github.com/dudacampelo) |
| Isabella Sena | [@IsabellaSenaa](https://github.com/IsabellaSenaa)|

---

## 📌 Sobre o projeto

O MediReminder é uma aplicação de linha de comando (CLI) em Python
que permite o gerenciamento de medicamentos para idosos e cuidadores.
Os dados são persistidos em banco de dados PostgreSQL hospedado no Supabase.

---

## 🛠️ Tecnologias utilizadas

- Python 3.9+
- Supabase (PostgreSQL na nuvem)
- API pública ViaCEP
- pytest (testes automatizados)
- Ruff (lint)
- GitHub Actions (CI/CD)
- Replit (deploy)

---

## ⚙️ Como executar localmente

### Pré-requisitos
- Python 3.9 ou superior
- Git instalado

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/lucstr-souza/ProjetoBoootcampII.git
cd ProjetoBoootcampII

# 2. Instale as dependências
pip install -r requisitos.txt

# 3. Configure as variáveis de ambiente
# Crie um arquivo .env com:
# SUPABASE_URL=https://hplvcevjevccodhygyzi.supabase.co
# SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhwbHZjZXZqZXZjY29kaHlneXppIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODExNTA4MTAsImV4cCI6MjA5NjcyNjgxMH0.DJUxyo3VcgetSYbusl3A1kfCydfe17JGyMog2d2cWd4

# 4. Execute a aplicação
python app.py
```

### Funcionalidades
- `1` — Adicionar medicamento
- `2` — Listar medicamentos
- `3` — Marcar medicamento como tomado
- `4` — Consultar CEP do paciente (API ViaCEP)
- `5` — Sair

---

## 🧪 Executar os testes

```bash
pytest testes/
```

## 🔍 Executar o lint

```bash
ruff check .
```

---

## 🗄️ Banco de Dados

O projeto utiliza **Supabase** (PostgreSQL) como banco de dados na nuvem.
A tabela `medicamentos` armazena nome, horário e status de cada medicamento.


