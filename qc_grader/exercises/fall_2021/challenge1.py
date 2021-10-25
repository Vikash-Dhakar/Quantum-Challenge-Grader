import pickle
import jsonpickle

from typeguard import typechecked

from qiskit.algorithms.minimum_eigen_solvers import VQE, QAOA
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms.minimum_eigen_optimizer import MinimumEigenOptimizer

from qc_grader.grade import grade_and_submit


@typechecked
def grade_ex1a(qp: QuadraticProgram) -> None:
    answer = jsonpickle.encode(qp.export_as_lp_string())
    grade_and_submit(answer, '1a')


@typechecked
def grade_ex1b(vqe: VQE, qp: QuadraticProgram) -> None:
    meo = MinimumEigenOptimizer(vqe)
    result = meo.solve(qp)
    answer = pickle.dumps(result).decode('ISO-8859-1')
    grade_and_submit(answer, '1b')


@typechecked
def grade_ex1c(qp: QuadraticProgram) -> None:
    answer = jsonpickle.encode(qp.export_as_lp_string())
    grade_and_submit(answer, '1c')


@typechecked
def grade_ex1d(qaoa: QAOA, qp: QuadraticProgram) -> None:
    meo = MinimumEigenOptimizer(qaoa)
    result = meo.solve(qp)
    answer = pickle.dumps(result).decode('ISO-8859-1')
    grade_and_submit(answer, '1d')
