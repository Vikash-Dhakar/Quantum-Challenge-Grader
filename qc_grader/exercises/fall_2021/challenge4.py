from typing import Any, Callable
from typeguard import typechecked
import pickle

from qiskit import Aer
from qiskit.algorithms import QAOA
from qiskit.utils import QuantumInstance
from qiskit.providers.ibmq.job.ibmqjob import IBMQJob
from qiskit_optimization.problems.quadratic_program import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_optimization.applications import Knapsack

from qc_grader.grade import grade_and_submit, run_using_problem_set, prepare_solver, get_problem_set
from qc_grader.api import get_server_endpoint

seed = 42
time_limit_4b = 20
time_limit_4c = 12
precision_limit = 0.75
shots = 1024
backend = Aer.get_backend("qasm_simulator")

criteria: dict = {
    'max_qubits': 28,
    'min_cost': 1000,
    'check_gates': True
}

basis_gates = [
    'u1', 'u2', 'u3', 'cx', 'cz', 'id',
    'x', 'y', 'z', 'h', 's', 'sdg', 't',
    'tdg', 'swap', 'ccx',
    'unitary', 'diagonal', 'initialize',
    'cu1', 'cu2', 'cu3', 'cswap',
    'mcx', 'mcy', 'mcz',
    'mcu1', 'mcu2', 'mcu3',
    'mcswap', 'multiplexer', 'kraus', 'roerror'
]

@typechecked
def grade_ex4a(quadratic_program: QuadraticProgram) -> None:
    answer = {
        'qp': quadratic_program.export_as_lp_string()
    }
    grade_and_submit(answer, '4a')


@typechecked
def grade_ex4b(function: Callable) -> None:
    answer_dict = run_using_problem_set(
        function,
        '4b',
        params_order=['L1', 'L2', 'C1', 'C2', 'C_max']
    )

    problem_set_index = answer_dict['index']
    values, weights, max_weight = answer_dict['result']
    
    prob = Knapsack(values = values,
                    weights = weights, 
                    max_weight = max_weight)
    qp = prob.to_quadratic_program()
    qins = QuantumInstance(backend = Aer.get_backend('qasm_simulator'),
                           shots = shots, 
                           seed_simulator = seed, 
                           seed_transpiler = seed)
    qaoa_mes = QAOA(quantum_instance = qins, reps = 2)
    qaoa = MinimumEigenOptimizer(qaoa_mes)
    result = qaoa.solve(qp)

    answer_dict = {
            'index': problem_set_index,
            'result': result
            }
    answer = pickle.dumps(answer_dict).decode('ISO-8859-1')

    grade_and_submit(answer, '4b')


def exec_qc(qc, backend):
    tqc = transpile(qc, basis_gates=["u1", "u2", "u3", "cx"], optimization_level=0)
    num_ops = tqc.count_ops()
    depth = tqc.depth()
    qobj = assemble(tqc, shots=shots, seed_simulator=seed)
    job = backend.run(qobj)
    return job, num_ops, depth


def prepare_ex4c(solver_func: Callable) -> IBMQJob:
    return prepare_solver(
        solver_func,
        '4c',
        **criteria,
        basis_gates=basis_gates,
        shots=1000,
        seed_simulator=12345,
        optimization_level=0
    )

@typechecked
def grade_ex4c(function: Callable) -> None:
    answer_dict = run_using_problem_set(
        function,
        '4c',
        params_order=['L1', 'L2', 'C1', 'C2', 'C_max']
    )

    problem_set_index = answer_dict['index']
    values, weights, max_weight = answer_dict['result']
    qc = function(L1, L2, C1, C2, C_max)
    job, num_ops, depth = exec_qc(qc, backend)
 

    answer_dict = {
            'index': problem_set_index,
            'result': result
            }
    answer = pickle.dumps(answer_dict).decode('ISO-8859-1')

    grade_and_submit(answer, '4b')

