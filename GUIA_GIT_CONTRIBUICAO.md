# 🚀 GUIA DE CONTRIBUIÇÃO GIT, BRANCHES E PULL REQUESTS
> **Trabalho A3 – Gestão e Qualidade de Software**  
> **Objetivo:** Garantir que **Lucas, Caio, Gabriel e Fernando** tenham commits reais em suas contas no GitHub, sigam o padrão **GitFlow** e realizem **Pull Requests com validação de CI/CD** para tirar nota máxima no critério de versionamento.

---

## 👥 1. O Que Cada Integrante Fará (Missão Individual no Git)

Cada membro do grupo criará sua própria branch a partir da `develop`, fará uma contribuição legítima dentro do seu papel, enviará para o GitHub e abrirá um **Pull Request (PR)** para juntar à `develop` (Git Merge):

| Integrante | Papel | Nome da Branch a Criar | Arquivo que irá editar/contribuir | Tipo de Commit |
| :--- | :--- | :--- | :--- | :--- |
| **Lucas Henrique Miranda** | Requisitos & ODS 4 | `feature/documentacao-ods4-lucas` | `DOCUMENTO_ENTREGA_A3.md` (ajustar introdução/ODS) | `docs: detalha justificativa pedagogica e ODS 4` |
| **Caio Duraes** | Backend Lead | `feature/melhoria-mensagens-caio` | `src/calculator.py` ou `main.py` (comentários/textos) | `feat: aprimora interface de feedback de notas` |
| **Gabriel Ferreira** | DevOps & Git | `feature/setup-gitflow-gabriel` | `README.md` (inserir tabela com links dos membros) | `docs: documenta fluxo de trabalho GitFlow` |
| **Fernando Almeida** | QA & Testes TDD | `feature/testes-adicionais-fernando`| `tests/test_calculator.py` (adicionar novo teste) | `test: adiciona validacao de borda para nota zero` |

---

## 🛠️ 2. Passo a Passo Para Cada Integrante Fazer no Seu Computador

### Passo 0: Adicionar os Integrantes como Colaboradores no GitHub (Ação do Dono do Repositório)
1. O dono do repositório acessa:  
   👉 `https://github.com/vivoeasy100/calculadora_de_notas_academicas-/settings/access`
2. Clica em **"Add people"**.
3. Digita o nome de usuário ou e-mail do GitHub de **Lucas, Caio e Fernando**.
4. Cada um deles deve aceitar o convite que chegar no seu e-mail ou na notificação do GitHub.

---

### Passo 1: Clonar o Repositório e Configurar a Identidade
No terminal de cada integrante:
```bash
# 1. Clonar o projeto
git clone https://github.com/vivoeasy100/calculadora_de_notas_academicas-.git

# 2. Entrar na pasta
cd calculadora_de_notas_academicas-

# 3. Identificar o seu nome e email no Git (MUITO IMPORTANTE para o seu nome aparecer no GitHub!)
git config user.name "Seu Nome Completo"
git config user.email "seu-email-cadastrado-no-github@exemplo.com"
```

---

### Passo 2: Ir para a branch `develop` e criar a sua branch individual
Seguindo o GitFlow, ninguém desenvolve direto na `main`:
```bash
# Baixar as últimas atualizações
git fetch origin

# Mudar para a branch develop
git checkout develop
git pull origin develop

# Criar a sua branch da sua tarefa (veja a tabela da seção 1 para saber a sua)
# Exemplo do Lucas:
git checkout -b feature/documentacao-ods4-lucas

# Exemplo do Caio:
# git checkout -b feature/melhoria-mensagens-caio

# Exemplo do Gabriel:
# git checkout -b feature/setup-gitflow-gabriel

# Exemplo do Fernando:
# git checkout -b feature/testes-adicionais-fernando
```

---

### Passo 3: Fazer a Alteração no Arquivo Atribuído
Abra o arquivo designado no VS Code ou bloco de notas, faça uma pequena melhoria real:

* **Exemplo do Fernando (`tests/test_calculator.py`):**
  Adicionar no final da classe `TestGradeCalculator`:
  ```python
  def test_grade_zero_is_valid(self):
      """Garante que a nota zero é válida e calculada corretamente."""
      mean = GradeCalculator.calculate_arithmetic_mean([0.0, 10.0])
      self.assertEqual(mean, 5.0)
  ```

* **Exemplo do Lucas (`DOCUMENTO_ENTREGA_A3.md`):**
  Adicionar uma linha detalhando que a calculadora visa diminuir o estresse antes da prova final.

* **Exemplo do Caio (`main.py`):**
  Melhorar uma frase do menu ou adicionar seu nome na tela de créditos.

---

### Passo 4: Validar os Testes Localmente Antes de Subir
Antes de commitar, execute o comando de testes para garantir que nada quebrou:
```bash
python -m unittest discover -s tests
```
*Se aparecer `OK`, o código está perfeito para subir!*

---

### Passo 5: Criar o Commit Semântico e Enviar a Branch
```bash
# Adicionar o arquivo alterado
git add .

# Criar o commit semântico (use o prefixo feat, docs ou test)
git commit -m "docs: detalha justificativa pedagogica da ODS 4"

# Enviar a branch para o GitHub
git push -u origin NOME-DA-SUA-BRANCH
```
*(Substitua `NOME-DA-SUA-BRANCH` pelo nome da branch que você criou no Passo 2).*

---

## 🔀 3. Como Fazer o Git Merge e Validar pelo GitHub (Pull Request)

O professor avalia a colaboração e a **Qualidade com CI/CD**. Fazer o Merge pelo **Pull Request** no navegador é a melhor prática da indústria:

### 1. Abrir o Pull Request (PR)
1. No navegador, acesse o GitHub:  
   👉 `https://github.com/vivoeasy100/calculadora_de_notas_academicas-`
2. O GitHub exibirá um botão amarelo: **"Compare & pull request"**. Clique nele.
3. **MUITO IMPORTANTE:** Selecione como branch de destino:  
   `base: develop`  <---  `compare: feature/sua-branch`
4. Escreva no título o que você fez (ex: `feat: adiciona validacao de nota zero`).
5. Clique em **"Create pull request"**.

### 2. A Validação Automática do CI/CD (Garantia da Qualidade)
- Assim que o PR for aberto, o **GitHub Actions** iniciará a verificação automaticamente (arquivo `.github/workflows/ci.yml`).
- Você verá um ícone amarelo girando: *"test / Python CI Pipeline"*.
- Após cerca de 20 segundos, o ícone ficará **VERDE com um check (✓)**:  
  *Isso comprova para o professor que o CI rodou e validou os testes de qualidade do código daquele integrante!*

### 3. Fazer o Merge (Integrar o Código)
1. Com o teste verde aprovado, clique no botão verde **"Merge pull request"**.
2. Clique em **"Confirm merge"**.
3. Pronto! O código agora está integrado na branch `develop`.

---

## 🏁 4. Fechamento Final do Ciclo GitFlow (Merge para a `main`)

Quando todos os 4 integrantes tiverem feito seus Pull Requests e merges na `develop`, o líder do projeto ou o Gabriel fará o merge final da `develop` para a `main`:

```bash
git checkout main
git pull origin main
git merge develop
git push origin main
```

---

## 📸 5. O que Printar para a Apresentação e Relatório
Para garantir nota máxima no critério **"Versionamento do Software (GitFlow, Git Semântico)"**:
1. **Aba Network/Insights do GitHub:** Mostrando o desenho das branches se cruzando (*Network Graph*).
2. **Aba Pull Requests:** Mostrando os PRs criados e mergeados pelos 4 integrantes.
3. **Aba Actions:** Mostrando todos os checks verdes de CI passando em cada contribuição.
4. **Histórico de Commits:** Mostrando as fotos/nomes dos 4 integrantes com mensagens no formato `feat:`, `docs:`, `test:`.
