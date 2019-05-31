import unittest

from genereJSON.modele.Reponse import Reponse

class ReponseTest(unittest.TestCase):

    def setUp(self):
        self.r1 = Reponse("fb", "le Dimanche 14 Juillet 2019.", 0, 0, 0, 0, "shortanswerquestionanswer", 0)

    def testGet(self):
        self.assertEqual(self.r1.feedback, "fb")
        self.assertEqual(self.r1.text, "le Dimanche 14 Juillet 2019.")
        self.assertEqual(self.r1.penalty, 0)
        self.assertEqual(self.r1.usecase, 0)
        self.assertEqual(self.r1.fraction, 0)
        self.assertEqual(self.r1.hidden, 0)
        self.assertEqual(self.r1.typeq, "shortanswerquestionanswer")
        self.assertEqual(self.r1.correct, 0)

if __name__ == '__main__':
    unittest.main()