
from ..api import get_challenge_question_set

def get_question_id(lab_id: str, ex_id: str) -> int:
    try:
        question_name = f'{lab_id}/{ex_id}'
        question_set = get_challenge_question_set()

        if isinstance(question_set[0], dict):
            questions = list(filter(lambda q: question_name in q['name'], question_set))
            return questions[0]['id']
        else:
            return question_set.index(question_name) + 1
    except Exception:
        return -1
