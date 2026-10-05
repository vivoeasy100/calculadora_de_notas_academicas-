"""
Módulo de Domínio: Calculadora Acadêmica (EduGrade).
Desenvolvido com foco em Testabilidade (TDD), Código Limpo e Alta Coesão.
"""

from typing import Dict, List, Optional
from src.exceptions import InvalidGradeError, InvalidWeightError


class GradeCalculator:
    """
    Responsável pelo cálculo de médias, situação acadêmica e nota necessária para exame.
    Padrão institucional:
    - Média mínima de aprovação direta: 7.0 (ou 6.0 configurável)
    - Média mínima para prestar exame final: 4.0
    - Abaixo de 4.0: Reprovação direta
    """

    DEFAULT_APPROVAL_GRADE = 6.0
    DEFAULT_EXAM_MIN_GRADE = 4.0

    @staticmethod
    def validate_grade(grade: float) -> None:
        """Valida se uma nota é numérica e pertence ao intervalo [0.0, 10.0]."""
        if not isinstance(grade, (int, float)):
            raise InvalidGradeError(f"A nota deve ser um valor numérico. Recebido: {type(grade).__name__}")
        if grade < 0.0 or grade > 10.0:
            raise InvalidGradeError(f"Nota inválida: {grade}. As notas devem estar entre 0.0 e 10.0.")

    @classmethod
    def calculate_arithmetic_mean(cls, grades: List[float]) -> float:
        """Calcula a média aritmética simples de uma lista de notas."""
        if not grades:
            raise ValueError("A lista de notas não pode ser vazia.")
        for g in grades:
            cls.validate_grade(g)
        return round(sum(grades) / len(grades), 2)

    @classmethod
    def calculate_weighted_mean(cls, assessments: Dict[str, Dict[str, float]]) -> float:
        """
        Calcula média ponderada a partir de um dicionário:
        Formato: {"A1": {"grade": 7.0, "weight": 0.4}, "A2": {"grade": 8.0, "weight": 0.6}}
        """
        if not assessments:
            raise ValueError("As avaliações não foram informadas.")

        total_weighted_sum = 0.0
        total_weights = 0.0

        for name, data in assessments.items():
            grade = data.get("grade")
            weight = data.get("weight")

            if grade is None or weight is None:
                raise ValueError(f"Dados incompletos para a avaliação '{name}'. Requer 'grade' e 'weight'.")

            cls.validate_grade(grade)

            if weight <= 0:
                raise InvalidWeightError(f"O peso da avaliação '{name}' deve ser maior que zero.")

            total_weighted_sum += grade * weight
            total_weights += weight

        if total_weights <= 0:
            raise InvalidWeightError("A soma dos pesos deve ser maior que zero.")

        return round(total_weighted_sum / total_weights, 2)

    @classmethod
    def get_status(
        cls,
        final_mean: float,
        passing_grade: float = DEFAULT_APPROVAL_GRADE,
        exam_threshold: float = DEFAULT_EXAM_MIN_GRADE
    ) -> str:
        """Retorna o status acadêmico do aluno com base na média obtida."""
        cls.validate_grade(final_mean)
        if final_mean >= passing_grade:
            return "APROVADO"
        elif final_mean >= exam_threshold:
            return "RECUPERACAO"
        else:
            return "REPROVADO"

    @classmethod
    def calculate_required_exam_grade(
        cls,
        current_mean: float,
        target_final: float = 5.0
    ) -> float:
        """
        Calcula quanto o estudante precisa tirar na prova final/exame para atingir a meta mínima.
        Fórmula padrão: (current_mean + exam_grade) / 2 = target_final
        => exam_grade = (target_final * 2) - current_mean
        """
        cls.validate_grade(current_mean)
        required = (target_final * 2) - current_mean
        required = max(0.0, required)
        return min(10.0, round(required, 2))
 
 
# Modulo otimizado para alta performance e calculo preditivo de notas 
