from typing import Tuple, Union

import numpy as np

from qiskit.opflow.primitive_ops.pauli_sum_op import PauliSumOp

from qc_grader.grade import grade_json, grade_number
from qc_grader.util import paulisumop_to_json


criteria: dict = {}


def grade_lab4_ex1a(matmult_result: complex) -> None:
    ok, _ = grade_number(matmult_result, 'lab4', 'ex1a', **criteria)


def grade_lab4_ex1b(shot_result: complex) -> None:
    ok, _ = grade_number(shot_result, 'lab4', 'ex1b', **criteria)


def grade_lab4_ex2a(H_tfi: PauliSumOp) -> None:
    answer = {
        'qubit_op': paulisumop_to_json(H_tfi)
    }
    ok, _ = grade_json(answer, 'lab4', 'ex2a', **criteria)


def grade_lab4_ex2b(tfi_result: Tuple) -> None:
    answer = []
    for t in tfi_result:
        if isinstance(t, np.ndarray):
            answer.append(t.tolist())
        else:
            answer.append(t)
    ok, _ = grade_json(answer, 'lab4', 'ex2b', **criteria)


def grade_lab4_ex3(*args) -> None:
    print('Grading not yet available')
