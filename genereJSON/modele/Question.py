class Question():
    def __init__(self, feedback, questiontext, usecase, hidden, typeq, name, answers):
        self.feedback = feedback
        self.answers = answers
        self.questiontext = questiontext
        self.usecase = usecase
        self.hidden = hidden
        self.typeq = typeq
        self.name = name

    def getNbQuestions(self):
        return len(self.answers)

    def toJSON(self):
        st = '{\n' \
              '     "feedback": "' + self.feedback + '",\n'\
              '     "answers": \n' \
              '         [\n'

        i = 0
        while i < (len(self.answers)-1):
            st += self.answers[i].toJSON() + ','
            i = i + 1

        #le dernier élement n'a pas de virgule à la fin
        st += self.answers[len(self.answers)-1].toJSON()

        st +=  '         ],\n' \
              '     "questiontext": "' + self.questiontext + '",\n' \
              '     "usecase": ' + str(self.usecase) + ', \n' \
              '     "hidden": ' + str(self.hidden) + ',\n' \
              '     "type": "' + self.typeq + '",\n' \
              '     "name": "' + self.name + '"\n' \
              '}'
        return st

