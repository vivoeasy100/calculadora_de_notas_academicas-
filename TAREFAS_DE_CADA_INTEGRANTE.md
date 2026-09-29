# 📋 TAREFAS INDIVIDUAIS DO GRUPO (CHECKLIST NOMINAL)
> **Trabalho A3 – Gestão e Qualidade de Software**  
> **Professor:** Daniel Henrique Matos de Paiva  
> **Repositório:** [https://github.com/vivoeasy100/calculadora_de_notas_academicas-](https://github.com/vivoeasy100/calculadora_de_notas_academicas-)  
> **Prazo das Entregas:** 16/10/2026  

---

## 🎯 RESUMO EXECUTIVO
Toda a codificação em Python, os testes unitários (TDD), o pipeline de CI/CD e os textos base **já estão prontos e funcionando no repositório**.

Abaixo está a **lista exata do que cada integrante precisa fazer**, passo a passo, para garantir a sua participação prática, seus commits no GitHub e o sucesso na apresentação:

---

## 👤 1. LUCAS HENRIQUE MIRANDA
* **RA:** `325131396`
* **GitHub:** [@LuchMiranda](https://github.com/LuchMiranda)
* **Papel no Projeto:** Product Owner & Engenharia de Requisitos (ODS 4)

### Suas Tarefas Práticas:
1. **Aceitar o convite no GitHub:** Entrar no seu e-mail ou no GitHub e aceitar o convite de colaborador do repositório.
2. **Fazer a sua contribuição no Git (Branch individual):**
   * No seu terminal, puxe a branch develop e crie a sua:
     ```bash
     git checkout develop
     git pull origin develop
     git checkout -b feature/documentacao-ods4-lucas
     ```
   * Abra o arquivo `DOCUMENTO_ENTREGA_A3.md`, adicione ou refine um parágrafo sobre a **ODS 4 (Educação de Qualidade)** e salve.
   * Faça o commit e envie:
     ```bash
     git add .
     git commit -m "docs: aprimora justificativa da ODS 4 para retencao estudantil"
     git push -u origin feature/documentacao-ods4-lucas
     ```
   * Abra o **Pull Request** no GitHub apontando para a branch `develop`.
3. **Gerar o Documento Word Oficial:**
   * Abrir o modelo Word oficial com a capa da faculdade.
   * Copiar o conteúdo pronto de `DOCUMENTO_ENTREGA_A3.md`, colar no Word, conferir nomes/RAs e salvar o `.docx` para entrega.
4. **Na Apresentação (3 minutos):**
   * Você abre a apresentação cumprimentando o professor Daniel e os colegas.
   * Explica o problema real da evasão de alunos, a dificuldade de cálculo de médias ponderadas e o vínculo direto com a **ODS 4**.

---

## 👤 2. CAIO DURAES
* **RA:** `325132875`
* **GitHub:** [@caiovas28-dotcom](https://github.com/caiovas28-dotcom)
* **Papel no Projeto:** Desenvolvedor Backend & Arquitetura

### Suas Tarefas Práticas:
1. **Aceitar o convite no GitHub:** Confirmar o convite de colaborador no GitHub.
2. **Fazer a sua contribuição no Git (Branch individual):**
   * No terminal:
     ```bash
     git checkout develop
     git pull origin develop
     git checkout -b feature/melhoria-mensagens-caio
     ```
   * Abra o arquivo `main.py` e adicione ou ajuste uma mensagem no console para o usuário (ex: no cabeçalho ou nas mensagens de aprovação/exame) e salve.
   * Faça o commit e envie:
     ```bash
     git add .
     git commit -m "feat: refina mensagens de retorno ao usuario na CLI"
     git push -u origin feature/melhoria-mensagens-caio
     ```
   * Abra o **Pull Request** no GitHub apontando para a branch `develop`.
3. **Entender e Testar o Código no Computador:**
   * Rodar no terminal: `python main.py` e testar as opções do menu (simulação rápida, carregar integrantes, etc.).
4. **Na Apresentação (4 a 5 minutos):**
   * Você compartilha a tela e demonstra o sistema funcionando ao vivo.
   * Mostra o cálculo de notas, o que acontece quando o aluno fica de recuperação (mostrando a nota necessária no exame) e simula uma nota inválida (ex: 15) para mostrar o **Tratamento de Exceções (`try/catch`)** funcionando sem quebrar.

---

## 👤 3. GABRIEL FERREIRA
* **RA:** `325140970`
* **GitHub:** [@1Gapril](https://github.com/1Gapril)
* **Papel no Projeto:** DevOps, Versionamento (GitFlow) & Apresentação

### Suas Tarefas Práticas:
1. **Aceitar o convite no GitHub:** Confirmar o convite de colaborador no GitHub.
2. **Fazer a sua contribuição no Git (Branch individual):**
   * No terminal:
     ```bash
     git checkout develop
     git pull origin develop
     git checkout -b feature/setup-gitflow-gabriel
     ```
   * Abra o arquivo `README.md`, verifique/adicione uma breve nota sobre o padrão de branches no final e salve.
   * Faça o commit e envie:
     ```bash
     git add .
     git commit -m "docs: detalha especificacoes das branches do GitFlow"
     git push -u origin feature/setup-gitflow-gabriel
     ```
   * Abra o **Pull Request** no GitHub apontando para a branch `develop`.
3. **Montar os Slides em PowerPoint (.pptx):**
   * Criar uma apresentação de 6 a 8 slides seguindo os tópicos divididos no arquivo `ROTEIRO_APRESENTACAO_A3.md`.
4. **Na Apresentação (3 minutos):**
   * Você explica como o repositório foi organizado no GitHub.
   * Mostra as branches do GitFlow (`main`, `develop`, `feature/*`) e os commits semânticos (`feat:`, `docs:`, `test:`).

---

## 👤 4. FERNANDO ALMEIDA
* **RA:** `326132695`
* **GitHub:** [@vivoeasy100](https://github.com/vivoeasy100)
* **Papel no Projeto:** Garantia da Qualidade, TDD & CI/CD (QA Engineer)

### Suas Tarefas Práticas:
1. **Gestão do Repositório (Dono):**
   * Garantir que Lucas, Caio e Gabriel foram adicionados em `Settings > Collaborators`.
   * Realizar os merges dos Pull Requests que a equipe abrir no GitHub.
2. **Fazer a sua contribuição no Git (Branch individual de Testes):**
   * No terminal:
     ```bash
     git checkout develop
     git pull origin develop
     git checkout -b feature/testes-adicionais-fernando
     ```
   * Abra o arquivo `tests/test_calculator.py` e adicione um novo método de teste unitário (ex: testar nota zero com sucesso).
   * Verifique se todos os testes passam: `python -m unittest discover -s tests`.
   * Faça o commit e envie:
     ```bash
     git add .
     git commit -m "test: adiciona teste unitario para valor limite de nota zero"
     git push -u origin feature/testes-adicionais-fernando
     ```
   * Abra o Pull Request para `develop` e faça o merge após a validação do CI.
3. **Na Apresentação (3 a 4 minutos):**
   * Você apresenta a metodologia **TDD (Test-Driven Development)** e o **Clean Code**.
   * Executa os testes unitários ao vivo no terminal (`python -m unittest discover -s tests`) mostrando os testes passando em milissegundos.
   * Abre a aba **Actions** do GitHub e mostra o pipeline do arquivo `.github/workflows/ci.yml` rodando e aprovado com check verde.

---

## 👥 TAREFA CONJUNTA (TODOS OS 4 JUNTOS)
* **Gravação do Vídeo Pitch de 5 minutos (YouTube):**
  * Entrar em uma chamada (Google Meet, Discord ou Teams).
  * Gravar a tela e cada integrante falar a sua parte (1 minuto e pouco cada) seguindo o cronômetro de `ROTEIRO_APRESENTACAO_A3.md`.
  * Subir o vídeo no YouTube no modo "Não Listado" e guardar o link.
