"""
Módulo de Exceções Customizadas para Regras de Domínio Acadêmico.
Atende aos requisitos de Tratamento de Erros e Clean Code.
"""


class AcademicError(Exception):
    """Exceção base para o domínio acadêmico."""
    pass


class InvalidGradeError(AcademicError):
    """Lançada quando a nota informada está fora da faixa válida (0 a 10)."""
    pass


class InvalidWeightError(AcademicError):
    """Lançada quando os pesos das avaliações são inconsistentes ou menores/iguais a zero."""
    pass


class StudentNotFoundError(AcademicError):
    """Lançada quando um aluno consultado não existe no sistema."""
    pass
