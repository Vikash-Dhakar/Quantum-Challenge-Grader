from typeguard import typechecked
from qiskit import QuantumCircuit
from qc_grader.grader.grade import grade, get_problem_set

_challenge_id = 'fall_2022'

@typechecked
def grade_lab3_ex1(qc: QuantumCircuit) -> None:
    grade(qc, 'ex3-1', _challenge_id)

@typechecked
def grade_lab3_ex2(qc: QuantumCircuit) -> None:
    grade(qc, 'ex3-2', _challenge_id)

@typechecked
def grade_lab3_ex3(qc: QuantumCircuit) -> None:
    grade(qc, 'ex3-3', _challenge_id)

@typechecked
def grade_lab3_ex4(qc: QuantumCircuit) -> None:
    grade(qc, 'ex3-4', _challenge_id)

@typechecked
def grade_lab3_ex5(qc: QuantumCircuit) -> None:
    grade(qc, 'ex3-5', _challenge_id)

@typechecked
def grade_lab3_ex6(qc: QuantumCircuit) -> None:
    grade(qc, 'ex3-6', _challenge_id)

@typechecked
def grade_lab3_ex7(qc: QuantumCircuit) -> None:
    grade(qc, 'ex3-7', _challenge_id)