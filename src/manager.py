"""
Módulo de Gerenciamento Acadêmico e Persistência de Dados (JSON).
Permite cadastrar disciplinas, alunos, avaliações e exportar relatórios.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
from src.calculator import GradeCalculator
from src.exceptions import StudentNotFoundError


class AcademicManager:
    """Gerencia estudantes e suas respectivas disciplinas e notas."""

    def __init__(self, storage_path: Optional[str] = "data/students.json"):
        self.storage_path = Path(storage_path) if storage_path else None
        self.students: Dict[str, dict] = {}
        self.load()

    def register_student(self, ra: str, name: str) -> None:
        """Cadastra um novo estudante no sistema."""
        ra_clean = str(ra).strip()
        if not ra_clean or not name.strip():
            raise ValueError("RA e Nome são obrigatórios.")
        if ra_clean in self.students:
            return  # Já cadastrado
        self.students[ra_clean] = {
            "name": name.strip(),
            "subjects": {}
        }
        self.save()

    def add_subject(self, ra: str, subject_name: str) -> None:
        """Adiciona uma disciplina ao histórico do estudante."""
        ra_clean = str(ra).strip()
        if ra_clean not in self.students:
            raise StudentNotFoundError(f"Estudante com RA '{ra_clean}' não localizado.")
        
        subj = subject_name.strip()
        if subj not in self.students[ra_clean]["subjects"]:
            self.students[ra_clean]["subjects"][subj] = {
                "assessments": {}
            }
            self.save()

    def launch_grade(self, ra: str, subject_name: str, eval_name: str, grade: float, weight: float = 1.0) -> None:
        """Lança uma nota com peso em uma disciplina do estudante."""
        ra_clean = str(ra).strip()
        if ra_clean not in self.students:
            raise StudentNotFoundError(f"Estudante com RA '{ra_clean}' não localizado.")

        subj = subject_name.strip()
        if subj not in self.students[ra_clean]["subjects"]:
            self.add_subject(ra_clean, subj)

        GradeCalculator.validate_grade(grade)
        if weight <= 0:
            raise ValueError("O peso deve ser maior que zero.")

        self.students[ra_clean]["subjects"][subj]["assessments"][eval_name] = {
            "grade": float(grade),
            "weight": float(weight)
        }
        self.save()

    def get_subject_report(self, ra: str, subject_name: str) -> dict:
        """Gera boletim detalhado da disciplina para o estudante."""
        ra_clean = str(ra).strip()
        if ra_clean not in self.students:
            raise StudentNotFoundError(f"Estudante com RA '{ra_clean}' não localizado.")

        subj_data = self.students[ra_clean]["subjects"].get(subject_name)
        if not subj_data or not subj_data["assessments"]:
            return {
                "subject": subject_name,
                "average": None,
                "status": "SEM NOTAS",
                "needed_in_exam": None
            }

        assessments = subj_data["assessments"]
        mean = GradeCalculator.calculate_weighted_mean(assessments)
        status = GradeCalculator.get_status(mean)
        needed_exam = GradeCalculator.calculate_required_exam_grade(mean) if status == "RECUPERACAO" else 0.0

        return {
            "student_name": self.students[ra_clean]["name"],
            "subject": subject_name,
            "assessments": assessments,
            "average": mean,
            "status": status,
            "needed_in_exam": needed_exam
        }

    def save(self) -> None:
        """Persiste os dados em arquivo JSON com tratamento de integridade."""
        if not self.storage_path:
            return
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(self.students, f, indent=2, ensure_ascii=False)

    def load(self) -> None:
        """Carrega dados salvos com tolerância a falhas (resiliência)."""
        if not self.storage_path or not self.storage_path.exists():
            return
        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                self.students = json.load(f)
        except (json.JSONDecodeError, OSError):
            self.students = {}
