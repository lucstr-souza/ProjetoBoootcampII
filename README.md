# 💊 Lembrete de Medicações

## Descrição do Problema
Muitas pessoas, especialmente idosos ou pacientes em tratamento contínuo, enfrentam dificuldades para lembrar de tomar seus medicamentos nos horários corretos. Isso pode comprometer a eficácia do tratamento e causar riscos à saúde.
  
## Proposta da solução
Sistema simples que permite registrar medicamentos, horários e acompanhar se foram tomados.

## Público-alvo
- idosos
- pacientes com tratamento contínuo
- pessoas com rotina intensa
- Cuidadores

## Funcionalidades
- Adicionar medicamento
- Listar medicamentos
- Marcar medicamento como tomado

## Tecnologias
- Python 3.13
- Pytest
- Ruff
- Git e GitHub
- GitHub Actions

## Instalação
```bash
# 1. Clonar repositório
git clone https://github.com/SEU-USUARIO/medireminder.git
cd medireminder

# 2. Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Execução da aplicação
python -m src.main

# 5. Executar testes
python -m pytest

# 6. Executar Lint
python -m ruff check .

# Versão
1.0.0

# Autor
Luisa Castro Souza - github.com/lucstr-souza

# Repositório
https://github.com/lucstr-souza/ProjetoBoootcampII.git
