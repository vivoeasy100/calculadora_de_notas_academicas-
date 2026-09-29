# ROTEIRO DE APRESENTAÇÃO E VÍDEO PITCH (TRABALHO A3)

## 🎤 1. ROTEIRO PARA APRESENTAÇÃO FINAL (10 A 15 MINUTOS)

### Bloco 1: Abertura e Contexto (3 minutos)
**Responsável:** **Lucas Henrique Miranda (RA: 325131396)**
- **Abertura:** Cumprimentar o professor Daniel e os colegas de classe.
- **Apresentação da Equipe:** Nome e RA dos 4 integrantes.
- **O Problema do Mundo Real:** Explicar a dor dos estudantes com fórmulas de notas complexas, prazos e a falta de visibilidade sobre as notas necessárias para aprovação.
- **Vínculo com a ODS 4 (Educação de Qualidade):** Como a aplicação combate a ansiedade e previne a evasão universitária.
- **Escopo e Requisitos:** Apresentação da proposta do sistema EduGrade.

### Bloco 2: Arquitetura e Demonstração ao Vivo do Sistema (4 a 5 minutos)
**Responsável:** **Caio Duraes (RA: 325132875)**
- **A Solução na Prática:** Abrir o terminal e rodar `python main.py`.
- **Demonstração:**
  - Opção 4: Carregar os 4 integrantes do grupo no sistema ao vivo.
  - Opção 2: Simular uma nota de aluno em situação de exame final (mostrando o cálculo automático de quanto ele precisa tirar).
  - Testar um erro intencional (digitar uma nota `15` ou texto) para evidenciar o **Tratamento de Exceções (`try/catch`)** funcionando perfeitamente sem quebrar o programa.
- **Arquitetura & Clean Code:** Explicar rapidamente a separação em `src/calculator.py`, `src/manager.py` e `src/exceptions.py`.

### Bloco 3: Gestão de Configuração e Versionamento GitFlow (3 minutos)
**Responsável:** **Gabriel Ferreira (RA: 325140970)**
- **Padrão GitFlow:** Explicar as branches utilizadas (`main`, `develop`, `feature/*`).
- **Commits Semânticos:** Mostrar o histórico de commits seguindo a convenção (`feat:`, `fix:`, `test:`, `docs:`).
- **Colaboração em Equipe:** Como o GitHub foi utilizado para sincronizar as tarefas de todos os 4 membros do grupo.

### Bloco 4: Garantia da Qualidade, TDD e CI/CD (3 a 4 minutos)
**Responsável:** **Fernando Almeida (RA: 326132695)**
- **TDD (Test-Driven Development):** Explicar como os testes unitários foram criados para guiar as regras de cálculo e evitar regressões.
- **Execução dos Testes ao Vivo:** Rodar no terminal `python -m unittest discover -s tests` e mostrar os 10 testes passando em milissegundos.
- **Pipeline de Integração Contínua (CI):** Exibir o arquivo `.github/workflows/ci.yml` configurado no GitHub Actions, garantindo que nenhum código quebrado vá para a branch principal.
- **Conclusão:** Agradecimentos e encerramento.

---

## 📹 2. ROTEIRO DO VÍDEO PITCH DE 5 MINUTOS (YOUTUBE)

- **00:00 - 01:00:** Apresentação do grupo, instituição, tema EduGrade e a ODS 4 (Lucas).
- **01:00 - 02:30:** Demonstração do software em funcionamento: cálculo de média, tratamento de erros e dados salvos (Caio).
- **02:30 - 03:45:** Estratégia de Versionamento GitFlow e commits semânticos no GitHub (Gabriel).
- **03:45 - 05:00:** Metodologia TDD, execução dos testes unitários e pipeline de CI no GitHub Actions (Fernando).
