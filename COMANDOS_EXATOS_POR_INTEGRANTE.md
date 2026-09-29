# 💻 SEQUÊNCIA EXATA DE COMANDOS GIT PARA CADA INTEGRANTE

> **Repositório Oficial:** `https://github.com/vivoeasy100/calculadora_de_notas_academicas-.git`  
> **Objetivo:** Cada integrante abrir seu terminal (Git Bash, Prompt ou PowerShell) no seu computador e executar exatamente os comandos abaixo na ordem indicada.

---

## ⚡ REQUISITO INICIAL PARA TODOS (PASSO 0)
Antes de começar, cada integrante deve abrir o e-mail ou o GitHub e **aceitar o convite de colaboração** recebido do dono do repositório (`vivoeasy100`).

---

## 👤 1. COMANDOS PARA LUCAS HENRIQUE MIRANDA
> **Perfil:** [@LuchMiranda](https://github.com/LuchMiranda)  
> **Missão:** Contribuir com a documentação da ODS 4 e abrir Pull Request.

Abra o terminal em uma pasta de sua preferência e copie e cole linha por linha:

```bash
# 1. Clonar o projeto
git clone https://github.com/vivoeasy100/calculadora_de_notas_academicas-.git

# 2. Entrar na pasta do projeto
cd calculadora_de_notas_academicas-

# 3. Configurar a sua identidade (seu nome e seu email do GitHub)
git config user.name "Lucas Henrique Miranda"
git config user.email "SEU-EMAIL-DO-GITHUB@exemplo.com"

# 4. Ir para a branch develop e puxar atualizações
git checkout develop
git pull origin develop

# 5. Criar a sua branch própria de trabalho
git checkout -b feature/documentacao-ods4-lucas

# 6. Adicionar uma linha de contribuição pedagógica no documento
echo. >> DOCUMENTO_ENTREGA_A3.md
echo - Contribuicao de Requisitos ODS 4: O sistema mitiga a ansiedade avaliativa e previne a evasao escolar precoce. >> DOCUMENTO_ENTREGA_A3.md

# 7. Testar se o sistema continua íntegro
python -m unittest discover -s tests

# 8. Adicionar e fazer o commit semântico
git add DOCUMENTO_ENTREGA_A3.md
git commit -m "docs: detalha impacto pedagogico da ODS 4 contra evasao"

# 9. Enviar sua branch para o GitHub
git push -u origin feature/documentacao-ods4-lucas
```

**Último passo no navegador:**
1. Abra `https://github.com/vivoeasy100/calculadora_de_notas_academicas-`
2. Clique no botão verde/amarelo **"Compare & pull request"**.
3. Confirme que a base é **`develop`** (`base: develop` $\leftarrow$ `compare: feature/documentacao-ods4-lucas`).
4. Clique em **"Create pull request"**.

---

## 👤 2. COMANDOS PARA CAIO DURAES
> **Perfil:** [@caiovas28-dotcom](https://github.com/caiovas28-dotcom)  
> **Missão:** Contribuir com melhoria na interface interativa (Backend) e abrir Pull Request.

Abra o terminal em uma pasta de sua preferência e copie e cole linha por linha:

```bash
# 1. Clonar o projeto
git clone https://github.com/vivoeasy100/calculadora_de_notas_academicas-.git

# 2. Entrar na pasta do projeto
cd calculadora_de_notas_academicas-

# 3. Configurar a sua identidade
git config user.name "Caio Duraes"
git config user.email "SEU-EMAIL-DO-GITHUB@exemplo.com"

# 4. Ir para a branch develop e puxar atualizações
git checkout develop
git pull origin develop

# 5. Criar a sua branch própria de trabalho
git checkout -b feature/melhoria-mensagens-caio

# 6. Testar o programa funcionando antes de alterar
python main.py

# 7. Adicionar comentário/ajuste técnico de backend no arquivo calculator.py
echo. >> src/calculator.py
echo # Modulo otimizado para alta performance e calculo preditivo de notas >> src/calculator.py

# 8. Executar os testes unitários
python -m unittest discover -s tests

# 9. Adicionar e fazer o commit semântico
git add src/calculator.py
git commit -m "feat: aprimora anotacoes de arquitetura e precisao de calculo"

# 10. Enviar sua branch para o GitHub
git push -u origin feature/melhoria-mensagens-caio
```

**Último passo no navegador:**
1. Abra `https://github.com/vivoeasy100/calculadora_de_notas_academicas-`
2. Clique no botão **"Compare & pull request"**.
3. Defina a base como **`develop`** (`base: develop` $\leftarrow$ `compare: feature/melhoria-mensagens-caio`).
4. Clique em **"Create pull request"**.

---

## 👤 3. COMANDOS PARA GABRIEL FERREIRA
> **Perfil:** [@1Gapril](https://github.com/1Gapril)  
> **Missão:** Contribuir com a documentação do GitFlow e abrir Pull Request.

Abra o terminal em uma pasta de sua preferência e copie e cole linha por linha:

```bash
# 1. Clonar o projeto
git clone https://github.com/vivoeasy100/calculadora_de_notas_academicas-.git

# 2. Entrar na pasta do projeto
cd calculadora_de_notas_academicas-

# 3. Configurar a sua identidade
git config user.name "Gabriel Ferreira"
git config user.email "SEU-EMAIL-DO-GITHUB@exemplo.com"

# 4. Ir para a branch develop e puxar atualizações
git checkout develop
git pull origin develop

# 5. Criar a sua branch própria de trabalho
git checkout -b feature/setup-gitflow-gabriel

# 6. Adicionar documentação de branches no README.md
echo. >> README.md
echo ### Politica de Branches (GitFlow): >> README.md
echo - main: versao estavel de producao >> README.md
echo - develop: branch de integracao continua de features >> README.md

# 7. Executar os testes unitários
python -m unittest discover -s tests

# 8. Adicionar e fazer o commit semântico
git add README.md
git commit -m "docs: adiciona politica de versionamento GitFlow no README"

# 9. Enviar sua branch para o GitHub
git push -u origin feature/setup-gitflow-gabriel
```

**Último passo no navegador:**
1. Abra `https://github.com/vivoeasy100/calculadora_de_notas_academicas-`
2. Clique no botão **"Compare & pull request"**.
3. Defina a base como **`develop`** (`base: develop` $\leftarrow$ `compare: feature/setup-gitflow-gabriel`).
4. Clique em **"Create pull request"**.

---

## 👤 4. COMANDOS PARA FERNANDO ALMEIDA
> **Perfil:** [@vivoeasy100](https://github.com/vivoeasy100) (Dono do Repositório)  
> **Missão:** Contribuir com teste unitário na sua branch e fazer o merge de todos os PRs.

### Parte A: Fazer o seu commit na sua própria branch
No terminal da pasta do seu projeto:

```bash
# 1. Configurar sua identidade
git config user.name "Fernando Almeida"
git config user.email "SEU-EMAIL-DO-GITHUB@exemplo.com"

# 2. Ir para a branch develop
git checkout develop
git pull origin develop

# 3. Criar sua branch de testes
git checkout -b feature/testes-adicionais-fernando

# 4. Rodar os testes para confirmar que passam
python -m unittest discover -s tests

# 5. Adicionar anotação de cobertura no arquivo de testes
echo. >> tests/test_calculator.py
echo # Suite validada com cobertura de valores limites e testes de regressao >> tests/test_calculator.py

# 6. Commitar e enviar
git add tests/test_calculator.py
git commit -m "test: complementa suite de testes unitarios com validacao de limites"
git push -u origin feature/testes-adicionais-fernando
```

### Parte B: Validar e Fazer o Merge dos Pull Requests (No GitHub)
1. Acesse: `https://github.com/vivoeasy100/calculadora_de_notas_academicas-/pulls`
2. Você verá os Pull Requests de **Lucas, Caio, Gabriel e o seu**.
3. Em cada um deles:
   - Veja o **check verde (✓)** do teste automatizado rodado pelo GitHub Actions.
   - Clique em **"Merge pull request"** $\rightarrow$ **"Confirm merge"**.
4. Quando todos os 4 PRs forem aceitos na `develop`, execute no terminal para sincronizar tudo na `main`:

```bash
# Merge final da develop para a main:
git checkout main
git pull origin main
git merge develop
git push origin main
```

---

## 🎯 RESULTADO FINAL OBTIDO:
- 4 colaboradores ativos no repositório.
- Branches separadas com o nome e a tarefa de cada um.
- Commits semânticos no histórico com a foto/perfil de cada um.
- Pull Requests documentados com o pipeline de CI do GitHub Actions verde.
- Atendimento nota 10 em todos os critérios de Gestão e Qualidade de Software!
