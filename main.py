"""
Interface Principal de Linha de Comando (CLI) - EduGrade.
Calculadora e Gestão de Desempenho Acadêmico vinculada à ODS 4.
Tratamento robusto de erros com try/except e interface limpa para apresentação.
"""

import sys
from src.calculator import GradeCalculator
from src.exceptions import AcademicError, InvalidGradeError, InvalidWeightError
from src.manager import AcademicManager


def print_header():
    print("=" * 65)
    print("    🎓 EDUGRADE - GESTÃO & CALCULADORA DE NOTAS ACADÊMICAS")
    print("        Trabalho A3 - Gestão e Qualidade de Software")
    print("        Vinculado à ODS 4 (Educação de Qualidade)")
    print("=" * 65)


def display_team():
    print("\n👥 INTEGRANTES DO GRUPO:")
    print(" • Lucas Henrique Miranda  - RA: 325131396 (Intro & Planejamento)")
    print(" • Caio Duraes             - RA: 325132875 (Dev & Arquitetura)")
    print(" • Gabriel Ferreira        - RA: 325140970 (Documentação & GitFlow)")
    print(" • Fernando Almeida        - RA: 326132695 (Qualidade, TDD & CI/CD)")
    print("-" * 65)


def quick_calculation_flow():
    print("\n--- [CÁLCULO RÁPIDO DE MÉDIA ACADÊMICA] ---")
    try:
        a1 = float(input("Informe a nota da A1 (0 a 10): "))
        GradeCalculator.validate_grade(a1)

        a2 = float(input("Informe a nota da A2 (0 a 10): "))
        GradeCalculator.validate_grade(a2)

        p1 = float(input("Informe o peso da A1 (padrão 0.4): ") or "0.4")
        p2 = float(input("Informe o peso da A2 (padrão 0.6): ") or "0.6")

        assessments = {
            "A1": {"grade": a1, "weight": p1},
            "A2": {"grade": a2, "weight": p2}
        }

        media = GradeCalculator.calculate_weighted_mean(assessments)
        status = GradeCalculator.get_status(media)

        print("\n" + "*" * 40)
        print(f"📊 MÉDIA CALCULADA: {media:.2f}")
        print(f"📌 SITUAÇÃO: {status}")

        if status == "APROVADO":
            print("🎉 Parabéns! Aluno aprovado por média.")
        elif status == "RECUPERACAO":
            needed = GradeCalculator.calculate_required_exam_grade(media)
            print(f"⚠️ Aluno em Exame Final. Nota necessária na Prova Final: {needed:.2f}")
        else:
            print("❌ Aluno reprovado sem direito a exame final.")
        print("*" * 40)

    except ValueError:
        print("\n[ERRO DE ENTRADA]: Você deve digitar um número válido (ex: 7.5 ou 8).")
    except AcademicError as ex:
        print(f"\n[REGRA ACADÊMICA]: {ex}")


def student_management_flow(manager: AcademicManager):
    print("\n--- [GESTÃO DE ESTUDANTE E HISTÓRICO] ---")
    ra = input("Informe o RA do aluno: ").strip()
    name = input("Informe o nome do aluno: ").strip()

    try:
        manager.register_student(ra, name)
        discipline = input("Nome da disciplina (ex: Gestão e Qualidade de Software): ").strip()
        manager.add_subject(ra, discipline)

        n_evals = int(input("Quantas avaliações deseja lançar? (ex: 2): "))
        for i in range(1, n_evals + 1):
            eval_name = input(f"Nome da avaliação #{i} (ex: A{i}): ").strip()
            grade = float(input(f"Nota para {eval_name} (0 a 10): "))
            weight = float(input(f"Peso para {eval_name} (ex: 0.5): "))
            manager.launch_grade(ra, discipline, eval_name, grade, weight)

        report = manager.get_subject_report(ra, discipline)
        print("\n" + "=" * 50)
        print(f"📄 BOLETIM ACADÊMICO - {report['student_name']} (RA: {ra})")
        print(f"📚 Disciplina: {report['subject']}")
        print(f"📈 Média Ponderada: {report['average']:.2f}")
        print(f"📌 Situação Final: {report['status']}")
        if report['status'] == "RECUPERACAO":
            print(f"⚠️ Exame Final: Precisa tirar ao menos {report['needed_in_exam']:.2f}")
        print("💾 Dados salvos com sucesso em 'data/students.json'.")
        print("=" * 50)

    except ValueError:
        print("\n[ERRO]: Digite valores numéricos válidos.")
    except Exception as e:
        print(f"\n[ERRO]: {e}")


def seed_group_demo(manager: AcademicManager):
    """Pré-carrega os 4 integrantes do grupo com dados reais para demonstrar ao vivo ao professor."""
    team = [
        {"ra": "325131396", "name": "Lucas Henrique Miranda", "a1": 8.5, "a2": 9.0},
        {"ra": "325132875", "name": "Caio Duraes", "a1": 7.0, "a2": 8.0},
        {"ra": "325140970", "name": "Gabriel Ferreira", "a1": 8.0, "a2": 8.5},
        {"ra": "326132695", "name": "Fernando Almeida", "a1": 9.5, "a2": 9.0},
    ]
    for member in team:
        manager.register_student(member["ra"], member["name"])
        manager.launch_grade(member["ra"], "Gestão e Qualidade de Software", "A1", member["a1"], 0.4)
        manager.launch_grade(member["ra"], "Gestão e Qualidade de Software", "A2", member["a2"], 0.6)
    print("\n✅ Sucesso! Os 4 integrantes foram carregados no banco de dados!")


def main():
    manager = AcademicManager()
    while True:
        print_header()
        print("1 - Visualizar Integrantes do Grupo e Papéis")
        print("2 - Cálculo Rápido de Média e Situação (Simulador)")
        print("3 - Cadastrar Aluno, Lançar Notas e Gerar Boletim")
        print("4 - Carregar Dados dos 4 Integrantes para Demonstração")
        print("5 - Sair")
        print("-" * 65)

        choice = input("Escolha uma opção (1-5): ").strip()

        if choice == "1":
            display_team()
        elif choice == "2":
            quick_calculation_flow()
        elif choice == "3":
            student_management_flow(manager)
        elif choice == "4":
            seed_group_demo(manager)
        elif choice == "5":
            print("\nEncerrando EduGrade. Sucesso na apresentação do A3!")
            sys.exit(0)
        else:
            print("\n⚠️ Opção inválida. Digite de 1 a 5.")

        input("\nPressione [Enter] para continuar...")


if __name__ == "__main__":
    main()
