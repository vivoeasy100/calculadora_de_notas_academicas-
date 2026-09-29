# Trabalho A3 - Gestão e Qualidade de Software
**Professor:** Daniel Henrique Matos de Paiva  
**Instituição:** Ânima Educação / UNA  
**Tema do Projeto:** EduGrade - Calculadora e Gestão de Desempenho Acadêmico  
**ODS Vinculada:** ODS 4 – Educação de Qualidade (Meta 4.4 / 4.6)  

---

## 👥 Integrantes do Grupo e Divisão Oficial de Papéis

Com base nos 4 membros oficiais da equipe e na estrutura sugerida para a apresentação e entrega prática:

| Integrante | RA | Papel Principal | Responsabilidade na Apresentação (10-15 min) | Responsabilidade Prática no Projeto |
| :--- | :--- | :--- | :--- | :--- |
| **Lucas Henrique Miranda** | `325131396` | **Introdução & Planejamento (PO / Requisitos)** | Abertura (2 a 3 min): Contexto, problema real, ODS 4, requisitos e escopo do sistema. | Elaboração do documento Word/Relatório, definição das regras de negócio, notas e critérios de aprovação. |
| **Caio Duraes** | `325132875` | **Desenvolvimento & Código (Backend Lead)** | Demonstração (4 a 5 min): Execução da aplicação ao vivo, explicação da arquitetura, tratamento de exceções. | Codificação da lógica de negócio em Python/Java/C#, modularização, tratamento de erros (`try/except`). |
| **Gabriel Ferreira** | `325140970` | **Documentação & Versionamento (DevOps / GitFlow)** | Processos Git (2 a 3 min): Fluxo GitFlow (branches `main`, `develop`, `feature/*`), commits semânticos e GitHub. | Gestão do repositório GitHub, templates de PR/Issues, elaboração dos slides PowerPoint e auxílio no Pitch. |
| **Fernando Almeida** | `326132695` | **Qualidade & Testes (QA / TDD / CI-CD)** | Qualidade (3 a 4 min): Metodologia TDD, cobertura de testes unitários, Clean Code e Pipeline de CI (GitHub Actions). | Criação da suíte de testes unitários (`pytest` / `unittest`), automação do CI com GitHub Actions e refatoração. |

---

## 🎯 Definição do Projeto: "EduGrade" (Calculadora de Notas Acadêmicas)

### 1. O Problema Real
Muitos estudantes enfrentam dificuldades para acompanhar sua evolução acadêmica ao longo do semestre devido a sistemas com fórmulas de cálculo complexas (médias ponderadas, pesos distintos entre A1, A2, A3, exames finais e critérios de presença). Essa falta de visibilidade resulta em desistências, reprovações evitáveis e estresse acadêmico.

### 2. A Solução
O **EduGrade** é uma aplicação voltada para estudantes e docentes, permitindo:
- Cadastro estruturado de disciplinas e pesos avaliativos.
- Lançamento de notas parciais (A1, A2, A3, etc.).
- Cálculo automático da média final com cálculo preditivo da "nota necessária para aprovação no exame final".
- Diagnóstico acadêmico imediato: **Aprovado**, **Em Recuperação/Exame** ou **Reprovado**.
- Persistência e exportação de dados (JSON/SQLite).

### 3. Vínculo com a ODS 4 (Educação de Qualidade)
Apoia a retenção escolar e o acompanhamento pedagógico através de ferramentas transparentes que auxiliam na gestão da aprendizagem e combate à evasão.

---

## 📋 Checklist de Critérios do Professor & Status de Atendimento

- [x] **Equipe:** 4 integrantes identificados com Nome e RA.
- [x] **Linguagem:** Python 3 (código modular, legível e multiplataforma).
- [x] **Código Limpo (Clean Code):** Nomes semânticos, funções com responsabilidade única (SRP), indentação padrão PEP8.
- [x] **Tratamento de Erros:** Blocos `try/catch` para entradas numéricas inválidas, notas fora da faixa (0-10), divisão por zero em pesos e arquivos corrompidos.
- [x] **TDD (Test-Driven Development):** Testes unitários com `pytest` / `unittest` cobrindo cálculo de médias, aprovação e cenários de exceção.
- [x] **GitFlow & Commits Semânticos:** Estrutura documentada com branches `main`, `develop`, `feature/*` e commits convencionais (`feat:`, `fix:`, `test:`, `docs:`).
- [x] **CI/CD:** Pipeline automatizado via GitHub Actions executando testes e verificação de lint em cada push/PR.
- [x] **Entregas:**
  - 1. Documento Word (Minuta pronta estruturada).
  - 2. Repositório e Código funcional.
  - 3. Roteiro de PowerPoint para apresentação.
  - 4. Roteiro para o Vídeo Pitch (5 minutos).
