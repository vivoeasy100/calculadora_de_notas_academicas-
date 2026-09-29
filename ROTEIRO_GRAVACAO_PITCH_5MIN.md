# 🎬 ROTEIRO DE GRAVAÇÃO DO VÍDEO PITCH (5 MINUTOS - YOUTUBE)
> **Trabalho A3 – Gestão e Qualidade de Software**  
> **Tema:** EduGrade - Calculadora de Notas e Gestão Acadêmica (ODS 4)  
> **Professor:** Daniel Henrique Matos de Paiva  
> **Duração Total:** 05:00 minutos cravados  

---

## 💡 DICAS RÁPIDAS PARA A GRAVAÇÃO
1. **Onde gravar:** Abram uma chamada no **Google Meet** ou **Discord**.
2. **Câmeras:** Se possível, liguem as webcams (ou mostrem as fotos dos integrantes).
3. **Compartilhamento de Tela:** Uma pessoa (ex: Fernando ou Caio) pode deixar a tela compartilhada enquanto cada um fala na sua vez.
4. **YouTube:** Ao subir no YouTube, coloquem o título `A3 GQS - EduGrade - Calculadora Acadêmica` e configurem a visibilidade como **"Não Listado"** (Unlisted).

---

## ⏱️ CRONOGRAMA MINUTO A MINUTO (O QUE CADA UM FALA)

---

### 🟢 MINUTO 00:00 até 01:10 — ABERTURA E ODS 4
🎤 **Quem fala:** **Lucas Henrique Miranda (RA: 325131396)**  
🖥️ **O que mostrar na tela:** Slide 1 e 2 (Capa com nomes/RAs e slide da ODS 4).

> **Texto da Fala:**
> *"Olá professor Daniel e colegas! Somos a equipe de Gestão e Qualidade de Software composta por mim, Lucas Miranda, o Caio Duraes, o Gabriel Ferreira e o Fernando Almeida.*
>
> *O nosso projeto é o **EduGrade**, uma solução voltada para resolver uma dor real de milhares de universitários: a falta de visibilidade clara sobre o cálculo de médias ponderadas, notas mínimas e a pontuação necessária no exame final para evitar a reprovação.*
>
> *Nosso projeto está diretamente conectado com a **ODS 4 da ONU – Educação de Qualidade**, atuando como uma ferramenta preventiva contra a desmotivação e a evasão acadêmica através da transparência pedagógica.*
>
> *Agora o Caio vai demonstrar a aplicação funcionando na prática."*

---

### 🟢 MINUTO 01:10 até 02:40 — DEMONSTRAÇÃO DO SOFTWARE (RODANDO AO VIVO)
🎤 **Quem fala:** **Caio Duraes (RA: 325132875)**  
🖥️ **O que mostrar na tela:** Terminal rodando `python main.py`.

> **Texto da Fala:**
> *(Enquanto digita `python main.py` no terminal e o menu aparece):*
> *"Obrigado, Lucas! O nosso sistema foi desenvolvido em Python, aplicando princípios rigorosos de **Clean Code** e separação de responsabilidades.*
>
> *(Seleciona a Opção 4 no menu):*
> *Aqui na Opção 4, nós pré-carregamos a nossa própria equipe no banco de dados JSON para demonstração, onde cada disciplina armazena suas avaliações.*
>
> *(Seleciona a Opção 2 no menu):*
> *Agora demonstrando o cálculo preditivo: se um aluno tira 4.0 na A1 com peso 0.4 e 4.5 na A2 com peso 0.6, o sistema calcula a média de 4.30 e imediatamente diagnostica a situação como 'RECUPERAÇÃO', informando exatamente quanto ele precisa tirar na prova final.*
>
> *(Digita uma nota inválida, como 15 ou uma letra):*
> *E cumprindo o critério de **Tratamento de Erros (`try/catch`)**, se o usuário digitar uma nota fora da faixa de 0 a 10 ou caracteres inválidos, o sistema intercepta a exceção através da nossa classe customizada `InvalidGradeError`, sem quebrar a execução.*
>
> *Passo agora para o Gabriel apresentar o nosso versionamento."*

---

### 🟢 MINUTO 02:40 até 03:50 — VERSIONAMENTO GITFLOW E COMMITS SEMÂNTICOS
🎤 **Quem fala:** **Gabriel Ferreira (RA: 325140970)**  
🖥️ **O que mostrar na tela:** O repositório no GitHub (`vivoeasy100/calculadora_de_notas_academicas-`), aba de Branches e aba de Commits.

> **Texto da Fala:**
> *"Obrigado, Caio! Para atender a todas as boas práticas de gestão de configuração, estruturamos o nosso repositório seguindo rigorosamente o padrão **GitFlow**.*
>
> *(Mostrando a aba de branches no GitHub):*
> *Temos a branch `main` destinada à versão final estável, a branch `develop` onde integramos todas as funcionalidades, e branches do tipo `feature/` criadas para cada membro da equipe desenvolver sua parte de forma isolada.*
>
> *(Mostrando o histórico de commits):*
> *Além disso, adotamos o padrão de **Commits Semânticos**, utilizando prefixos como `feat:`, `docs:`, `test:` e `refactor:`, facilitando a rastreabilidade e a leitura do histórico do projeto.*
>
> *Agora o Fernando vai explicar como garantimos a qualidade através do TDD e da integração contínua."*

---

### 🟢 MINUTO 03:50 até 05:00 — QUALIDADE, TDD E PIPELINE CI/CD
🎤 **Quem fala:** **Fernando Almeida (RA: 326132695)**  
🖥️ **O que mostrar na tela:** Terminal rodando `python -m unittest discover -s tests` e depois a aba **Actions** do GitHub (check verde).

> **Texto da Fala:**
> *"Obrigado, Gabriel! Como parte essencial da disciplina de Gestão e Qualidade de Software, nós adotamos a metodologia **TDD (Test-Driven Development)**.*
>
> *(Executa no terminal: `python -m unittest discover -s tests`):*
> *Como vocês podem ver na tela, temos uma suíte completa com 10 testes unitários cobrindo cálculos de médias, validações de limites, notas zero e tratamento de exceções. Todos os 10 testes passam com 100% de sucesso em milissegundos.*
>
> *(Muda para a aba 'Actions' no GitHub):*
> *Para fechar com chave de ouro, configuramos um pipeline de **CI/CD** com **GitHub Actions** através do nosso arquivo `ci.yml`. A cada commit ou Pull Request aberto na `develop` ou `main`, o robô do GitHub roda automaticamente a análise estática e todos os testes unitários, garantindo que nenhum código com defeito entre em produção.*
>
> *Com isso, entregamos um projeto robusto, testado e com alto padrão de qualidade de software. Muito obrigado a todos!"*

---

## 🚀 PASSO A PASSO FINAL PARA O GRUPO GRAVAR (15 MINUTOS):
1. Marquem um horário no Meet ou Discord.
2. O Fernando compartilha a tela com o terminal e o GitHub abertos.
3. Coloquem um cronômetro na mão e cada um lê o seu texto do roteiro acima.
4. Salvem o vídeo, subam no YouTube e coloquem o link no documento Word e no relatório da Expo UNA.
