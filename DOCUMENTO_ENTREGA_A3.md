# EDUGRADE – CALCULADORA E GESTÃO DE NOTAS ACADÊMICAS
**CENTRO UNIVERSITÁRIO UNA**  
**CURSO:**  Análise e Desenvolvimento de Sistemas  
**DISCIPLINA:** Gestão e Qualidade de Software (GQS)  
**PROFESSOR:** Daniel Henrique Matos de Paiva  

---

## 1. IDENTIFICAÇÃO DOS INTEGRANTES DO GRUPO
> **Repositório do Projeto:** https://github.com/vivoeasy100/calculadora_de_notas_academicas-

| Nome Completo | RA | Usuário GitHub | Função no Projeto |
| :--- | :--- | :--- | :--- |
| **Lucas Henrique Miranda** | `325131396` | [@LuchMiranda](https://github.com/LuchMiranda) | Product Owner & Requisitos do Sistema |
| **Caio Duraes** | `325132875` | [@caiovas28-dotcom](https://github.com/caiovas28-dotcom) | Desenvolvedor Backend & Arquitetura |
| **Gabriel Ferreira** | `325140970` | [@1Gapril](https://github.com/1Gapril) | DevOps & Gestão de Configuração (GitFlow) |
| **Fernando Almeida** | `326132695` | [@vivoeasy100](https://github.com/vivoeasy100) | Engenheiro de Qualidade & Testes (QA/TDD) |

---

## 2. PROBLEMA A SER RESOLVIDO DO MUNDO REAL

No ambiente universitário, o estudante precisa acompanhar o próprio desempenho ao longo de todo o semestre. Na prática, isso é mais difícil do que parece: cada instituição e cada disciplina adota critérios próprios, com avaliações de pesos diferentes (A1, A2, A3), provas integradas e regras específicas para recuperação ou exame final. Como consequência, muitos alunos só descobrem que estão em situação de risco quando já não há tempo hábil para reagir.

Essa falta de previsibilidade e de acompanhamento contínuo contribui diretamente para:
- Ansiedade e desmotivação acadêmica;
- Reprovações que poderiam ter sido evitadas com planejamento antecipado;
- Aumento do risco de evasão universitária.

O problema não é a falta de capacidade do aluno, e sim a falta de **informação clara e no momento certo**. É essa lacuna que o projeto se propõe a preencher.

---

## 3. OBJETIVOS E PÚBLICO-ALVO

**Objetivo geral:** desenvolver uma aplicação em Python que permita ao estudante calcular sua média, conhecer sua situação acadêmica e saber, com antecedência, quanto precisa tirar para ser aprovado.

**Objetivos específicos:**
- Implementar o cálculo de média aritmética e média ponderada com pesos personalizáveis;
- Classificar automaticamente a situação do aluno (aprovado, recuperação ou reprovado);
- Calcular a nota mínima necessária no exame final;
- Armazenar o histórico de alunos, disciplinas e notas de forma persistente;
- Aplicar, durante todo o desenvolvimento, boas práticas de Gestão e Qualidade de Software (Clean Code, TDD, GitFlow e CI/CD).

**Público-alvo:** estudantes universitários que desejam acompanhar suas notas e, secundariamente, orientadores pedagógicos que acompanham o desempenho dos alunos.

---

## 4. SOLUÇÃO PROPOSTA: SISTEMA "EDUGRADE"

O **EduGrade** é uma solução computacional modular, executada no terminal, projetada para oferecer uma ferramenta prática, transparente e confiável de simulação, cálculo e acompanhamento de metas acadêmicas.

### 4.1 Funcionalidades implementadas
1. **Cálculo de Média Ponderada e Aritmética:** permite personalizar o peso de cada avaliação.
2. **Diagnóstico Automático de Situação:** enquadramento imediato em *Aprovado*, *Recuperação / Exame Final* ou *Reprovado*.
3. **Cálculo Preditivo para o Exame:** indica a nota mínima que o aluno precisa obter na prova final para ser aprovado.
4. **Gestão de Estudantes e Boletim:** cadastro de aluno (RA e nome), disciplinas e avaliações, com geração de boletim por disciplina.
5. **Persistência em JSON:** armazenamento do histórico de notas por disciplina e estudante, com tolerância a falhas na leitura e gravação do arquivo.

### 4.2 Regras de negócio adotadas
- **Aprovado:** média maior ou igual a 6,0 (valor padrão, configurável);
- **Recuperação / Exame Final:** média maior ou igual a 4,0 e menor que 6,0;
- **Reprovado:** média menor que 4,0;
- **Nota necessária no exame:** calculada para que a média entre a nota atual e a nota do exame atinja 5,0, ou seja, `nota do exame = (5,0 × 2) − média atual`, limitada ao intervalo de 0,0 a 10,0.

### 4.3 Exemplo de uso
Um aluno tira **4,0 na A1 (peso 0,4)** e **4,5 na A2 (peso 0,6)**. O sistema calcula a média ponderada de **4,30**, classifica a situação como **Recuperação** e informa que ele precisa tirar **5,70 no exame final** para ser aprovado.

---

## 5. REQUISITOS DO SISTEMA

### 5.1 Requisitos funcionais
| Código | Requisito |
| :--- | :--- |
| RF01 | O sistema deve calcular a média aritmética de uma lista de notas. |
| RF02 | O sistema deve calcular a média ponderada a partir de notas e pesos informados. |
| RF03 | O sistema deve classificar a situação do aluno em Aprovado, Recuperação ou Reprovado. |
| RF04 | O sistema deve calcular a nota mínima necessária no exame final. |
| RF05 | O sistema deve cadastrar estudantes (RA e nome), disciplinas e lançar notas com peso. |
| RF06 | O sistema deve gerar o boletim de uma disciplina para o estudante. |
| RF07 | O sistema deve salvar e carregar os dados em arquivo JSON. |

### 5.2 Requisitos não funcionais
| Código | Requisito |
| :--- | :--- |
| RNF01 | **Confiabilidade:** notas fora do intervalo de 0,0 a 10,0 e pesos menores ou iguais a zero devem ser rejeitados com mensagens claras, sem interromper a execução. |
| RNF02 | **Manutenibilidade:** o código deve separar domínio, persistência, exceções e interface. |
| RNF03 | **Testabilidade:** as regras de cálculo devem ser cobertas por testes unitários automatizados. |
| RNF04 | **Portabilidade:** o sistema deve executar em qualquer computador com Python 3.10 ou superior. |
| RNF05 | **Usabilidade:** a interação deve ocorrer por menu de terminal com orientações e mensagens de erro compreensíveis. |

---

## 6. VÍNCULO COM OS OBJETIVOS DE DESENVOLVIMENTO SUSTENTÁVEL (ODS)

O projeto está vinculado diretamente ao **ODS 4: Educação de Qualidade** da Organização das Nações Unidas (ONU), especificamente:
- **Meta 4.3:** acesso e permanência em uma educação superior de qualidade, já que a ferramenta ajuda o aluno a se manter no curso.
- **Meta 4.4:** fortalecimento de habilidades e competências técnicas, tanto pelo uso da ferramenta quanto pelo próprio desenvolvimento do projeto.
- **Incentivo à permanência estudantil:** a ferramenta apoia a redução da evasão através da autoavaliação contínua e da governança sobre o próprio aprendizado.

A ODS 4 busca assegurar uma educação inclusiva, equitativa e de qualidade, e promover oportunidades de aprendizagem ao longo da vida para todos. No ensino superior, um dos maiores obstáculos a esse objetivo é a evasão, que muitas vezes começa de forma silenciosa: o estudante não acompanha a própria média, não entende como os pesos das avaliações influenciam o resultado e só percebe o risco de reprovação quando já não há tempo hábil para reagir. O EduGrade atua justamente nesse ponto. Ao permitir que o aluno simule suas notas, visualize sua situação (aprovado, recuperação ou reprovado) e saiba exatamente quanto precisa tirar no exame final, o sistema transforma uma incerteza em informação concreta e em planejamento. Com mais transparência sobre o próprio desempenho, o estudante ganha autonomia para corrigir a rota a tempo, o que contribui para a redução da retenção e da evasão e fortalece a permanência estudantil.

---

## 7. APLICAÇÃO DAS BOAS PRÁTICAS DE GESTÃO E QUALIDADE DE SOFTWARE (GQS)

1. **Clean Code (Código Limpo):**
   - Nomenclatura semântica e funções com nomes que expressam sua intenção;
   - Aplicação do SRP (*Single Responsibility Principle*): cada módulo tem uma responsabilidade (`calculator.py` para as regras de cálculo, `manager.py` para a persistência, `exceptions.py` para os erros e `main.py` para a interface);
   - Indentação e estilo segundo os padrões PEP 8, verificados por análise estática (Flake8).
2. **Tratamento de Exceções Robusto:**
   - Classes de erro especializadas (`AcademicError`, `InvalidGradeError`, `InvalidWeightError`, `StudentNotFoundError`);
   - Bloqueio de notas fora da faixa (0,0 a 10,0) e proteção contra pesos inválidos e divisão por zero.
3. **Desenvolvimento Guiado por Testes (TDD):**
   - 10 testes unitários automatizados, no padrão AAA (*Arrange, Act, Assert*), cobrindo os fluxos críticos de cálculo, os cenários de erro e o cadastro de estudantes.
4. **Versionamento e GitFlow:**
   - Branches `main` (produção), `develop` (integração) e branches `feature/*` individuais;
   - Histórico construído com commits semânticos (`feat`, `fix`, `test`, `docs`) e integração por Pull Requests.
5. **Automação de CI/CD:**
   - Pipeline no GitHub Actions que executa análise estática e testes a cada push ou pull request para `main` e `develop`.

---

## 8. COMO EXECUTAR O PROJETO

**Pré-requisito:** Python 3.10 ou superior.

```bash
# Executar os testes unitários
python -m unittest discover -s tests

# Executar a aplicação
python main.py
```

---

## 9. LIMITAÇÕES E MELHORIAS FUTURAS

**Limitações atuais:**
- A interface é feita apenas por terminal;
- O sistema usa as regras de aprovação e exame definidas como padrão, e não as de uma instituição específica;
- Os dados são salvos em arquivo JSON local, sem banco de dados.

**Melhorias futuras:**
- Interface gráfica ou web para facilitar o uso por estudantes;
- Migração da persistência para um banco de dados relacional;
- Configuração das regras de aprovação por instituição ou disciplina;
- Gráficos de evolução das notas e alertas de risco de reprovação.

---

## 10. CONSIDERAÇÕES FINAIS

O EduGrade mostra que uma solução simples, bem estruturada e testada pode gerar impacto real na vida acadêmica do estudante, ao transformar regras de cálculo confusas em informação clara e acionável. Além do resultado técnico, o desenvolvimento do projeto permitiu ao grupo aplicar na prática os conceitos de Gestão e Qualidade de Software: organização do código, tratamento de erros, testes automatizados, versionamento com GitFlow e integração contínua, trabalhando em equipe com papéis bem definidos.