from typing import Any
import jsonpickle

from qiskit_optimization.problems.quadratic_program import QuadraticProgram
from qiskit_optimization.algorithms.minimum_eigen_optimizer import MinimumEigenOptimizationResult

from qc_grader.grade import grade_and_submit, run_using_problem_set


def grade_ex4a(quadratic_program: QuadraticProgram) -> None:
    objective = quadratic_program.objective

    answer_dict = {
        'offset': objective.constant,
        'matrix': objective.quadratic.to_array(symmetric=True),
        'linear coeff': objective.linear.to_array()
    }
    grade_and_submit(answer_dict, 'ex4', 'partA')


def grade_ex4b(function: Any) -> None:
    answer = run_using_problem_set(
        function,
        'ex4', 'partB',
        params_order=['L1', 'L2', 'C1', 'C2', 'Cmax']
    )
    if answer:
        grade_and_submit(answer, 'ex4', 'partB')


def grade_ex4c(answer: Any) -> None:
    print('Grading not yet available')
