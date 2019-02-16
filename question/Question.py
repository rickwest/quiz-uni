import copy
import random


class QuestionCollection:
    """A wrapper around a dictionary of Questions"""

    def __init__(self):
        self.__questions = {}

    @property
    def questions(self):
        return list(self.__questions.values())

    def add(self, question):
        if not question in self.__questions.values():
            self.__questions[question.ident] = question
            return True
        return False

    def __len__(self):
        return len(self.__questions)


class QuestionBank(QuestionCollection):
        """Singleton to create ONE list of questions to be used in the tests"""
        __instance = None

        @classmethod
        def getInstance(cls):
            if not cls.__instance:
                cls.__instance = QuestionBank()
                cls.__instance.__bank = QuestionCollection()
            return cls.__instance


class Question:
    __identifiers = []

    def __init__(self, question, answer, tags, points=10, ident=''):
        self._question = question
        self._answer = answer
        self._points = points
        self._tags = tags

        if ident:
            self._ident = ident
        else:
            ident = random.randint(1000, 9999)
            while ident in type(self).__identifiers:
                ident = random.randint(1000, 9999)
            type(self).__identifiers += [ident]
            self._ident = "question" + str(ident)

    @property
    def ident(self):
        return self._ident

    def getTags(self):
        return self._tags

    def setTags(self, tags):
        self._tags = tags

    def getPoints(self):
        return self._points

    def setPoints(self, points):
        self._points = points

    def clone(self):
        return copy.copy(self)

    @staticmethod
    def stringInputToList(x):
        """Static method that takes a string, splits on a comma and returns a list,
        also making sure remove any empty strings from the list"""
        return list(filter(None, [y.strip() for y in x.split(',')]))
