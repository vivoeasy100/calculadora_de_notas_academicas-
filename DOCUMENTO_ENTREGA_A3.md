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

### Dados complementares para contextualização do problema

- **Dimensão da educação superior no Brasil:** segundo o Censo da Educação Superior de 2024, o país registrou **10.226.873 matrículas em cursos de graduação**, um crescimento de **2,5% em relação a 2023**. Esse dado ajuda a dimensionar o público potencial de ferramentas de apoio acadêmico; por si só, não representa uma taxa de reprovação ou evasão. Fonte: [Apresentação do Censo da Educação Superior 2024 — Inep](https://download.inep.gov.br/educacao_superior/censo_superior/documentos/2024/apresentacao_censo_da_educacao_superior_2024.pdf).
- **Acompanhamento de trajetórias:** o Inep disponibiliza indicadores específicos para acompanhar trajetórias na educação superior, incluindo séries históricas por período. Essas bases podem apoiar futuras análises do contexto de permanência estudantil, mas não medem o impacto do EduGrade. Fonte: [Indicadores de Trajetória da Educação Superior — Inep](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/indicadores-de-trajetoria-da-educacao-superior).
- **Necessidade atendida pela solução:** o sistema concentra, em um único fluxo, a média calculada, a classificação acadêmica e uma estimativa da nota necessária no exame final. O benefício previsto é informacional e de planejamento; a eficácia sobre reprovação ou evasão ainda exigiria avaliação própria com usuários e dados de acompanhamento.

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

### Delimitação prática do escopo

- **Entrada de dados:** o simulador rápido recebe duas avaliações (A1 e A2) com pesos informados pelo usuário; no fluxo de gestão, o usuário informa quantas avaliações deseja cadastrar para uma disciplina.
- **Saída principal:** média ponderada, classificação acadêmica e, quando aplicável, estimativa da nota necessária no exame final.
- **Registro acadêmico:** o cadastro associa um estudante ao RA, ao nome, às disciplinas e às avaliações registradas.
- **Fora do escopo atual:** autenticação de usuários, acesso simultâneo por diferentes dispositivos, integração com sistemas acadêmicos institucionais e configuração de regras específicas de cada universidade.

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

### 4.4 Detalhamento dos cálculos e da operação

**Média aritmética:** soma das notas dividida pela quantidade de notas informadas.

\[\text{Média aritmética} = \frac{n_1+n_2+\cdots+n_k}{k}\]

**Média ponderada:** cada nota é multiplicada pelo peso correspondente; a soma dos produtos é dividida pela soma dos pesos. Assim, os pesos não precisam necessariamente somar 1, desde que sejam positivos.

\[\text{Média ponderada} = \frac{\sum_{i=1}^{k}(n_i\times p_i)}{\sum_{i=1}^{k}p_i}\]

No exemplo acima: `(4,0 × 0,4) + (4,5 × 0,6) = 1,6 + 2,7 = 4,3`. Como os pesos somam `1,0`, a média é `4,3`. Para a meta de exame de `5,0`, a fórmula implementada é `(5,0 × 2) − 4,3 = 5,7`.

**Fluxo do menu principal:**

| Opção | Operação disponível |
| :---: | :--- |
| 1 | Exibir os integrantes do grupo e seus papéis. |
| 2 | Calcular rapidamente a média e a situação acadêmica. |
| 3 | Cadastrar estudante, registrar disciplina e avaliações e gerar boletim. |
| 4 | Carregar dados de demonstração dos quatro integrantes do grupo. |
| 5 | Encerrar a aplicação. |

**Organização técnica:** `main.py` coordena a interface; `src/calculator.py` contém as regras de cálculo; `src/manager.py` administra estudantes, disciplinas, avaliações e arquivo JSON; e `src/exceptions.py` reúne exceções próprias do domínio acadêmico.

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

### 5.3 Critérios objetivos de verificação

| Código | Critério de verificação | Evidência prevista |
| :--- | :--- | :--- |
| CV01 | Uma lista com notas `7,0`, `8,0` e `9,0` deve produzir média aritmética `8,0`. | Teste automatizado de média aritmética. |
| CV02 | Uma lista vazia não deve produzir uma média válida. | Verificação de exceção para entrada vazia. |
| CV03 | Notas inferiores a `0,0` ou superiores a `10,0` devem ser rejeitadas pela validação de domínio. | Teste de notas inválidas. |
| CV04 | Para A1 `6,0` com peso `0,4` e A2 `8,0` com peso `0,6`, a média ponderada deve ser `7,2`. | Teste de média ponderada. |
| CV05 | Um peso igual a zero deve ser rejeitado no cálculo ponderado. | Teste de peso inválido. |
| CV06 | Com os parâmetros padrão, média `6,0` classifica o estudante como aprovado; média `4,0` permite recuperação; média `3,9` resulta em reprovação. | Testes de classificação de situação. |
| CV07 | Para média atual `4,0` e meta de exame `5,0`, a nota necessária calculada deve ser `6,0`. | Teste do cálculo de exame. |
| CV08 | O cadastro de estudante e o lançamento de avaliações devem permitir gerar um boletim com média e situação. | Teste do gerenciador acadêmico. |

Esses critérios tornam explícitos alguns resultados esperados para demonstração e verificação. Eles não substituem os requisitos institucionais específicos, que não fazem parte da configuração atual do sistema.

---

## 6. VÍNCULO COM OS OBJETIVOS DE DESENVOLVIMENTO SUSTENTÁVEL (ODS)

O projeto está vinculado diretamente ao **ODS 4: Educação de Qualidade** da Organização das Nações Unidas (ONU), especificamente:
- **Meta 4.3:** acesso e permanência em uma educação superior de qualidade, já que a ferramenta ajuda o aluno a se manter no curso.
- **Meta 4.4:** fortalecimento de habilidades e competências técnicas, tanto pelo uso da ferramenta quanto pelo próprio desenvolvimento do projeto.
- **Incentivo à permanência estudantil:** a ferramenta apoia a redução da evasão através da autoavaliação contínua e da governança sobre o próprio aprendizado.

A ODS 4 busca assegurar uma educação inclusiva, equitativa e de qualidade, e promover oportunidades de aprendizagem ao longo da vida para todos. No ensino superior, um dos maiores obstáculos a esse objetivo é a evasão, que muitas vezes começa de forma silenciosa: o estudante não acompanha a própria média, não entende como os pesos das avaliações influenciam o resultado e só percebe o risco de reprovação quando já não há tempo hábil para reagir. O EduGrade atua justamente nesse ponto. Ao permitir que o aluno simule suas notas, visualize sua situação (aprovado, recuperação ou reprovado) e saiba exatamente quanto precisa tirar no exame final, o sistema transforma uma incerteza em informação concreta e em planejamento. Com mais transparência sobre o próprio desempenho, o estudante ganha autonomia para corrigir a rota a tempo, o que contribui para a redução da retenção e da evasão e fortalece a permanência estudantil.

### Dados de referência e delimitação da contribuição para a ODS 4

- **Meta 4.3:** a ONU a relaciona ao acesso igualitário de mulheres e homens à educação técnica, profissional e superior de qualidade, incluindo a universidade.
- **Meta 4.4:** a ONU a relaciona ao aumento de jovens e adultos com competências relevantes, incluindo competências técnicas e profissionais para o trabalho.
- **Relação com o EduGrade:** a ferramenta tem relação indireta com o tema por fornecer informação para o acompanhamento de notas e por ser um projeto de desenvolvimento de software. Ela não substitui políticas de acesso e permanência, acompanhamento pedagógico ou apoio financeiro e psicossocial.
- **Limite de evidência:** o dado de matrículas do Censo da Educação Superior contextualiza a dimensão do setor, mas não comprova uma relação causal entre uso de calculadoras de notas e redução de evasão. Para medir esse resultado seriam necessárias métricas definidas antes e depois do uso, participação de estudantes e análise de dados ao longo do tempo.

Referência oficial: [Objetivo de Desenvolvimento Sustentável 4 — Nações Unidas](https://sdgs.un.org/goals/goal4).

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

### 7.1 Inventário dos testes automatizados

O arquivo `tests/test_calculator.py` possui **10 métodos de teste**. Os cenários registrados no código incluem:

| Área | Cenários verificados |
| :--- | :--- |
| Média aritmética | Cálculo com `[7,0; 8,0; 9,0]`, rejeição de lista vazia e rejeição de notas inválidas (`11,5` e `-1,0`). |
| Média ponderada | Cálculo com notas `6,0` e `8,0`, usando pesos `0,4` e `0,6`; rejeição de peso igual a zero. |
| Classificação | Aprovação com médias `7,5` e `6,0`; recuperação com `5,5` e `4,0`; reprovação com `3,9` e `1,5`. |
| Exame final | Nota necessária calculada para médias atuais de `4,0` e `5,0`, considerando meta de `5,0`. |
| Gestão de estudantes | Cadastro de um estudante, lançamento de A1 e A2 e emissão de boletim com média `8,6` e situação `APROVADO`. |

**Observação sobre cobertura:** a quantidade de métodos de teste não equivale a percentual de cobertura do código. O repositório possui testes automatizados para os cenários listados; um percentual de cobertura só deve ser informado depois da execução de uma ferramenta de medição apropriada.

### 7.2 Detalhes do pipeline de integração contínua

A configuração atual do arquivo `.github/workflows/ci.yml` estabelece:

- **Ambiente:** `ubuntu-latest`.
- **Versão de Python configurada no CI:** Python `3.10`.
- **Dependências instaladas na automação:** `pytest` e `flake8`.
- **Testes:** execução por meio de `pytest -v`.
- **Análise estática:** o primeiro comando do Flake8 interrompe o fluxo para um conjunto de erros críticos selecionados; uma segunda execução apresenta avisos de estilo com `--exit-zero`, portanto esses avisos, isoladamente, não falham o pipeline.
- **Eventos monitorados:** `push` e `pull_request` direcionados às branches `main` e `develop`.

O pipeline automatiza verificações, mas não deve ser descrito como garantia absoluta de ausência de defeitos; ele verifica os cenários de teste e as regras de análise configuradas.

---

## 8. COMO EXECUTAR O PROJETO

**Pré-requisito:** Python 3.10 ou superior.

```bash
# Executar os testes unitários
python -m unittest discover -s tests

# Executar a aplicação
python main.py
```

### Passo a passo adicional para execução local

1. Confira a versão do Python:

   ```bash
   python --version
   ```

2. Na pasta raiz do repositório, execute os testes:

   ```bash
   python -m unittest discover -s tests
   ```

3. Inicie a interface interativa:

   ```bash
   python main.py
   ```

4. No menu, selecione a opção `2` para testar o cálculo rápido ou a opção `3` para cadastrar um estudante, informar a disciplina, lançar avaliações e gerar o boletim. A opção `4` carrega registros demonstrativos dos integrantes do grupo.

**Execução pelo mesmo comando usado no CI:** depois de instalar `pytest` e `flake8` no ambiente local, também é possível executar `pytest -v`, conforme o workflow do GitHub Actions.

**Arquivo de dados:** o gerenciador utiliza `data/students.json` por padrão. O conteúdo é gravado localmente, e o diretório pode ser criado automaticamente quando o sistema salva os primeiros registros.

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

### Observações adicionais de operação e segurança

- **Acesso:** a aplicação atual não implementa autenticação, perfis de acesso ou permissões separadas para estudantes e orientadores.
- **Armazenamento:** os registros ficam em um arquivo JSON local; não há banco de dados remoto, sincronização entre dispositivos ou rotina de backup implementada.
- **Privacidade:** como o sistema pode armazenar nome, RA, disciplinas e notas, recomenda-se utilizar dados fictícios em demonstrações públicas e proteger o arquivo local que contenha dados reais.
- **Integridade de arquivos:** o carregamento trata erros de leitura e JSON inválido, inicializando a estrutura em memória vazia; a gravação não apresenta um tratamento explícito equivalente para falhas de escrita. Isso deve ser considerado em futuras melhorias.
- **Regras acadêmicas:** a média padrão de aprovação e a meta do exame são definidas no código. A aplicação não consulta regulamentos acadêmicos de instituições nem confirma se as regras adotadas correspondem às de um curso específico.
- **Uso responsável:** a nota prevista pelo programa é uma estimativa matemática com base nos valores informados. O resultado deve ser conferido com o regulamento da disciplina ou com a instituição de ensino.

---

## 10. CONSIDERAÇÕES FINAIS

O EduGrade mostra que uma solução simples, bem estruturada e testada pode gerar impacto real na vida acadêmica do estudante, ao transformar regras de cálculo confusas em informação clara e acionável. Além do resultado técnico, o desenvolvimento do projeto permitiu ao grupo aplicar na prática os conceitos de Gestão e Qualidade de Software: organização do código, tratamento de erros, testes automatizados, versionamento com GitFlow e integração contínua, trabalhando em equipe com papéis bem definidos.

### Indicadores técnicos verificáveis do projeto

| Indicador | Informação documentada |
| :--- | :--- |
| Linguagem e ambiente | Python 3; o workflow do CI configura Python 3.10. |
| Interface | Menu interativo executado pelo terminal (`main.py`). |
| Módulos principais | `src/calculator.py`, `src/manager.py` e `src/exceptions.py`, além do ponto de entrada `main.py`. |
| Testes automatizados | 10 métodos de teste no arquivo `tests/test_calculator.py`, com cenários de cálculo, validação, classificação, exame e cadastro. |
| Ferramentas do CI | GitHub Actions, `pytest` e `flake8`. |
| Persistência | Arquivo local JSON em `data/students.json`. |
| Resultados sociais medidos | Não há, no escopo técnico documentado, estudo de impacto ou medição de redução de reprovação/evasão. Esse resultado permanece como benefício esperado, não como efeito comprovado. |

---

## 11. REFERÊNCIAS E FONTES DE DADOS

1. **Organização das Nações Unidas (ONU).** *Goal 4: Quality Education* — descrição oficial das metas 4.3 e 4.4. Disponível em: <https://sdgs.un.org/goals/goal4>. Acesso em: 10 out. 2026.
2. **Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep).** *Censo da Educação Superior 2024 — apresentação de resultados*. Fonte para o número de matrículas em cursos de graduação. Disponível em: <https://download.inep.gov.br/educacao_superior/censo_superior/documentos/2024/apresentacao_censo_da_educacao_superior_2024.pdf>. Acesso em: 10 out. 2026.
3. **Inep.** *Indicadores de Trajetória da Educação Superior*. Disponível em: <https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/indicadores-de-trajetoria-da-educacao-superior>. Acesso em: 10 out. 2026.
4. **Repositório do EduGrade.** Código, testes automatizados e configuração de integração contínua. Disponível em: <https://github.com/vivoeasy100/calculadora_de_notas_academicas-/tree/feature/documentacao-ods4-Lucas>. Acesso em: 10 out. 2026.
5. **Arquivo de testes do projeto.** `tests/test_calculator.py`. Disponível em: <https://github.com/vivoeasy100/calculadora_de_notas_academicas-/blob/feature/documentacao-ods4-Lucas/tests/test_calculator.py>.
6. **Workflow de CI.** `.github/workflows/ci.yml`. Disponível em: <https://github.com/vivoeasy100/calculadora_de_notas_academicas-/blob/feature/documentacao-ods4-Lucas/.github/workflows/ci.yml>.
7. **Módulo de cálculo.** `src/calculator.py`. Disponível em: <https://github.com/vivoeasy100/calculadora_de_notas_academicas-/blob/feature/documentacao-ods4-Lucas/src/calculator.py>.
8. **Módulo de gerenciamento e persistência.** `src/manager.py`. Disponível em: <https://github.com/vivoeasy100/calculadora_de_notas_academicas-/blob/feature/documentacao-ods4-Lucas/src/manager.py>.

---
