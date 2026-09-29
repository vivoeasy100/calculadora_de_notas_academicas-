# 📊 STATUS DO PROJETO A3: O QUE JÁ ESTÁ PRONTO E O QUE FALTA FAZER

> **Disciplina:** Gestão e Qualidade de Software (GQS)  
> **Professor:** Daniel Henrique Matos de Paiva  
> **Data Limite das Entregas:** 16/10/2026  
> **Projeto:** EduGrade (Calculadora & Gestão Acadêmica - ODS 4)  

---

## 🟢 1. O QUE JÁ ESTÁ 100% PRONTO (PARTE TÉCNICA E CONTEÚDO)

Toda a parte técnica, lógica, arquitetura, testes e documentação textual **já foram totalmente construídos e validados** dentro desta pasta. Não é necessário programar mais nada:

- [x] **Código da Aplicação em Python:** Completo, funcional e sem erros.
  - Lógica de médias ponderadas e aprovação institucional ([`src/calculator.py`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/src/calculator.py)).
  - Tratamento de exceções e erros de entrada com *Clean Code* ([`src/exceptions.py`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/src/exceptions.py)).
  - Persistência e salvamento em JSON ([`src/manager.py`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/src/manager.py)).
  - Menu interativo para apresentação com os 4 integrantes ([`main.py`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/main.py)).
- [x] **Qualidade & Metodologia TDD:** 10 testes unitários automatizados cobrindo todos os cenários, executando com 100% de sucesso ([`tests/test_calculator.py`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/tests/test_calculator.py)).
- [x] **Pipeline de CI/CD:** Configuração de integração contínua pronta para o GitHub Actions ([`.github/workflows/ci.yml`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/.github/workflows/ci.yml)).
- [x] **Vínculo com ODS:** 100% alinhado com a **ODS 4 (Educação de Qualidade)** da ONU.
- [x] **Texto Completo do Documento da Entrega:** Já redigido com o problema real, solução, ODS e boas práticas ([`DOCUMENTO_ENTREGA_A3.md`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/DOCUMENTO_ENTREGA_A3.md)).
- [x] **Roteiro dos Slides e do Pitch:** Minuto a minuto pronto para a fala de cada um ([`ROTEIRO_APRESENTACAO_A3.md`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/ROTEIRO_APRESENTACAO_A3.md)).

---

## 🟡 2. O QUE FALTA O GRUPO FAZER (AÇÕES PRÁTICAS PARA ENTREGA)

Para enviar no portal da faculdade, restam apenas **4 tarefas operacionais simples**. Abaixo está o que deve ser feito e o responsável:

### 📝 Tarefa 1: Gerar o Documento Word Oficial (.docx)
* **Responsável:** **Lucas Henrique Miranda** (apoio: todos)
* **O que fazer:**
  1. Abrir o Microsoft Word (usando o template/capa padrão da faculdade).
  2. Copiar todo o texto do arquivo [`DOCUMENTO_ENTREGA_A3.md`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/DOCUMENTO_ENTREGA_A3.md) e colar no Word.
  3. Conferir os nomes, RAs e salvar como arquivo Word (.docx ou PDF).
* **Prazo Limite:** 16/10/2026.

---

### 🐙 Tarefa 2: Subir o Repositório no GitHub
* **Responsável:** **Gabriel Ferreira**
* **O que fazer:**
  1. Criar um repositório público ou privado no GitHub (ex: `a3-qualidade-software-edugrade`).
  2. Subir todos os arquivos desta pasta para o repositório.
  3. Criar as branches no padrão **GitFlow**:
     * Branch `main`
     * Branch `develop`
     * Branch `feature/calculadora-notas`
  4. Garantir que a aba "Actions" no GitHub execute o pipeline verde do arquivo `.github/workflows/ci.yml`.
  5. Copiar o link do repositório para colocar no relatório e na entrega.
* **Prazo Limite:** 16/10/2026.

---

### 📊 Tarefa 3: Montar os Slides no PowerPoint (.pptx)
* **Responsável:** **Gabriel Ferreira** e **Lucas Henrique Miranda**
* **O que fazer:**
  1. Criar uma apresentação de 6 a 8 slides simples baseados no roteiro pronto em [`ROTEIRO_APRESENTACAO_A3.md`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/ROTEIRO_APRESENTACAO_A3.md):
     * Slide 1: Capa (Integrantes, RAs, Professor, Matéria e Tema).
     * Slide 2: Problema do mundo real e ODS 4 (Educação de Qualidade).
     * Slide 3: A Solução EduGrade (Objetivos e Funcionalidades).
     * Slide 4: Arquitetura, Clean Code e Tratamento de Erros.
     * Slide 5: Versionamento GitFlow e Commits Semânticos.
     * Slide 6: Garantia da Qualidade, TDD e Pipeline CI/CD.
* **Prazo Limite:** 16/10/2026.

---

### 🎥 Tarefa 4: Gravar o Vídeo Pitch de 5 Minutos (YouTube)
* **Responsável:** **Todos os 4 Integrantes**
* **O que fazer:**
  1. O grupo entra em uma chamada (Google Meet, Teams ou Discord).
  2. Coloca para gravar a chamada.
  3. Segue estritamente a divisão de tempo (cerca de 1 min e pouco para cada um):
     * **Lucas:** Abertura, problema e ODS 4.
     * **Caio:** Mostra a tela rodando `python main.py` e simulando as notas.
     * **Gabriel:** Mostra o GitHub com as branches e commits semânticos.
     * **Fernando:** Roda os testes `python -m unittest discover -s tests` e mostra o pipeline de CI.
  4. Postar o vídeo no YouTube no modo **Não Listado** (Unlisted) e guardar o link.
* **Prazo:** Antes da apresentação final.

---

## 📅 3. CALENDÁRIO OFICIAL DAS ETAPAS

| Data / Semana | Evento | O que apresentar / entregar |
| :--- | :--- | :--- |
| **16/10/2026** | **Entrega Oficial Inicial** | Envio do Word, Link do GitHub e PowerPoint no sistema |
| **Semana 19/10** | **Feedback 01** | Primeira checagem com o Professor Daniel |
| **Semana 09/11** | **Feedback 02** | Segunda checagem e ajustes finos |
| **Semana 23/11** | **Apresentação Final / Expo UNA** | Apresentação ao vivo da equipe (10 a 15 min) |

---

## 💡 RESUMO RÁPIDO PARA O GRUPO
> **"Falta programar algo?"**  
> 👉 **Não.** Toda a programação, os testes unitários e a documentação técnica estão prontos.  
> 
> **"O que temos que fazer agora?"**  
> 👉 Apenas a parte burocrática: formatar no Word, subir no GitHub, criar os slides e gravar o vídeo pitch de 5 minutos!
