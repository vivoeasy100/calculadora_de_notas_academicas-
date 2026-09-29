import unittest
import tempfile
import os
from src.calculator import GradeCalculator
from src.exceptions import InvalidGradeError, InvalidWeightError
from src.manager import AcademicManager


class TestGradeCalculator(unittest.TestCase):
    """Testes Unitários (TDD) para o módulo GradeCalculator."""

    def test_arithmetic_mean_success(self):
        # AAA Pattern (Arrange, Act, Assert)
        grades = [7.0, 8.0, 9.0]
        mean = GradeCalculator.calculate_arithmetic_mean(grades)
        self.assertEqual(mean, 8.0)

    def test_arithmetic_mean_empty_list_raises_error(self):
        with self.assertRaises(ValueError):
            GradeCalculator.calculate_arithmetic_mean([])

    def test_arithmetic_mean_invalid_grade_raises_exception(self):
        with self.assertRaises(InvalidGradeError):
            GradeCalculator.calculate_arithmetic_mean([7.0, 11.5])

        with self.assertRaises(InvalidGradeError):
            GradeCalculator.calculate_arithmetic_mean([-1.0, 8.0])

    def test_weighted_mean_success(self):
        assessments = {
            "A1": {"grade": 6.0, "weight": 0.4},
            "A2": {"grade": 8.0, "weight": 0.6}
        }
        # (6.0 * 0.4) + (8.0 * 0.6) = 2.4 + 4.8 = 7.2
        mean = GradeCalculator.calculate_weighted_mean(assessments)
        self.assertEqual(mean, 7.2)

    def test_weighted_mean_invalid_weight_raises_error(self):
        assessments = {
            "A1": {"grade": 7.0, "weight": 0.0}
        }
        with self.assertRaises(InvalidWeightError):
            GradeCalculator.calculate_weighted_mean(assessments)

    def test_status_approved(self):
        self.assertEqual(GradeCalculator.get_status(7.5), "APROVADO")
        self.assertEqual(GradeCalculator.get_status(6.0), "APROVADO")

    def test_status_exam_recuperacao(self):
        self.assertEqual(GradeCalculator.get_status(5.5), "RECUPERACAO")
        self.assertEqual(GradeCalculator.get_status(4.0), "RECUPERACAO")

    def test_status_failed_reprovado(self):
        self.assertEqual(GradeCalculator.get_status(3.9), "REPROVADO")
        self.assertEqual(GradeCalculator.get_status(1.5), "REPROVADO")

    def test_required_exam_grade_calculation(self):
        # Média 4.0, meta 5.0 -> (5 * 2) - 4 = 6.0
        required = GradeCalculator.calculate_required_exam_grade(current_mean=4.0, target_final=5.0)
        self.assertEqual(required, 6.0)

        # Média 5.0, meta 5.0 -> 5.0
        required2 = GradeCalculator.calculate_required_exam_grade(current_mean=5.0, target_final=5.0)
        self.assertEqual(required2, 5.0)


class TestAcademicManager(unittest.TestCase):
    """Testes de Integração e Domínio para o AcademicManager."""

    def test_register_student_and_report(self):
        fd, temp_path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        try:
            manager = AcademicManager(storage_path=temp_path)

            ra = "326132695"
            name = "Fernando Almeida"
            manager.register_student(ra, name)

            manager.launch_grade(ra, "Gestão e Qualidade de Software", "A1", 8.0, weight=0.4)
            manager.launch_grade(ra, "Gestão e Qualidade de Software", "A2", 9.0, weight=0.6)

            report = manager.get_subject_report(ra, "Gestão e Qualidade de Software")
            self.assertEqual(report["student_name"], name)
            self.assertEqual(report["average"], 8.6)
            self.assertEqual(report["status"], "APROVADO")
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)


if __name__ == "__main__":
    unittest.main()
