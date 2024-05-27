import pickle
import jsonpickle

from typeguard import typechecked

from typing import Callable

from qiskit import QuantumCircuit

from qc_grader.grader.grade import grade, get_problem_set

_challenge_id = 'iqc_2024'

@typechecked
def grade_lab5_ex1(
   gates_cut: set,
   swap_depth: int,
   cut_depth: float
) -> None:
   answer_dict = {
     'gates_cut': gates_cut,
     'swap_depth': swap_depth,
     'cut_depth': cut_depth
   }
   answer = pickle.dumps(answer_dict).decode('ISO-8859-1')
   
   grade(answer, 'lab5-ex1', _challenge_id) 