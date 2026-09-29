# 🎓 EduGrade - Calculadora & Gestão de Notas Acadêmicas
> **Trabalho A3 Prático – Gestão e Qualidade de Software**  
> **Professor:** Daniel Henrique Matos de Paiva  
> **Instituição:** Ânima Educação / Centro Universitário UNA  
> **Alinhamento Sustentável:** ODS 4 – Educação de Qualidade  

---

## 👥 Integrantes do Grupo e Divisão de Responsabilidades

| Integrante | RA | Papel no Projeto & Apresentação |
| :--- | :--- | :--- |
| **Lucas Henrique Miranda** | `325131396` | **Introdução, Planejamento & Requisitos (PO)** |
| **Caio Duraes** | `325132875` | **Desenvolvimento & Arquitetura de Software** |
| **Gabriel Ferreira** | `325140970` | **Documentação, Versionamento & GitFlow** |
| **Fernando Almeida** | `326132695` | **Garantia da Qualidade, TDD & CI/CD** |

---

## 🎯 Sobre o Projeto

O **EduGrade** é um sistema desenvolvido para auxiliar discentes e docentes no acompanhamento preciso do desempenho escolar e acadêmico, prevenindo reprovações e desmotivação através do cálculo antecipado de médias ponderadas, regras de aprovação institucional e predição de nota necessária no exame final.

### 🌿 Vínculo com a ODS 4 (Educação de Qualidade)
Apoia as metas da ONU para educação inclusiva e equitativa, reduzindo taxas de evasão ao fornecer visibilidade contínua sobre a evolução pedagógica.

---

## 🚀 Boas Práticas e Critérios Atendidos (GQS)

1. **Linguagem:** Python 3 (código limpo, tipado e legível).
2. **Clean Code & Refatoração:** Separação estrita de responsabilidades entre Domínio (`src/calculator.py`), Persistência (`src/manager.py`), Exceções (`src/exceptions.py`) e Interface (`main.py`).
3. **Tratamento de Exceções:** Validações de intervalos numéricos (0.0 a 10.0), pesos positivos e tipos de dados com classes personalizadas de erro.
4. **TDD (Test-Driven Development):** 100% dos fluxos de cálculo cobertos com testes unitários em padrão AAA (Arrange, Act, Assert).
5. **GitFlow & Commits Semânticos:**
   - Branches: `main`, `develop`, `feature/*`.
   - Padrão de commits: `feat:`, `fix:`, `test:`, `docs:`, `refactor:`.
6. **Integração Contínua (CI/CD):** Pipeline configurado em [ci.yml](file:///.github/workflows/ci.yml) para validação automática de testes e análise estática (Flake8) a cada pull request.

---

## ⚙️ Como Executar o Projeto

### Pré-requisitos
- Python 3.10 ou superior instalado.

### 1. Executar os Testes Unitários (TDD)
```bash
python -m unittest discover -s tests
```

### 2. Executar a Aplicação Interativa
```bash
python main.py
```

---

## 📁 Estrutura do Repositório

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml               # Pipeline de CI/CD automatizado
├── data/                        # Diretório de persistência de dados JSON
├── src/
│   ├── calculator.py            # Regras de negócio e cálculos de notas
│   ├── exceptions.py            # Exceções customizadas do domínio
│   └── manager.py               # Gerenciador de alunos e persistência
├── tests/
│   └── test_calculator.py       # Suíte completa de testes unitários TDD
├── DOCUMENTO_ENTREGA_A3.md      # Minuta completa para o documento Word
├── ROTEIRO_APRESENTACAO_A3.md   # Roteiro de 10 a 15 min e Pitch de 5 min
├── PLANO_DE_EXECUCAO_A3.md      # Mapeamento do grupo e critérios
├── main.py                      # Ponto de entrada interativo da aplicação
└── README.md
```
