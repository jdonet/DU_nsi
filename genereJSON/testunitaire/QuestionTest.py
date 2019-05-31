import unittest

from genereJSON.modele.Question import Question
from genereJSON.modele.Reponse import Reponse

class ReponseTest(unittest.TestCase):

    def setUp(self):
        r1 = Reponse("fb", "le Dimanche 14 Juillet 2019.", 0, 0, 0, 0, "shortanswerquestionanswer", 0)
        r2 = Reponse("fb", "le Jeudi", 0, 0, 0, 0, "shortanswerqr", 1)
        r3 = Reponse("fb", "le Vendredi", 0, 0, 0, 0, "shortanswerqr", 0)

        listRep = []
        listRep.append(r1)
        listRep.append(r2)
        listRep.append(r3)

        self.q1 = Question("fb", "A travers le monde , leprochain Pi day ou jour de Pi tombera :", 0, 0, "shortanswer",
                      "Le prochain Jour de Pi", listRep)


    def testGet(self):
        self.assertEqual(self.q1.feedback, "fb")
        self.assertEqual(self.q1.getNbQuestions(), 3)
        self.assertEqual(self.q1.questiontext, "A travers le monde , leprochain Pi day ou jour de Pi tombera :")
        self.assertEqual(self.q1.usecase, 0)
        self.assertEqual(self.q1.hidden, 0)
        self.assertEqual(self.q1.typeq, "shortanswer")
        self.assertEqual(self.q1.name, "Le prochain Jour de Pi")


if __name__ == '__main__':
    unittest.main()