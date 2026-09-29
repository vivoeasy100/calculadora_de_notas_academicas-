# 📢 GUIA GERAL DO GRUPO: O QUE FOI FEITO & COMO PROCEDER
> **Trabalho A3 Prático – Gestão e Qualidade de Software (GQS)**  
> **Professor:** Daniel Henrique Matos de Paiva  
> **Tema:** EduGrade (Calculadora & Gestão de Notas Acadêmicas - ODS 4)  

---

## 📌 1. Visão Geral: O Que Foi Desenvolvido?

Para atender a **100% das exigências do professor** descritas no edital da A3, nós transformamos a ideia da calculadora acadêmica em um projeto de software profissional, completo e funcional.

O projeto conta com:
1. **Sistema em Python Funcional:** Permite simular notas ponderadas (A1, A2, etc.), diagnostica se o aluno está *Aprovado*, *Em Exame Final* ou *Reprovado*, calcula automaticamente quanto precisa tirar na prova final e salva o histórico em formato JSON.
2. **Boas Práticas de Engenharia (Clean Code):** Código altamente modular, sem repetições, com funções de responsabilidade única e tratamento rigoroso de erros (`try/catch`).
3. **Metodologia TDD (Test-Driven Development):** Suíte de testes unitários que valida todas as regras antes de rodar a aplicação.
4. **CI/CD Automatizado:** Pipeline pronto para o GitHub Actions que testa o código automaticamente a cada commit ou pull request.
5. **Documentação Acadêmica Completa:** Textos estruturados para a entrega no Word, slides e roteiro de fala para a apresentação e vídeo pitch.

---

## 👥 2. Divisão de Papéis e O que Cada Um Precisa Saber

A divisão foi alinhada com as habilidades propostas e o tamanho da equipe (4 integrantes):

```
       [Lucas]                 [Caio]               [Gabriel]             [Fernando]
Requisitos & ODS 4 ---> Dev & Arquitetura ---> GitFlow & Slides ---> QA, TDD & CI/CD
```

---

### 🔹 1. Lucas Henrique Miranda (RA: 325131396)
**Papel:** Introdução, Planejamento & Requisitos (Product Owner)  
* **O que você precisa estudar/fazer:**
  * Ler a seção 2 e 4 do arquivo [`DOCUMENTO_ENTREGA_A3.md`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/DOCUMENTO_ENTREGA_A3.md).
  * Entender a conexão com a **ODS 4 (Educação de Qualidade)**: nosso sistema ajuda o aluno a prever notas e evitar reprovação ou evasão escolar.
  * Na apresentação (2 a 3 min), você faz a abertura: cumprimenta o professor, introduz o grupo, contextualiza o problema e explica o escopo do EduGrade.

---

### 🔹 2. Caio Duraes (RA: 325132875)
**Papel:** Desenvolvimento & Arquitetura de Software (Backend Lead)  
* **O que você precisa estudar/fazer:**
  * Olhar como o código está organizado:
    * [`src/calculator.py`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/src/calculator.py): Lógica de cálculo, média ponderada, média aritmética e cálculo de nota necessária no exame.
    * [`src/exceptions.py`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/src/exceptions.py): Tratamento de erros customizados (ex: notas maiores que 10 ou menores que 0, pesos inválidos).
    * [`src/manager.py`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/src/manager.py): Salva e carrega os alunos no arquivo `data/students.json`.
    * [`main.py`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/main.py): Menu interativo no terminal.
  * Na apresentação (4 a 5 min), você compartilha a tela, roda o comando `python main.py` e demonstra o sistema funcionando ao vivo (selecionando as opções do menu).

---

### 🔹 3. Gabriel Ferreira (RA: 325140970)
**Papel:** Documentação, Versionamento & DevOps (GitFlow)  
* **O que você precisa estudar/fazer:**
  * Subir o projeto para o repositório do GitHub.
  * Garantir a criação das branches seguindo o padrão **GitFlow**:
    * `main`: versão final de entrega.
    * `develop`: branch onde as integrações são unificadas.
    * `feature/...`: branches de cada funcionalidade.
  * Verificar os **commits semânticos** (ex: `feat: add grade calculation`, `test: add unit tests`, `docs: update readme`).
  * Montar os slides em PowerPoint a partir do roteiro pronto em [`ROTEIRO_APRESENTACAO_A3.md`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/ROTEIRO_APRESENTACAO_A3.md).

---

### 🔹 4. Fernando Almeida (RA: 326132695)
**Papel:** Qualidade de Software, Testes Unitários & CI/CD (QA Engineer)  
* **O que você precisa estudar/fazer:**
  * Olhar o arquivo [`tests/test_calculator.py`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/tests/test_calculator.py).
  * Executar os testes no terminal com o comando:
    ```bash
    python -m unittest discover -s tests
    ```
  * Entender o arquivo [`.github/workflows/ci.yml`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/.github/workflows/ci.yml): é o pipeline que roda no GitHub toda vez que alguém envia código, garantindo que nenhum bug chegue na branch principal.
  * Na apresentação (3 a 4 min), você roda os testes ao vivo para provar ao professor que todas as 10 verificações passam com sucesso.

---

## 📂 3. Mapa dos Arquivos do Projeto

Aqui está a lista do que existe no projeto para ninguém se perder:

| Arquivo | Para Que Serve? |
| :--- | :--- |
| **`INSTRUCOES_DO_GRUPO.md`** *(este arquivo)* | Guia explicativo passo a passo para todos os membros do grupo. |
| **`DOCUMENTO_ENTREGA_A3.md`** | Minuta completa já redigida. Basta copiar e colar no Word oficial para entrega. |
| **`ROTEIRO_APRESENTACAO_A3.md`** | Roteiro com falas sugeridas para a apresentação de 10 a 15 min e para o vídeo Pitch de 5 min. |
| **`PLANO_DE_EXECUCAO_A3.md`** | Detalhes sobre os critérios de pontuação do professor e matriz de papéis. |
| **`README.md`** | Página inicial técnica do GitHub explicando como rodar o projeto. |
| **`main.py`** | Aplicação principal interativa que roda no terminal. |
| **`src/`** | Código-fonte das regras de negócio, persistência e tratamento de erros. |
| **`tests/`** | Testes automatizados (TDD). |
| **`.github/workflows/ci.yml`** | Configuração do pipeline de integração contínua (CI/CD). |

---

## 💻 4. Como Qualquer Integrante Pode Rodar o Projeto

### Passo 1: Abrir o Terminal na pasta do projeto
Certifique-se de que o Python 3 está instalado no computador.

### Passo 2: Executar os Testes Unitários
```bash
python -m unittest discover -s tests
```
*Resultado esperado:* Ver 10 pontinhos (`..........`) e a mensagem `OK`.

### Passo 3: Executar o Programa
```bash
python main.py
```
*No menu que aparecer:*
- **Opção 1:** Mostra os 4 integrantes e seus respectivos papéis.
- **Opção 2:** Faz uma simulação rápida de notas (A1 e A2) com pesos.
- **Opção 3:** Cadastra um aluno, lança notas e gera o boletim.
- **Opção 4:** Pré-carrega os 4 integrantes já com notas reais de exemplo.

---

## 📅 5. Próximos Passos e Prazos

1. **Subir no GitHub:** Criar o repositório da equipe e subir este código com as branches do GitFlow.
2. **Gerar o Word:** Copiar o conteúdo de [`DOCUMENTO_ENTREGA_A3.md`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/DOCUMENTO_ENTREGA_A3.md) para o modelo institucional da faculdade (Entrega até **16/10/2026**).
3. **PowerPoint:** Montar os slides com base nos 4 blocos de [`ROTEIRO_APRESENTACAO_A3.md`](file:///e:/Trabalho%20A3%20-%20Pr%C3%A1tico/ROTEIRO_APRESENTACAO_A3.md).
4. **Gravação do Pitch (5 min):** Gravar a demonstração e publicar como vídeo não-listado no YouTube.
5. **Feedbacks com o Professor:**
   - Feedback 01: semana 19/10
   - Feedback 02: semana 09/11
   - Apresentação Final / Expo UNA: semana 23/11
