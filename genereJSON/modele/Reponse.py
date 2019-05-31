from typing import Any

class Reponse():
    def __init__ (self, feedback, text, penalty, usecase, fraction, hidden, typeq, correct):
        self.feedback = feedback
        self.text = text
        self.penalty = penalty
        self.usecase = usecase
        self.fraction =fraction
        self.hidden = hidden
        self.typeq = typeq
        self.correct = correct

    def default(self, o):
        return o.__dict__

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def toJSON(self):
        st = '{\n' \
              '     "feedback": "' + self.feedback + '",\n'\
              '     "text": "' + self.text + '",\n' \
              '     "penalty": ' + str(self.penalty) + ',\n' \
              '     "usecase": ' + str(self.usecase) + ', \n' \
              '     "fraction": ' + str(self.fraction) + ',\n' \
              '     "hidden": ' + str(self.hidden) + ',\n' \
              '     "type": "' + self.typeq + '",\n' \
              '     "correct": "' + str(self.correct) + '"\n' \
              '}'

        return st
