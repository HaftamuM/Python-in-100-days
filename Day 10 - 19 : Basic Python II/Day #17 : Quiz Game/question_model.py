class Question: 

    def __init__(self, q_text, q_answer) -> None:
        self.text = q_text
        self.answer = q_answer

new_q = Question("2+1", "false")
print(new_q.text)