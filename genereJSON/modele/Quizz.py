class Quizz():
    def __init__(self, name, description, questions):
        self.name = name
        self.description = description
        #questions est un tableau de Question
        self.questions = questions
        
    #def ajouteQuestionAleatoireConversionBinaire(self):
        #création d'une question aléatoire de conversion binaire
        #r1 = Reponse(...)
        #...
        #q1 = Question(...)
        
        #self.questions.append(q1)
        #return st
    
    #def ajouteQuestionAleatoireComplementA2(self):
        #création d'une question aléatoire de conversion binaire
        #r1 = Reponse(...)
        #...
        #q1 = Question(...)
        
        #self.questions.append(q1)
        #return st

    def toJSON(self):
        st = '{\n' \
              '     "name": "' + self.name + '",\n'\
              '     "questions": \n' \
              '         [\n'

        i = 0
        while i < (len(self.questions) - 1):
            st += self.questions[i].toJSON() + ','
            i = i + 1

        st += self.questions[len(self.questions) - 1].toJSON()

        st +=  '         ],\n' \
               '     "description": "' + self.description + '"\n' \
               '}'
        return st