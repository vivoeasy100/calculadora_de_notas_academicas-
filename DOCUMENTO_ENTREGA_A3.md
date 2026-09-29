# MINUTA PARA O DOCUMENTO WORD (ENTREGA A3)
**CENTRO UNIVERSITÁRIO UNA / ÂNIMA EDUCAÇÃO**  
**DISCIPLINA:** Gestão e Qualidade de Software (GQS)  
**PROFESSOR:** Daniel Henrique Matos de Paiva  
**DATA LIMITE:** 16/10/2026  

---

## 1. IDENTIFICAÇÃO DOS INTEGRANTES DO GRUPO

| Nome Completo | RA | Função no Projeto |
| :--- | :--- | :--- |
| **Lucas Henrique Miranda** | `325131396` | Product Owner & Requisitos do Sistema |
| **Caio Duraes** | `325132875` | Desenvolvedor Backend & Arquitetura |
| **Gabriel Ferreira** | `325140970` | DevOps & Gestão de Configuração (GitFlow) |
| **Fernando Almeida** | `326132695` | Engenheiro de Qualidade & Testes (QA/TDD) |

---

## 2. PROBLEMA A SER RESOLVIDO DO MUNDO REAL

No ambiente universitário e escolar, milhares de estudantes enfrentam dificuldades frequentes na gestão de seu desempenho acadêmico ao longo do semestre letivo. Com sistemas institucionais complexos que utilizam critérios de médias ponderadas distintas (pesos entre avaliações A1, A2 e A3), provas integradas e cálculo de nota necessária para exame final/recuperação, muitos alunos só tomam conhecimento de sua situação de risco quando já é tarde demais para recuperação.

Essa falta de previsibilidade e acompanhamento contínuo contribui diretamente para:
- Desmotivação e ansiedade acadêmica;
- Reprovações que poderiam ter sido evitadas com planejamento antecipado;
- Índices crescentes de evasão universitária.

---

## 3. SOLUÇÃO PROPOSTA: SISTEMA "EDUGRADE"

O **EduGrade** é uma solução computacional modular projetada para fornecer aos alunos e orientadores pedagógicos uma ferramenta prática, transparente e confiável para simulação, cálculo e acompanhamento de metas acadêmicas.

### Funcionalidades Implementadas:
1. **Cálculo de Média Ponderada e Aritmética:** Permite personalizar pesos de cada avaliação institucional.
2. **Diagnóstico Automático de Situação:** Enquadramento imediato em *Aprovado*, *Recuperação / Exame Final* ou *Reprovado*.
3. **Cálculo Preditivo para Exame:** Indica com precisão decimal a nota mínima que o aluno necessita obter na prova final para ser aprovado.
4. **Persistência de Dados em Formato JSON:** Armazenamento resiliente de históricos de notas por disciplina e estudante.

---

## 4. VÍNCULO COM OS OBJETIVOS DE DESENVOLVIMENTO SUSTENTÁVEL (ODS)

O projeto está vinculado diretamente ao **ODS 4: Educação de Qualidade** da Organização das Nações Unidas (ONU), especificamente:
- **Meta 4.4:** Fortalecimento de habilidades e competências técnicas.
- **Incentivo à permanência estudantil:** A ferramenta apoia a redução da evasão através da autoavaliação contínua e governança sobre o aprendizado.

---

## 5. APLICAÇÃO DAS BOAS PRÁTICAS DE GESTÃO E QUALIDADE DE SOFTWARE (GQS)

1. **Clean Code (Código Limpo):**
   - Nomenclatura semântica em inglês e português técnico.
   - Aplicação de SRP (*Single Responsibility Principle*): classes com funções delimitadas e independentes.
   - Indentação rigorosa segundo os padrões PEP 8.
2. **Tratamento de Exceções Robusto:**
   - Criação de classes de erro especializadas (`AcademicError`, `InvalidGradeError`, `InvalidWeightError`).
   - Bloqueio de notas fora da faixa (0.0 a 10.0) e proteção contra divisão por zero de pesos.
3. **Desenvolvimento Guiado por Testes (TDD):**
   - Criação de 10 testes unitários automatizados cobrindo todos os fluxos críticos de cálculo e cenários de erro antes da refatoração.
4. **Versionamento e GitFlow:**
   - Uso de branches `main` (produção), `develop` (desenvolvimento) e branches de feature individuais.
   - Histórico construído com commits semânticos (`feat`, `fix`, `test`, `docs`).
5. **Automação de CI/CD:**
   - Pipeline estruturado no GitHub Actions para execução de testes e validação de qualidade a cada pull request.
