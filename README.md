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
- Consultar CEP dos pacientes

## Tecnologias
- Python 3.13
- Pytest
- Ruff
- Git e GitHub
- GitHub Actions

## Como executar o projeto

### Pré-requisitos
- Python 3.9 ou superior instalado
- Git instalado

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/lucstr-souza/ProjetoBoootcampII.git
cd ProjetoBoootcampII

# 2. Instale as dependências
pip install -r requisitos.txt

# 3. Execute a aplicação
python -m src.main
```

### Funcionalidades disponíveis
- `1` — Adicionar medicamento
- `2` — Listar medicamentos
- `3` — Marcar medicamento como tomado
- `4` — Consultar CEP do paciente (integração com API ViaCEP)
- `5` — Sair

### Executar os testes
```bash
pytest testes/
```

### Executar o lint
```bash
ruff check .
```

### Integração com API ViaCEP
A opção 4 do menu consulta a API pública [ViaCEP](https://viacep.com.br) 
e retorna o endereço completo a partir de um CEP informado.
Exemplo de uso: digite `01310100` e receba os dados de localização do paciente.

---
